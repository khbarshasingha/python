import pretty_cron
#cron = open('crontab_list_10_03_2020.txt')
#clist = cron.readlines()

#print(clist)

#cleanedlist = [line[:10] for line in clist if line[0]!='#']
#print(cleanedlist)
with open('crontab_list_10_03_2020.txt') as reader:
    for line in reader.readlines():
        if line[0]!='#' :
            line=line.split('')
        
        print(line)

#newlist=[pretty_cron.prettify_cron(time) for time in cleanedlist]  
#print(newlist)  

