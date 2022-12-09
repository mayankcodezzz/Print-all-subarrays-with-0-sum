#Print all subarrays with sum zero
def insert(d,key,value):
    d.setdefault(key,[]).append(value)

def printallsublist(list):
    d={}
    insert(d,0,-1)
    total=0
    for i in range(len(list)):
        total=total+list[i]
        if total in d:
            ls=d.get(total)
            for j in ls:
                print(list[j+1:i+1])
        insert(d,total,i)

list=[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
printallsublist(list)
