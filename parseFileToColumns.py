import csv, ast

f= open('pathToCSV.csv', 'r')
reader = csv.reader(f)

#Allows for the column names to be in one word
def trimTheName(list):      
    final_list = []
    for headers in list:
        final_list.append(''.join(headers.split()))
    return final_list

longest, headers, type_list = [], [], []

#Finding the datatype
def datatype(val, current_type):
    try:
        # Evaluates numbers to an appropriate type, and strings an error
        t = ast.literal_eval(val)
    except ValueError:
        return 'varchar'
    except SyntaxError:
        return 'varchar'
    if type(t) in [int, int, float]:
       if (type(t) in [int, int]) and current_type not in ['float', 'varchar']:
           # Use smallest possible int type
           if (-32768 < t < 32767) and current_type not in ['int', 'bigint']:
               return 'smallint'
           elif (-2147483648 < t < 2147483647) and current_type not in ['bigint']:
               return 'int'
           else:
               return 'bigint'
    if type(t) is float and current_type not in ['varchar']:
           return 'decimal'
    else:
        return 'varchar'

for row in reader:
    if len(headers) == 0:
        headers = row
        for col in row:
            longest.append(0)
            type_list.append('')
    else:
        for i in range(len(row)):
            # NA is the csv null value
            if type_list[i] == 'varchar' or row[i] == 'NA':
                pass
            else:
                var_type = datatype(row[i], type_list[i])
                type_list[i] = var_type
            if len(row[i]) > longest[i]:
                longest[i] = len(row[i])
headers = trimTheName(headers)
f.close()

#create a table
statement = 'create table table_name ('
for i in range(len(headers)):
    if type_list[i] == 'varchar':
        statement = (statement + '\n{} varchar({}),').format(headers[i].lower(), str(longest[i]))
    else:
        statement = (statement + '\n' + '{} {}' + ',').format(headers[i].lower(), type_list[i])

statement = statement[:-1] + ');'
