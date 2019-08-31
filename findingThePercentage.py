n = int(input())
d={}
for _ in range(n):
	val = input()
	val = val.split(' ')
	name = val[0]
	m1=float(val[1])
	m2 = float(val[2])
	m3 = float(val[3])
	d[name]=[m1,m2,m3]
x=input()
print("%.2f"%(sum(d[x])/3))
