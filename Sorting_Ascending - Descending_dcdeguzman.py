# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:25:10 2020

@author: JADE
"""

#Ascending
#Bubble Sort
def bubbleSort(number_list):
    for sortnum in range(len(number_list)-1,0,-1):
        for i in range(sortnum):
            if number_list[i]>number_list[i+1]:
                temp = number_list[i]
                number_list[i] = number_list[i+1]
                number_list[i+1] = temp

print ("Bubble Sort")
number_list = [24, 3, 60, 7, 9, 11]
bubbleSort(number_list)
print("Ascending order is ", number_list)

#Descending
number_list.sort(reverse = True)
print("Descending order is ", number_list)
print("                      ")
print("                      ")


#Selection Sort
def selectionSort(number_list):
   for sortnum in range(len(number_list)-1,0,-1):
       max_position=0
       for location in range(1,sortnum+1):
           if number_list[location]>number_list[max_position]:
               max_position = location

       temp = number_list[sortnum]
       number_list[sortnum] = number_list[max_position]
       number_list[max_position] = temp

print ("Selection Sort")
number_list = [24, 3, 60, 7, 9, 11]
selectionSort(number_list)
print("Ascending order is ", number_list)

#Descending
number_list.sort(reverse = True)
print("Descending order is ", number_list)
print("                      ")
print("                      ")


#Insertion Sort
def insertionSort(number_list):
   for index in range(1,len(number_list)):

     current_value = number_list[index]
     position = index

     while position>0 and number_list[position-1]>current_value:
         number_list[position]=number_list[position-1]
         position = position-1

     number_list[position]=current_value

print ("Insertion Sort")
number_list = [24, 3, 60, 7, 9, 11]
insertionSort(number_list)
print("Ascending order is ", number_list)

#Descending
number_list.sort(reverse = True)
print("Descending order is ", number_list)
print("                      ")
print("                      ")


number_list = [24, 3, 60, 7, 9, 11]
odd = 0
even = 0
for x in number_list:
        if not x % 2:
    	     even+=1
        else:
    	     odd+=1
print("Count numbers")
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)
print("                      ")
print("                      ")


sum = 0
number_list = [24, 3, 60, 7, 9, 11]
for num in number_list:
    sum = sum +num
average  = sum / len(number_list)
print ("Sum of numbers is : ", sum)
print ("Average of numbers is: ", average )









