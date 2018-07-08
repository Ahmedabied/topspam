import requests,re,sys,_thread,time,os
try:
    url="https://www.sarahah.top/u/"+sys.argv[1]
    msg=sys.argv[2]
    headers={
        "Host": "www.sarahah.top","User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "Accept": "*/*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","Referer": url,"X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8","Connection": "keep-alive",
        }
    ip = [{'http':'http://'+str(i.split("\n")[0])} for i in open("proxy.list")]
    def sendmsg(url,msg,proxy,count):
        token,num,id,name=[re.findall(r'"([^"]*)"',i)[0] for i in re.findall("value.*",requests.get(url).text)]
        data={
            "ctl00$body$ScriptManager1":"ctl00$body$up|ctl00$body$btnSend","__EVENTTARGET":"ctl00$body$btnSend","__EVENTARGUMENT":"","__VIEWSTATE":token,"__VIEWSTATEGENERATOR":num,
            "ctl00$body$txtMessage":msg,"ctl00$body$hdnProfile":id,"ctl00$body$hdnProfileName":name,"__ASYNCPOST":"true",
            }
        with requests.session() as sessions:
            get=sessions.post(url,data=data,headers=headers,proxies=proxy)
        os.system('cls' if "win" in sys.platform else "clear" if "linux" in sys.platform else "exit")
        print("\033[35m COUNT   : "+str(i)+"\033[0m")
        print("\033[31m Message : "+str(msg)+"\033[0m")
        print("\033[33m Name    : "+str(name)+"\033[0m")
        print("\033[4m  ID      : "+str(id)+"\033[0m")
        print("\033[34m URL     : "+str(url)+"\033[0m")
        print("\033[91m Proxy   : "+str(proxy)+"\033[0m")
        print("\033[47m \033[47m \033[47m \033[47m \033[47m \033[47m \033[47m \033[0m")
    for i in range(len(ip)):
        _thread.start_new_thread(sendmsg,(url,msg,ip[i],i))
        time.sleep(0.403)
except:print("\033[94m"+sys.argv[0].split("\\")[::-1][0]+" [User Name] [Message]\033[0m")
