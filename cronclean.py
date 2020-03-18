import pretty_cron
import pandas as pd

time=[]
out_dict = {'time_stamp':[], 'file_path':[], 'log_path':[]}
with open('crontab_list_10_03_2020.txt') as reader:
    for line in reader.readlines():
        if line[0]!='#' and line[0]!='\n' and line[0]!=' ' and line[0]!='M':
            data=line.split(' ')
            out_dict['time_stamp'].append(data[:5])
            try:
                sep_index = data.index('>>')
                if str.lower(data[sep_index+1 if data[sep_index+1]!='' else sep_index+2].strip('\n'))\
                    .endswith(tuple(['.log', '.out', '.txt', '.cronlog', '.py'])):
                    out_dict['file_path'].append(data[sep_index-1])
                    out_dict['log_path'].append(data[sep_index+1 if data[sep_index+1]!='' else sep_index+2])
                else:
                    out_dict['file_path'].append(data[-1]) 
                    out_dict['log_path'].append('')
                    print('Exception found\n::',data)
            except ValueError:
                out_dict['file_path'].append(data[-1]) 
                out_dict['log_path'].append('')
                    
df = pd.DataFrame(out_dict)
df.to_excel('out.xlsx')
print('done')
