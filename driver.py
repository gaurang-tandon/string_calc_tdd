import re

def add(numbers:str):
    number_list = re.split(r'[;\n,//]', numbers)
    number_list = [int(x.strip()) for x in number_list if x]
    return sum(number_list)
    


print(add('//;\n1;2\n,\n34,,,3'))