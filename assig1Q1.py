import random as ramo
import numpy as numpo 
import matplotlib.pyplot as pygraph

#declare all lists/arrays

all_nums = []
all_cos = []
all_sin = []

#generate and print random numbers from 1 to 90 
print("\n \n 10 Random Numbers")
for i in range(0,10):
    all_nums.append(ramo.randint(0,90))

for print_nums in range(len(all_nums)):
    print(all_nums[print_nums])

#calculate COS of all and print
print("\n \n Cos of 10 Random Numbers")
for cs in range(0,10):
    new_element_push = all_nums[cs]
    all_cos.append(numpo.cos(new_element_push))
    COS = all_cos

#print COS numbers
print("\n \n Number\t\tCOS of Number")
for print_cos in range(len(all_nums)):
    print(all_nums[print_cos],"\t\t",COS[print_cos])
    
    
#calculate SIN of all and print
print("\n\n Sin of 10 Random Numbers")
for sn in range(0,10):
    new_element_push2 = all_nums[sn]
    all_sin.append(numpo.sin(new_element_push2))
    SIN = all_sin
    
#print SIN of numbers
print("\n\n Number\t\tSIN of Number")
for print_sin in range(len(all_nums)):
    print(all_nums[print_sin],"\t\t",COS[print_sin])

#plot the numbers on graph, assign labels and legend
pygraph.plot(COS,color='red',linestyle='dashed',marker='o',label='cos') #creates COS curve
pygraph.plot(SIN, color='green', linestyle='dashed', marker='o', label='sine') #creates SIN curve
legen = pygraph.subplot()
legen.legend() #prints legend on the graph
pygraph.xlabel('X', fontsize=18)
pygraph.ylabel('Y', fontsize=16)
pygraph.rcParams["figure.figsize"] = 12,9 #change the default size(values of size) of graph in program
pygraph.show()
    


