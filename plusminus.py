n=int(input())
arr=list(map(int, input().split()))

pos=0;
neg=0;
zero=0;
for i in arr:
    
    if(i>0):
        pos+=1
    elif(i<0):
        neg+=1
    elif(i==0):
        zero+=1
print("{:.6f}\n{:.6f}\n{:.6f}".format((pos/n),(neg/n),(zero/n)))