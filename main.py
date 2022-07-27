import csv
import os

os.system('clear')
os.system('rm -rf ./script.txt')

input_file = "source.csv"
outputfile = "script.txt"
string = ""
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['name']
        low_port = str(row['low_port'])
        high_port = str(row['high_port'])

        current_string = "config firewall service custom\nedit " + name + "\nset comment comment\nset udp-portrange " + low_port + ":" + high_port + "\nnext\nend\n\n"
        string += current_string

outfile = open(outputfile, 'w')
outfile.write(string)
outfile.close()