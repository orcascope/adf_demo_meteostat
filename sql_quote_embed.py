import re
test_string = "select 'Mr'||firstname, lastname||' sir'"
test_string2 = "select 'Mr'||firstname, lastname||' sir' as lname"
test_string=test_string2

def add_pipes_quotes(test_string):
    p = re.compile("('[^']*')")
    start_pos = 0
    result = ""
    for m in p.finditer(test_string):
        result = result+"'"+test_string[start_pos:m.start()]+"'||''''||"+m.group()+"||''''||"
        first = 0
        start_pos = m.end()

    result = result+"'"+test_string[start_pos:]+"'||\n"
    print(result)
    return result


with open('input_sql_text.sql', 'r') as file_in:
    sql_input = file_in.read().splitlines()
    for rec in sql_input:
        sql_output_line = add_pipes_quotes(rec)
