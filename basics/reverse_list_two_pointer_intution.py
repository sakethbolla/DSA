def reverse_list():
    l = [1,2,3,4,4,5]
    a,b = 0, len(l)-1
    while a<b:
        l[a], l[b] = l[b],l[a]
        a +=1
        b -=1
    return l
print(reverse_list())