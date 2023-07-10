import time
from numpy.random import randint
import matplotlib.pyplot as plt
def mergesort(array):
    if(len(array))>1:
        r=len(array)//2
        L=array[:r]
        M=array[r:]
        mergesort(L)
        mergesort(M)
        i=j=k=0
        while i<len(L) and j<len(M):
            if L[i]<M[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k]=M[j]
                j+=1
            k+=1
        while i<len(L):
            array[k]=L[i]
            i+=1
            k+=1
        while j<len(M):
            array[k]=M[j]
            j+=1
            k+=1

def printlist(array):
    for i in range(len(array)):
        print(array[i],end=" ")
    print()

if __name__ == '__main__' :
    array=[6,5,12,10,9,1]
    mergesort(array)
print(array)
def readinput():
    a=[]
    n=int(input("Enter the no.of TV channels:"))
    print("Enter the no.of viewers")
    for i in range(0,n):
        l=int(input())
        a.append(l)
    return a

elements=list()
times=list()
global labeldata
print("1.Mergesort ")
ch=int(input("Enter the choice"))
if(ch==1):
    array=readinput()
    mergesort(array)
    labeldata="MergeSort"
    print("Sorted Array is:")
    print(array)
print("******Running Time Analysis******")
for i in range(1,10):
    array=randint(0,1000*i,1000*i)
    print(i)
    start=time.time()

    if ch==1:
        mergesort(array)
    end=time.time()
    print(len(array),"Elements Sorted by",labeldata,end-start)
    elements.append(len(array))
    times.append(end-start)
plt.xlabel('List length')
plt.ylabel('Timke complexity')
plt.plot(elements,times,label=labeldata)
plt.grid()
plt.legend()
plt.show()