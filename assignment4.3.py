n=int(input("enter n :"))
a=1
print(a,end="\t")
b=3
print(b,end="\t")
c=5
for i in range (1,n-1):
    c=a+b
    print(c,end="\t")
    a=b
    b=c


        