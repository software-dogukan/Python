import numpy as np
numbers=[]
def find_mod(num):
    mod=[]
    count_numbers=int(len(num))
    for x in range(len(num)):
        x=x+1
        if count_numbers%x==0:
            mod.append(x)
    find_max=[]
    for x in range(0,len(mod)-1):
        for j in range(1,len(mod)-1):
            if int(mod[x]*mod[j])==count_numbers:
                find_max.append(mod[x])
                find_max.append(mod[j])
    if int(len(find_max))!=0:
        arr=np.array(num)
        print(arr.reshape(find_max[int(len(find_max)/2)],find_max[int(len(find_max)/2)+1]))
    else:
        print("Your numbers are 1D numbers")
        print(num)
while True:
    print("Can you give number?(If you give zero, programing will exit)")
    number=int(input())
    if number==0:
        break
    else:
        numbers.append(number)
find_mod(numbers)