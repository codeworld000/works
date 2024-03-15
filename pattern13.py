print(1)
limit=int(input("enter the limit"))
for i in range(1,limit+1):
    for j in range(i):
        if   j==0 or i==limit or j+1==i  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
print(2)
lim=int(input("enter the limit"))
for i in range(lim):
    for j in range(lim-i):
        if   j==0 or j+1+i==lim or i==0 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



print(3)
lim=int(input("enter the limit"))
for i in range(lim):
    for k in range(i):
        print(" ",end="")
    for j in range(lim-i):
        if i==0 or j==0 or j+1+i==lim:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print(4)
lim=int(input("enter the limit"))
for i in range(lim):
    for k in range (i):
        print(" ",end=" ")
    for j in range(lim-i):
        if i==0 or j==0 or j+1+i==lim :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print(5)
lim=int(input("enter the limit"))
for i in range(lim):
    for k in range(lim-i):
        print(" ",end=" ")
    for j in range(i+1):
        if j==0 or j==i  or i+1==lim:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
print(6)
lim=int(input("enter the limit"))
for i in range(lim):
    for k in range(lim-i):
        print(" ",end="")
    for j in range(i+1):
        if j==0 or j==i  or i+1==lim:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()