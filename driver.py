import re

def add(numbers:str):
    number_list = re.split(r'[;\n,//]', numbers)

    number_list = [int(x.strip()) for x in number_list if x]

    negative_numbers = [x for x in number_list if x < 0]

    if negative_numbers:
        raise Exception(f'negative numbers not allowed {",".join([str(x) for x in negative_numbers])}')

    return sum(number_list)
    


print(add('//;\n1;-2\n,\n-34,,,3'))