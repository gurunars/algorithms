from typing import List, Callable

from dataclasses import dataclass

from statistics import mean, stdev

Num = float

Features = Input = List[Num]

Label = Output = Num

ErrorFactor = Num

Bias = Num

Weights = List[Num]

FeatureScalingFunction = Callable[[Num], Num]

FeatureScalingFunctionTemplate = Callable[[Input], FeatureScalingFunction]

Converged = Callable[[List[Num]], bool]

ModelFunctionFormula = Callable[[Weights, Bias, Input], Output]

@dataclass
class Example:
    features: Features
    label: Label

@dataclass
class ModelFunction:
    weights: Weights
    bias: Bias
    formula: ModelFunctionFormula

    def __call__(self, input: Input) -> Output:
        return self.formula(self.weights, self.bias, input)

    def __repr__(self):
        return f"ModelFunction({self.weights}, {self.bias}, {self.formula.__name__})"

ExampleScalingFunction = Callable[[Example], Example]

CostFunction = Callable[[ModelFunction, List[Example]], ErrorFactor]

GenerateZeroParameters = Callable[[List[Example]], ModelFunction]


def linear_model_function_formula(
    weights: Weights,
    bias: Bias,
    input: Input
) -> Output:
    """
    >>> linear_model_function_formula(
    ...     weights = [1, 2, 3],
    ...     bias = 11,
    ...     input = [4, 5, 7]
    ... )
    46
    """
    return bias + sum(
        pair[0] * pair[1]
        for pair in zip(weights, input)
    )


def get_minmax_feature_scaling_function(numbers: Input) -> FeatureScalingFunction:
    """
    Guarantees all features will have the exact same scale
    but does not handle outliers well.

    >>> def round_features(features) -> List[Num]:
    ...     return [round(it, 2) for it in features]

    >>> def rescale(features: List[Num]) -> List[Num]:
    ...     return round_features(map(
    ...         get_minmax_feature_scaling_function(features),
    ...         features
    ...     ))

    >>> rescale([300, 325, 300, 325, 350, 2000])
    [-0.18, -0.16, -0.18, -0.16, -0.15, 0.82]

    >>> rescale([0, 1, 3.2, 2.2, 2.4, 5])
    [-0.46, -0.26, 0.18, -0.02, 0.02, 0.54]
    """
    m = mean(numbers)
    d = max(numbers) - min(numbers)
    return lambda it: (it - m) / d


def get_zscore_feature_scaling_function(numbers: Input) -> FeatureScalingFunction:
    """
    Handles outliers, but does not produce normalized data with
    the exact same scale.

    >>> def round_features(features) -> List[Num]:
    ...     return [round(it, 2) for it in features]

    >>> def rescale(features: List[Num]) -> List[Num]:
    ...     return round_features(map(
    ...         get_zscore_feature_scaling_function(features),
    ...         features
    ...     ))

    >>> rescale([300, 325, 300, 325, 350, 2000])
    [-0.44, -0.4, -0.44, -0.4, -0.36, 2.04]

    >>> rescale([0, 1, 3.2, 2.2, 2.4, 5])
    [-1.32, -0.75, 0.52, -0.06, 0.06, 1.55]
    """
    m = mean(numbers)
    d = stdev(numbers)
    return lambda it: (it - m) / d


def get_example_scaling_function(
    examples: List[Example],
    feature_scaling_function_template: FeatureScalingFunctionTemplate
) -> ExampleScalingFunction:
    """
    >>> def round_features(features) -> List[Num]:
    ...     return [round(it, 2) for it in features]

    >>> def round_examples(examples):
    ...     return [
    ...         Example(
    ...             features=round_features(ex.features),
    ...             label=ex.label
    ...         )
    ...         for ex in examples
    ...     ]

    >>> def rescale(examples):
    ...     return round_examples(map(
    ...         get_example_scaling_function(
    ...             examples,
    ...             get_minmax_feature_scaling_function
    ...         ),
    ...         examples
    ...     ))

    >>> from pprint import pprint
    >>> pprint(rescale([
    ...     Example([300, 0], 11),
    ...     Example([325, 1], 2),
    ...     Example([300, 3.2], 4),
    ...     Example([325, 2.2], 6),
    ...     Example([350, 2.4], 7),
    ...     Example([2000, 5], 14),
    ... ]))
    [Example(features=[-0.18, -0.46], label=11),
     Example(features=[-0.16, -0.26], label=2),
     Example(features=[-0.18, 0.18], label=4),
     Example(features=[-0.16, -0.02], label=6),
     Example(features=[-0.15, 0.02], label=7),
     Example(features=[0.82, 0.54], label=14)]
    """

    j_count = len(examples[0].features)
    feature_scale_functions: List[FeatureScalingFunction] = [
        feature_scaling_function_template([ex.features[j] for ex in examples])
        for j in range(j_count)
    ]

    def scale_example(example: Example) -> Example:
        return Example(
            features=[feature_scale_functions[j](example.features[j]) for j in range(j_count)],
            label=example.label
        )

    return scale_example


def descend(
    model_function: ModelFunction,
    learning_rate: Num,
    examples: List[Example]
) -> ModelFunction:
    """
    >>> descend(
    ...     learning_rate = 1,
    ...     model_function = ModelFunction(
    ...         weights = [0],
    ...         bias = 0,
    ...         formula = linear_model_function_formula
    ...     ),
    ...     examples = [Example([1], 300), Example([2], 500)]
    ... )
    ModelFunction([650], 400, linear_model_function_formula)

    >>> descend(
    ...     learning_rate = 1,
    ...     model_function = ModelFunction(
    ...         weights = [0],
    ...         bias = 0,
    ...         formula = linear_model_function_formula
    ...     ),
    ...     examples = [Example([1], 300), Example([2], 500), Example([3], 650), Example([4], 900)]
    ... )
    ModelFunction([1712.5], 587.5, linear_model_function_formula)
    """
    def compute(w: Num, d: Num) -> Num:
        return w - learning_rate * d

    deltas = [model_function(ex.features) - ex.label for ex in examples]
    return ModelFunction(
        weights = [
            compute(
                w,
                mean(
                    ex.features[j] * deltas[i]
                    for i, ex in enumerate(examples)
                )
            )
            for j, w in enumerate(model_function.weights)
        ],
        bias = compute(model_function.bias, mean(deltas)),
        formula = model_function.formula
    )


def get_squared_error_cost(
    model_function: ModelFunction,
    examples: List[Example],
) -> ErrorFactor:
    """
    >>> get_squared_error_cost(
    ...     ModelFunction([0], 0, linear_model_function_formula),
    ...     [Example([1], 300), Example([2], 500)],
    ... )
    85000.0

    >>> get_squared_error_cost(
    ...     ModelFunction([0], 0, linear_model_function_formula),
    ...     [Example([1], 300), Example([2], 500), Example([3], 650), Example([4], 900)],
    ... )
    196562.5
    """
    return mean(
        (model_function(ex.features) - ex.label) ** 2
        for ex in examples
    ) / 2


def init_with_static_zero_parameters(
    formula: ModelFunctionFormula,
    examples: List[Example],
) -> ModelFunction:
    return ModelFunction(
        weights=[0] * len(examples[0].features),
        bias=0,
        formula=formula
    )


def gradient_descent(
    model_function: ModelFunction,
    get_cost: CostFunction,
    converged: Converged,
    feature_scale_function_template: FeatureScalingFunctionTemplate,
    examples: List[Example],
    iter_limit: int=100,
    learning_rate: Num=0.1,
) -> ModelFunction:
    costs: List[Num] = []
    scale = get_example_scaling_function(
        examples, feature_scale_function_template
    )
    examples = [scale(ex) for ex in examples]
    for _ in range(iter_limit):
        if converged(costs):
            break
        model_function = descend(
            model_function,
            learning_rate,
            examples
        )
        costs.append(get_cost(
            model_function,
            examples
        ))
    return ModelFunction(
        weights = model_function.weights,
        bias = model_function.bias,
        formula = lambda w, b, input: model_function.formula(
            w, b,
            scale(Example(input, 0)).features
        )
    )
