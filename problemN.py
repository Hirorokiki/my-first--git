L=input()
l=sorted(L)
A=[]
a=0
if len(l)==1:
    print("いいえ")
    exit()
if len(l)>=2:
    for i in range(1,len(l)):
        if l[i]!=l[i-1]:
            A.append(i-a)
            a=i
    if i==len(l)-1:
        A.append(len(l)-a)
for i in range(0,len(A)):
    count=1
    for j in range(0,len(A)):
        if A[i]==A[j] and i!=j:
            count=count+1
        if count>=3:
        print("いいえ")
        exit()
    if count==1:
        print("いいえ")
        exit()
print("はい")