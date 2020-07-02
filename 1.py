print('Enter n')
n=int(input())
b=bool(int(input("Enter 1 or 0")))
if b==True:
    for x in range(n+1):
        print('*'*x)
else:
    for x in range(n,-1,-1):
        print('*'*x)
input()
