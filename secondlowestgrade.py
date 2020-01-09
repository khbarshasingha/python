if __name__ == '__main__':
    physics=[]
    names=[]
    x=[]
    n=int(input())
    for _ in range(0,n):
        st=[]
        name = input()
        st.append(name)
        score = float(input())
        st.append(score)
        physics.append(st)
    x=sorted(physics, key=lambda x:x[1])
    min1=x[n-1][1]  
    min2=physics[n-1][1]
    for i in x:
        if (i[1]<min1) :
            min2=min1
            min1=i[1]
            
        elif (i[1]<min2) and i[1] != min1:
            min2=i[1]
  
    for i in x:
        if i[1]==min2:
            names.append(i[0])    
    names.sort()
    for i in names:
        print(i)
