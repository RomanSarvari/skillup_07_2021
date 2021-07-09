"""
Задание 2
Дан текстовый файл.
Необходимо создать новый файл и записать в него следующую
статистику по исходному файлу:
 ■ Количество символов;
 ■ Количество строк;
 ■ Количество гласных букв;
 ■ Количество согласных букв; 
 ■ Количество цифр.
 """

import os

file_1 = '/Users/Sarvari/skillup_07_2021/lesson_3.6/HW/hw_1_3.txt'


def symbols_count(file):
    with open(file, 'r') as t:
        symbols = t.read()
    return(len(symbols))

def lines_count(file):
    with open(file, 'r') as t:
        lines = t.readlines()
    return(len(lines))

def letter_number(symbols, list):
    count = 0
    for i in symbols:
        if i in list:
            count += 1
    return count


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
vovels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
    'x', 'z',
]

f_symbols = symbols_count(file_1)
f_lines = lines_count(file_1)
f_vowels = letter_number(open(file_1).read(), vovels)
f_consonants = letter_number(open(file_1).read(), consonants)
f_numbers = letter_number(open(file_1).read(), numbers)

stat = open('/Users/Sarvari/skillup_07_2021/lesson_3.6/HW/statistics.txt', mode="w")
stat.write(
    'Symbols counts:' + str(f_symbols)+' ''\n'+
    'Lines counts:' + str(f_lines)+' ''\n'+
    'Vovels counts:' + str(f_vowels)+' ''\n'+
    'Consonants counts:' + str(f_consonants)+' ''\n'+
    'Numbers counts:' + str(f_numbers)+' ''\n'
)
stat.close()

with open('/Users/Sarvari/skillup_07_2021/lesson_3.6/HW/statistics.txt', 'r') as task_file:
    for line in task_file:
        print(line, end=' ' '\n')
