from decimal import *
n=int(input())

for i in range(1,n+1):
	print(Decimal(i), " " , oct(i).lstrip('0o'), " ",hex(i).lstrip('0x').upper()," ",bin(i).lstrip('0b'))
	print(Decimal(i), " " , oct(i), " ",hex(i)," ",bin(i),"\n")