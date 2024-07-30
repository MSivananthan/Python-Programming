size=int(input("Give the number of elements you want in array: "))
arr=[]
#taking input of the list
for i in range(0,size):
    elem=int(input("Enter the number "+str(i +1)+": "))
    arr.append(elem)
#taking average of the elements of the list
avg=sum(arr)/size
print("Average of the array elements is ",avg)
