import typer

from opentaxkr.ers import detect_report_type
from opentaxkr.ers.report import 전자신고서식
from opentaxkr.ers.양도소득세 import 양도소득세신고

app = typer.Typer()


@app.command()
def parse(filename: str):
    with open(filename, 'rb') as f:
        data = f.read()
        records = detect_report_type(data).parse(data.splitlines())
        print(records)
        # print(양도소득세신고.from_list_of_dict(records).records)


app()