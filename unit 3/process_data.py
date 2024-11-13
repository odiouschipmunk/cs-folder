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
def output_mr_b():
    with open('output.txt', 'w') as file:
        for row in csvdata:
            if 'mr b' in row:
                file.write(f'{row}\n')
output_mr_b()