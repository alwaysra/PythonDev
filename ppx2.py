import re,requests,json
'''
皮皮虾无水印下载--解析版本
2020-10-06
'''
def ppxdownloadmp4(ppx_url):
    #ppx_url='https://h5.pipix.com/s/JyeSQ73/'
    response = requests.get(ppx_url)
    # 得到跳转真实URL
    jempurl = response.url
    # 得到视频ID
    id = re.findall('https://h5.pipix.com/item/(.*?)\?app_id', jempurl)
    #解析网址
    req=requests.get('https://tenapi.cn/ppx/?url='+ppx_url)
    html=req.text
    # print(req)
    # print(html)
    #解析JSON
    jg=json.loads(html)
    if len(id)>0:
        print(id[0])
    else:
        print("无法获得视频ID")
    print(jg['title'])
    print(jg['url'])
    response=requests.get(jg['url'])
    f=open(id[0]+'_'+jg['title']+'.mp4','wb')
    f.write(response.content)
    f.close()

if __name__ == '__main__':
    while True:
        try:
            ppx_url = input('输入分享网址：')
            ppxdownloadmp4(ppx_url)
        except KeyError:
            pass
