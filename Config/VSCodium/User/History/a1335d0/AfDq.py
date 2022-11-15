my_str = ' I like python!              '
my_str = my_str.strip()
#? убирает пробелы в начале or в конце строки 
print(my_str)

#! можно так же использовать для обрезки не нужных нам символов передав их в качестве аргумента(" ")

my_str = my_str.strip('!')
print(my_str)

