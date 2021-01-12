import csv

with open('pokemon.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    f = open("output.py", "w")
    for row in csv_reader:
        output = f'{row[1]} = pokemon(\'{row[0]}\',\'{row[1].capitalize()}\',\'https://professorlotus.com/Sprites/{row[1].capitalize()}.gif\', [],[], 1, 20, \'s\',75,150,75,150)\n\n'
        print(f'\t#:{row[0]} Name:{row[1]}.')
        f.write(output)
    f.close()
    