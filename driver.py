def add(numbers:str):
    number_list = numbers.split(',')
    number_list = [int(x.strip()) for x in number_list if x]
    print(number_list)
    print(sum(number_list))
    


add('1,3,4,6,765,,1,3,4,')