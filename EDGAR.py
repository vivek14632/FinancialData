# download idx files: https://www.sec.gov/Archives/edgar/daily-index/2018/QTR1/
# create a secData folder in the location where you keep this .py file. This file will be used to store the data

import wget
fp = open('C:\\Users\\jeet\\Downloads\\form.idx', 'r')
data=fp.readlines()[11:]
fp.close()


for lines in data:
    temp=lines.split('\n')[0]
    temp=temp.split()
    if((temp[0]=='10-K') & (int(temp[-2][5:7])==1)):
        response = wget.download('http://www.sec.gov/Archives/'+temp[-1],'secData/')
