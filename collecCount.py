from collections import Counter
x= int(input())
shoe_size=list(map(int, input().strip().split()))
n=int(input())
ct=Counter(shoe_size)
total=0
for _ in range(n):
    l=list(map(int, input().strip().split()))
    if l[0] in shoe_size:
        if ct[l[0]]>0:
            total+=l[1]
            ct[l[0]]-=1
print(total)
