import requests 
import requests,json
from bs4 import BeautifulSoup as BS
from time import sleep
import sys,os, time, json,termcolor 

print ('\033[1;95mWelcome')
sleep (1)
print ()
print ('\033[1;92mclick on this link to get password👇')
#sleep (0.1)
print ()
link="\033[1;93m https://miklpro.com/scs4Je"
print (link)
#sleep (1)
print ()
password=input ('\033[1;92m》Enter Password Script :  \033[1;96m')
sleep (1)

'''rrr=requests.get('https://pastelink.net/vj5ydi3d').text
soup=BS(rrr,'html.parser')
lxc=(soup.find('div',{'class':'body-display'})).text'''

if password =="Abdullah0912":
    print ()
    print ('\033[1;96m》True Password《')
    sleep (1)
else:
    print ()
    print ('\033[1;91mError Password')
    exit()
import time, sys 
print ()


import os, time, pyfiglet,sys
c=('\033[1;092m××××××××××××××××××××××××××××××××××××××××××××××××××××')
for I in c+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.030)
print ()
d =('\033[1;092m############# Welcome To Abdullah Script ##########')
for I in d +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.030)
print ()
p=('\033[1;092m############## Script Orange 300 Unit ############')
for I in p+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.030)
print ()
u=('\033[1;092m########## Projected By Abdullah Salah ##########')
for I in u+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.030)

print ('\033[1;092m')





logo='''
██████╗░░█████╗░░█████╗░  ██╗░░░██╗███╗░░██╗██╗████████╗  ██████╗░██╗░░░██╗
╚════██╗██╔══██╗██╔══██╗  ██║░░░██║████╗░██║██║╚══██╔══╝  ██╔══██╗╚██╗░██╔╝
░█████╔╝██║░░██║██║░░██║  ██║░░░██║██╔██╗██║██║░░░██║░░░  ██████╦╝░╚████╔╝░
░╚═══██╗██║░░██║██║░░██║  ██║░░░██║██║╚████║██║░░░██║░░░  ██╔══██╗░░╚██╔╝░░
██████╔╝╚█████╔╝╚█████╔╝  ╚██████╔╝██║░╚███║██║░░░██║░░░  ██████╦╝░░░██║░░░
╚═════╝░░╚════╝░░╚════╝░  ░╚═════╝░╚═╝░░╚══╝╚═╝░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░

░█████╗░██████╗░██████╗░██╗░░░██╗██╗░░░░░██╗░░░░░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░░░██║██║░░░░░██║░░░░░██╔══██╗██║░░██║
███████║██████╦╝██║░░██║██║░░░██║██║░░░░░██║░░░░░███████║███████║
██╔══██║██╔══██╗██║░░██║██║░░░██║██║░░░░░██║░░░░░██╔══██║██╔══██║
██║░░██║██████╦╝██████╔╝╚██████╔╝███████╗███████╗██║░░██║██║░░██║
╚═╝░░╚═╝╚═════╝░╚═════╝░░╚═════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝'''

for I in logo +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.0010)

print ()



i='''\033[;092mTelegram channel : 

http://t.me/Techno0099

Youttube channel  :
    
https://youtube.com/channel/UCAbtkFAe9yyX0HJNFXyKJUg 
    
Facebook  :
        
https://www.facebook.com/AbdullahSalah0099/'''


for I in i +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.0040)

print ()
print ('\033[;093m*'*60)
print ()
choose='''\033[1;092m What's Your Current System  :  
\033[1;093m
  [1] الو 14

[2] الو اليومى

[3] الو الأسبوع

[4] نظام قديم

'''
print (choose)



cc=input ('\033[1;092m》Choose Your Current System : \033[1;096m')

print ()

num=input ('\033[1;092m》Enter Your Phone Number : \033[1;096m')
print ()

pas=input ('\033[1;092m》Enter Your Password : \033[1;096m')
print ()





#####################################




url='https://services.orange.eg/SignIn.svc/SignInUser'

data='{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":%s,"isAndroid":true,"password":%s}'%(num,pas)


headers={
"Content-Type": "application/json; charset=UTF-8",

"Content-Length": str(len(data)),

"Host": "services.orange.eg",

"Connection": "Keep-Alive",

"Accept-Encoding": "gzip",

"User-Agent": "okhttp/3.12.0"
}



r=requests.post (url,headers=headers,data=data).json()
if (r['SignInUserResult']['ErrorCode'])==0:
    print ('\033[1;096mDone Login')
elif (r['SignInUserResult']['ErrorCode'])==9:
    print ('\033[1;091mError Number Or Password')
    exit()


UserID=(r['SignInUserResult']['UserData']['UserID'])





#####################################



print ()
ctv=input ('\033[1;092m》Enter ctv : \033[1;096m')
print  ()
htv=input ('\033[1;092m》Enter htv : \033[1;096m')
print ()



if cc=="1":
    data1={"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"currentServiceClassID":"82","dial":num,"isCoin":True,"migratedToTariffPlanID":"84","migratedToTariffPlanName":"الو الأسبوعى","userID":UserID,"isEasyLogin":False,"password":pas}
    
    url1="https://services.orange.eg/CoinServices.svc/MigrateServiceClass"

        
    headers1={
        "_ctv": ctv,
        
        "_htv": htv,
        
        "Content-Type": "application/json; charset=UTF-8",

        "Content-Length": str(len(data1)),

        "Host": "services.orange.eg",

        "Connection": "Keep-Alive",

        "Accept-Encoding": "gzip",

        "User-Agent": "okhttp/3.12.0"}
        
    
    r1=requests.post(url1, headers=headers1, json=data1).json()
    
    
    
    if (r1['MigrateServiceClassResult']['ErrorCode'])==2:
        print ("\033[1;091mCan't add,may Error Choice")
    elif (r1['MigrateServiceClassResult']['ErrorCode'])==0:
        print('\033[1;096mDone Added 300 Unit')





#####################################




elif cc=="2":
    
    url2="https://services.orange.eg/CoinServices.svc/MigrateServiceClass"
    
    headers2={
    "_ctv": ctv,
    
    "_htv": htv,
    
    "Content-Type": "application/json; charset=UTF-8",

    "Content-Length": "316",

    "Host": "services.orange.eg",

    "Connection": "Keep-Alive",

    "Accept-Encoding": "gzip",

    "User-Agent": "okhttp/3.12.0"}
    
    data2={"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"currentServiceClassID":"83","dial":num,"isCoin":True,"migratedToTariffPlanID":"84","migratedToTariffPlanName":"الو الأسبوعى","userID":UserID,"isEasyLogin":False,"password":pas}
    
    r2=requests.post(url2, headers=headers2, json=data2).json()
   
    if (r2['MigrateServiceClassResult']['ErrorCode'])==2:
        print ("\033[1;091mCan't add,may Error Choice")
    elif (r2['MigrateServiceClassResult']['ErrorCode'])==0:
        print ('\033[1;096mDone Added 300 Unit')

    else:
        
        print ('\033[1;091Unknown Error, Try Again')





#####################################






elif cc=="3":
    
    url3="https://services.orange.eg/CoinServices.svc/MigrateServiceClass"
            
    headers3={
            "_ctv": ctv,
            "_htv": htv,
            "Content-Type": "application/json; charset=UTF-8",

            "Content-Length": "316",

            "Host": "services.orange.eg",

            "Connection": "Keep-Alive",

            "Accept-Encoding": "gzip",

            "User-Agent": "okhttp/3.12.0"}
            
    data3={"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"currentServiceClassID":"84","dial":num,"isCoin":True,"migratedToTariffPlanID":"82","migratedToTariffPlanName":"الو 14","userID":UserID,"isEasyLogin":False,"password":pas}
    
    r3=requests.post(url3, headers=headers3, json=data3).json()

    if (r3['MigrateServiceClassResult']['ErrorCode'])==2:
        print ("\033[1;091mCan't add,may Error Choice")
    elif (r3['MigrateServiceClassResult']['ErrorCode'])==0:
        print ('\033[1;096mDone Added 300 Unit')
    else:
        print ('\033[1;091Unknown Error, Try Again')
 




#####################################


elif cc=="4":

    url4="https://services.orange.eg/CoinServices.svc/MigrateServiceClass"
    
    headers4={"_ctv": ctv,

    "_htv": htv,
    "Content-Type": "application/json; charset=UTF-8",

    "Content-Length": "316",

    "Host": "services.orange.eg",

    "Connection": "Keep-Alive",

    "Accept-Encoding": "gzip",

    "User-Agent": "okhttp/3.12.0"}
    

    data4={"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"currentServiceClassID":"400","dial":num,"isCoin":False,"migratedToTariffPlanID":"84","migratedToTariffPlanName":"الو  الأسبوعي","userID":"9e74885c-3a35-45e1-83eb-840c59efd03b","isEasyLogin":False,"password":pas}
    
    r4=requests.post (url4,headers=headers4,json=data4).json()
    
    if (r4['MigrateServiceClassResult']['ErrorCode'])==2:
        print ("\033[1;091mCan't add,may Error Choice")
    elif (r4['MigrateServiceClassResult']['ErrorCode'])==0:
        print ('\033[1;096mDone Added 300 Unit')
    else:
        print ('\033[1;091Unknown Error, Try Again')


else:
    print ('\033[1;091mError Choice')
