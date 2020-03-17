import pretty_cron
#cron = open('crontab_list_10_03_2020.txt')
#clist = cron.readlines()

#print(clist)

#cleanedlist = [line[:10] for line in clist if line[0]!='#']
#print(cleanedlist)
time=[]
clist=[]
with open('crontab_list_10_03_2020.txt') as reader:
    for line in reader.readlines():
        if line[0]!='#' and line[0]!='\n' and line[0]!=' ':
            data=line.split(' ')
            print(data[-1])
            #time.append(line[:5])
            #filepath=data[-3]
            #clist.append(time)
            #clist.append(filepath)
        #print(line)
print(data)


#newlist=[pretty_cron.prettify_cron(time) for time in cleanedlist]  
#print(newlist)  

