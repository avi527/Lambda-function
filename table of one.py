def table(n):
    return lambda a:a*n
n=input("enter number")
b=table(n)
for i in range(1,11):
    print(n,"X",i,"=",b(i))
