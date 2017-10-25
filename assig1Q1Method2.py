import random as ramo
import numpy as numpo 
import matplotlib.pyplot as pygraph


all_nums = numpo.asarray([])
all_cos = numpo.asarray([])
all_sin = numpo.asarray([])


#generate and print random numbers from 1 to 90 
print("10 Random Numbers")
for i in range(0,10):
    all_nums = numpo.append(all_nums,ramo.randint(0,90))
#print(all_nums)
#print(SIN)
print("Number ")
for print_num in range(len(all_nums)):
    print(all_nums[print_num])
#take cos of all and print
print("Cos of 10 Random Numbers")
for cs in range(0,10):
    new_element_push = all_nums[cs]
    all_cos = numpo.append(all_cos,numpo.cos(new_element_push))
    COS = all_cos
#print(COS)
print("Number \t \t COS of Number")
for print_cos in range(len(all_nums)):
    print(all_nums[print_cos],"\t\t",COS[print_cos])
    
    
#take sin of all and print
print("Sin of 10 Random Numbers")
for sn in range(0,10):
    new_element_push2 = all_nums[sn]
    all_sin = numpo.append(all_sin,numpo.sin(new_element_push2))
    SIN = all_sin

#print(SIN)
print("Number \t \t SIN of Number")
for print_sin in range(len(all_nums)):
    print(all_nums[print_sin],"\t\t",COS[print_sin])
#plot the numbers on graph, assign labels and legend
pygraph.plot(COS,color='red',linestyle='dashed',marker='o',label='cos')
pygraph.plot(SIN, color='green', linestyle='dashed', marker='o', label='sine')
legen = pygraph.subplot()
legen.legend()
pygraph.xlabel('X', fontsize=18)
pygraph.ylabel('Y', fontsize=16)
pygraph.show()
    


