import requests,random,time

def getmzjpg():
    req=requests.get('https://api.941ka.cn/api/mnxz/')
    wjm=int(random.randint(1,9)*time.time())
    print(wjm)
    f=open(str(wjm)+'.jpg','wb')
    f.write(req.content)
    f.close()

while True:
    getmzjpg()
