import urllib.request as urllib
import re
import time
import socket
import os


def running(a, path):
    print("downloading " + a + " path: " + path)


def download(start, end, oriurl, split, path):   
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
    }

    opener=urllib.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.install_opener(opener)

    for i in range(start,end):
        url = oriurl + str(i)
        print("connecting to " + url)
        req = urllib.Request(url=url, headers=headers)
        request = urllib.urlopen(req)
        response = request.read()
        request.close()
        output = response.decode('utf-8')        
        urlarr = re.findall(r'new Audio\((.+?)\);', output)
        namere = re.search('<h5>(.+?)'+split+'(.+?)</h5>', output)
        filename = namere.group(2).strip()
        mp3url = "https:" + urlarr[0][1:-1]
        filepath = os.path.join(path, filename+".mp3")
        urllib.urlretrieve(mp3url, filepath, running(str(i), filepath))
        time.sleep(3)


if __name__ == '__main__':
    #1~138 - Done
    xiyouji = "https://ksfan.net/story/kai-shu-xi-you-ji-quan-ji/?page="
    #1~593 - Done
    sanguo = "https://ksfan.net/story/kai-shu-san-guo-yan-yi-he-ji/?page="
    #1~641
    lishi = "https://ksfan.net/story/kai-shu-jiang-li-shi/?page="
    #1~25
    naniya1 = "https://ksfan.net/story/na-ni-ya-chuan-qi-di-yi-bu/?page="
    #1~22
    naniya2 = "https://ksfan.net/story/na-ni-ya-chuan-qi-di-er-bu/?page="
    #1~13
    xiaowangzi = "https://ksfan.net/story/xiao-wang-zi/?page="
    #1~108
    chengyugushi = "https://ksfan.net/story/99-ge-cheng-yu-gu-shi/?page="
    #1~402
    gushi365 = "https://ksfan.net/story/kai-shu-365-ye/?page="
    #1~125
    shici = "https://ksfan.net/story/kai-shu-shi-ci-lai-le-he-ji/?page="
    #1~68
    changpian = "https://ksfan.net/story/jing-dian-chang-pian-ming-zhu/?page="

    #socket.setdefaulttimeout(300)
    start = 289
    end = 642
    split = ' - '
    path = "F:\Training\凯叔历史"
    download(start, end, lishi, split, path)
