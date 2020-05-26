
'''
皮皮虾无水印下载
'''
import re,requests

def ppxdownloadmp4(ppx_url):
    #分享链接
    #ppx_url='https://h5.pipix.com/s/bRvhQ8/'
    #'https://h5.pipix.com/s/b8w923/'
    response=requests.get(ppx_url)
    #得到跳转真实URL
    jempurl=response.url
    #得到视频ID
    id=re.findall('https://h5.pipix.com/item/(.*?)\?app_id',jempurl)
    #print(id)
    #6777547296595777796
    #拼接网址
    jxurl='https://h5.pipix.com/bds/webapi/item/detail/?item_id='+id[0]+'&source=share'
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    #print(jxurl)
    response=requests.get(url=jxurl,headers=headers)
    html=response.text
    #print(html)
    title = re.findall('"title":"(.*?)"', html)
    # 打印标题
    print(title[0])
    url=re.findall('video_fallback(.*?)","expires',html)
    print(len(url))
    if len(url)==1:
        url2 = re.findall('{"url":"(.*)', url[0])
        response = requests.get(url2[0])
        f = open(id[0] + '_'+title[0] + '.mp4', 'wb')
        f.write(response.content)
        f.close()
        print(id[0])
    elif len(url)==2:
        url2 = re.findall('{"url":"(.*)', url[0])
        response = requests.get(url2[0])
        f = open(id[0] + '_'+title[0] + '_神.mp4', 'wb')
        f.write(response.content)
        f.close()
        url2 = re.findall('{"url":"(.*)', url[1])
        response = requests.get(url2[0])
        f = open(id[0] + '_'+title[0] + '.mp4', 'wb')
        f.write(response.content)
        f.close()
        print(id[0])

if __name__ == '__main__':
    while True:
        try:
            ppx_url = input('输入分享网址：')
            ppxdownloadmp4(ppx_url)
        except KeyError:
            pass
