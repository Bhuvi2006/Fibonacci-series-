#Fibonacci series
a=int(input("Enter  the number: "))
#First number='n1'
n1=0
count=0
#Second number='n2'
n2=1
while count<a:
    print("The sequence is",n1)
    fs=n1+n2
    n1=n2
    n2=fs
    count+=1
print("Their sum is",fs)