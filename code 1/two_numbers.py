###########################################
###                                     ###
###     Author: Hamidreza Abooei        ###
###             9731303                 ###
###          Algrithm Design            ###
###                                     ###
###########################################


import random  # this library is for generating unsorted list
import time
# initializing the list and s

n = 1000000

random_list = []
for i in range(n):
    a = random.randint(1,n)
    random_list.append(a)

# print(random_list)

s = random.randint(2,2*n)
# print(s)

## code #1
start_time = time.time()

a = 0 
b = 0
flag = False
for i in random_list:
    for j in random_list:
        if (i + j == s):
            a = i 
            b = j
            flag = True
            break
    if(flag):
        break
            

print("a = " , a , " b = " , b , " s = " , s)
print("Execution time code #1 = " , time.time() - start_time)

## code #2
start_time = time.time()

sorted_list = sorted(random_list)
center_index = 0
for i in sorted_list:
    if ( i > ( s / 2 ) ):
        break
    center_index += 1
a,b = 0,0
flag = False
for i in range(center_index,len(sorted_list)):
    for j in range(center_index,1,-1):
        if (sorted_list[i] + sorted_list[j] == s):
            a = sorted_list[i]
            b = sorted_list[j]
            flag = True
            break
    if (flag):
        break


print("a = " , a , " b = " , b , " s = " , s)
print("Execution time code #2 = " , time.time() - start_time)


## code #3
start_time = time.time()

sorted_list = sorted(random_list)
center_index = 0
for i in sorted_list:
    if ( i > ( s / 2 ) ):
        break
    center_index += 1
a,b = 0,0
flag = False
for i in range(center_index,len(sorted_list)):
    for j in range(center_index,1,-1):
        if (sorted_list[i] + sorted_list[j] == s):
            a = sorted_list[i]
            b = sorted_list[j]
            flag = True
            break
        if (sorted_list[i] + sorted_list[j] < s):
            break
    if (flag):
        break


print("a = " , a , " b = " , b , " s = " , s)
print("Execution time code #3 = " , time.time() - start_time)
