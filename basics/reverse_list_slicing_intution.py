def reverse_list():
    l = [1,2,3,4,4,5]
    l[:] = l[::-1] #[:] = overwrites the list
    print(l)
print(reverse_list())