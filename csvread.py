import csv

with open('pokemon.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(f'\t#:{row[0]} Name:{row[1]}.')
        line_count += 1