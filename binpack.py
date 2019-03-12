#!/usr/bin/env python3

import sys
import os.path

class Bin:
    def __init__(self, size):
        self.size = size
        self.holdings = 0

    def __str__(self):      #added print function for personal clarity in testing
        return "[" + str(self.holdings) + " / " + str(self.size) + "]"

def first_fit(bin_size, item_list):
    bin_list = [Bin(bin_size)]
    for item in item_list:
        for bin in bin_list:        #checks if each bin can fit the current item
            if(item + bin.holdings <= bin.size):
                bin.holdings += item
                item = 0            #setting item to 0 if already added to a bin
                break
        
        if(item != 0):              #add a new bin if item cant fit
            new_bin = Bin(bin_size)
            new_bin.holdings = item
            bin_list.append(new_bin)
    return len(bin_list)


#sorts items into first available bin
def first_fit_regular(bin_size, item_list):
    bin_count = first_fit(bin_size, item_list)
    print("First Fit: " + str(bin_count) + ",", end=' ')

#orders by decreasing size, and then sorts by first available bin
def first_fit_decreasing(bin_size, item_list):
    item_list.sort(reverse=True)
    bin_count = first_fit(bin_size, item_list)
    print("First Fit Descreasing: " + str(bin_count) + ",", end=' ')

#sorts items by finding bin with least space left after item placed inside
def best_fit(bin_size, item_list):
    bin_list = [Bin(bin_size)]
    for item in item_list:
        best_bin = -1
        best_bin_value = bin_size + 1

        for i in range(len(bin_list)):
            current_value = bin_list[i].size - (bin_list[i].holdings + item)
            if(current_value == 0):                 #best possible fit, stop looking
                bin_list[i].holdings += item
                item = 0
                break
            elif(current_value > 0):                #item fits in bin
                if(best_bin_value > current_value): #check if better fit
                    best_bin = i
                    best_bin_value = current_value
                    
        if(item == 0):                              #best fit already found
            continue
        elif(best_bin != -1):                       #best fit found
            bin_list[best_bin].holdings += item
        else:                                       #no fit found, add new container
            new_bin = Bin(bin_size)
            new_bin.holdings = item
            bin_list.append(new_bin)
    print("Best Fit: " + str(len(bin_list)))



def main(file_name):
    lines = open(file_name).read().splitlines()         #read in file
    test_count = int(lines[0])                          #first line is # of tests
    current_test = 0
    while current_test < test_count:
        bin_size = int(lines[(current_test*3+1)])       #every test takes 3 lines, this grabs 
        items = lines[(current_test*3+3)]               #each tests data from the parsed file
        item_list = [int(item) for item in items.split()]
        current_test += 1

        print("Test Case " + str(current_test) + " ->", end=" ")
        first_fit_regular(bin_size, item_list)
        first_fit_decreasing(bin_size, item_list[:])    #sending a copy of the item list so original remains in given order
        best_fit(bin_size, item_list)

if __name__ == "__main__":
    main(sys.argv[1])