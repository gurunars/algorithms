

def header(content: str) -> str:
    return f'<th style="font-size: 1.2em;" align="left">{content}</th>'


out = f"""
<table class="docutils align-default">
    <tr>
        {header("Name")}
        {header("g(z)")}
        {header("g'(z)")}
        {header("Plot")}
    </tr>
    <tr>
        <td>Identity</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>RelU (Rectified Linear Unit)</td>
        <td></td>
        <td></td>
        <td>dfefefefr 2r2343 gfbsdgbefdfv</td>
    </tr>
    <tr>
        <td>Logistic (Sigmoid)</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Logistic (Sigmoid)</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>
"""
