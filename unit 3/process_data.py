import csv
#read from project_data.csv that is formatted as message, teacher name, class
def read_data():
    csvdata=None
    with open('project_data.csv', 'r') as file:
        reader=csv.reader(file)
        csvdata=list(reader)
    return csvdata
csvdata=read_data()
print(f'csv data: {csvdata}')
#if 'mr b' is in csv data, then output to output.txt
mr_b=[row for row in csvdata if 'mr b' in row]
print(f'mr b: {mr_b}')
print(f'type of mr b: {type(mr_b)}')
print(f'')
