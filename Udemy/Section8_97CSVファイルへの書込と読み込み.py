# -*- coding: utf-8 -*-
import csv

with open('test.csv', 'w', newline='') as csv_file:
    """
    newline=''を指定しないと、改行が2回入る。
    """
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})

print('------------------')

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])

