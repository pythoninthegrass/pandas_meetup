#!/usr/bin/env python3

import argparse
import pandas as pd
import xml.etree.ElementTree as ET
from icecream import ic
from pathlib import Path

# verbose icecream
ic.configureOutput(includeContext=True)

# argparse
parser = argparse.ArgumentParser(description='Generate CSV file from XML file.')
parser.add_argument('-i', '--input', help='Input XML file', required=False)
parser.add_argument('-o', '--output', help='Output CSV file', required=False)
args = parser.parse_args()

# get xml_id's
if args.input is not None:
    xml = args.input
else:
    xml_cwd = list(Path("raw").glob("*.xml"))
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
if args.output is None and not Path('output.csv').is_file():
    df.to_csv("output.csv", index=False)
elif args.output is None and Path('output.csv').is_file():
    df.to_csv("output.csv", index=False, mode='a', header=False)
else:
    df.to_csv(args.output, index=False)
