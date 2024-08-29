import re

def add(numbers:str):
    # IDENTIFYING DELIMITERS AND COMMA SEPERATED NUMBERS IN THE STRING AND PARSING THEM INTO A LIST
    number_list = re.split(r'[;\n,//]', numbers)
    
    # CONVERTING STRING NUMERIC CHARACTERS INTO INTEGERS AND REMOVING BLANK CHARACTERS AND EXTRA WHITE SPACES IF ANY
    number_list = [int(x.strip()) for x in number_list if x]
    
    # GETTING ALL THE NEGATIVE INTEGERS IN THE LIST IF ANY
    negative_numbers = [x for x in number_list if x < 0]

    # RAISING EXCEPTION IF ANY NEGATIVE INTEGER FOUND IN THE LIST/PROVIDED STRING
    if negative_numbers:
        raise Exception(f'negative numbers not allowed {",".join([str(x) for x in negative_numbers])}')
    
    # IF NO NEGATIVE INTEGERS FOUND THEN RETURNING THE SUM OF ALL INTEGERS IN THE STRING
    return sum(number_list)