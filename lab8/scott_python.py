#!/usr/bin/env python3
import json
import csv

with open('../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

csv_file = '../data/chacon.csv'

with open(csv_file, mode='a', newline='') as f:
    writer = csv.writer(f)

    for i in data:
        indicies = (data.index(i))
        line = f'{i["name"]},{i["html_url"]},{i["updated_at"]},{i["visibility"]}\n'
        if indicies < 5:
           f.write(line)
        else:
           pass
