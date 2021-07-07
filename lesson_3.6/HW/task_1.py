import difflib


file_1 = '/Users/Sarvari/skillup_07_2021/lesson_3.6/HW/hw_1_1.txt'
file_2 = '/Users/Sarvari/skillup_07_2021/lesson_3.6/HW/hw_1_2.txt'
file_3 = '/Users/Sarvari/skillup_07_2021/lesson_3.6/HW/hw_1_3.txt'

test1 = open(file_1, 'r')
test2 = open(file_2, 'r')
test3 = open(file_3, 'w')

list_1 = test1.readlines()
list_2 = test2.readlines()

k = 1
for i, j in zip(list_1, list_2):
    if i != j:
        test3.write("Line Number:" + str(k)+' ')
        test3.write(i.rstrip("\n") + ' ' + j)
    k = int(k)
    k = k+1

with open(file_3, "r") as modified_file:
    for line in modified_file:
        print(line, end="")
