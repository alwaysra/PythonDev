import requests,random,time,os

def getmzjpg():
    req=requests.get('https://api.941ka.cn/api/mnxz/')
    wjm=int(random.randint(1,9)*time.time())
    print(wjm)
    f=open('kamz\\'+str(wjm)+'.jpg','wb')
    f.write(req.content)
    f.close()

if __name__ == '__main__':
    folder = os.path.exists("kamz")
    if not folder:
        os.makedirs("kamz")
    while True:
        getmzjpg()

