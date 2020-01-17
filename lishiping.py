import requests,re
#import parsel
def pagemp4(pageurl):
    response=requests.get(pageurl)
    html=response.text
    mp4_url=re.findall('srcUrl="(.*?)"',html)
    name=re.findall('<h1 class="video-tt">(.*?)</h1>',html)
    response=requests.get(mp4_url[0])
    f=open(name[0]+'.mp4','wb')
    f.write(response.content)
    f.close()
    print(name)

response=requests.get('https://www.pearvideo.com/category_8')
html=response.text
#print(html)
videoids=re.findall('<a href="(.*?)" class="vervideo-lilink actplay">',html)
for item in videoids:
    pagemp4('https://www.pearvideo.com/' + item)
#print(videoids)
