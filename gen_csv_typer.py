#!/usr/bin/env python3

import pandas as pd
import typer
import xml.etree.ElementTree as ET
from icecream import ic
from pathlib import Path

# verbose icecream
ic.configureOutput(includeContext=True)

# init typer app
app = typer.Typer()


def main(
    src: str = typer.Option(..., "--in", "-i", help="Input XML file"),
    out: str = typer.Option(..., "--out", "-o", help="Output CSV file")
    ):
    """Generate CSV file from XML file."""

    # get xml_id's
    if src is not None:
        xml = src
    else:
        xml_cwd = list(Path("xml").glob("*.xml"))
        xml = xml_cwd[0].name

    root = ET.parse(xml)

    id_list = []
    name_list = []

    for id in root.findall(".//id"):
        xml_id = id.text
        id_list.append(xml_id)

    for name in root.findall(".//name"):
        xml_name = name.text
        name_list.append(xml_name)

    zipped = zip(id_list, name_list)
    zipped = sorted(zipped, key=lambda col: col[1].casefold())
    ic(list(zipped))

    # zip lists
    df = pd.DataFrame(list(zipped), columns=["id", "name"])

    # export zipped list as csv with pandas
    if out is None and not Path(out).is_file():
        df.to_csv("output.csv", index=False)
    elif out is None and Path(out).is_file():
        df.to_csv("output.csv", index=False, mode='a', header=False)
    else:
        df.to_csv(out, index=False)


if __name__ == "__main__":
    try:
        typer.run(main)
    except SystemExit as e:
        typer.echo(f"Exiting with status code {e.code}")
        pass
