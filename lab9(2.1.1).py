def LinearSearch(array,k):
    for i in range (k):
        if (array [i] == k):
            return i
array=[7,10,12,14,1,20,29,37]
print (LinearSearch(array,14))
print (LinearSearch(array,29))
