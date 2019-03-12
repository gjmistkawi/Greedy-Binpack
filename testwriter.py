#!/usr/bin/env python
import random
import io

test_count = 20
file_input = str(test_count) + "\n"
for i in range(test_count):                 #write 20 test cases
    bin_size = random.randint(1,101)        #random bin size: 0 < x < 101
    file_input += str(bin_size) + "\n"

    item_count = random.randint(1,101)      #random item count: 0 < x < 101
    file_input += str(item_count)  + "\n" 

    for j in range(item_count):             #add random items from item count
        item = random.randint(1,bin_size)   #items can be no larger than bin size
        file_input += str(item) + " "

    file_input += "\n"

f = open('test.txt', 'w')
f.write(file_input)