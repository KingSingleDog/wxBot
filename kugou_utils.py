import json
import requests

def get_search_tips(keyword,music_tip_count=5,mv_tip_count=2,album_count=2):
    url="http://searchtip.kugou.com/getSearchTip?MusicTipCount="+str(music_tip_count)+"&MVTipCount="+str(mv_tip_count)+"&albumcount="+str(album_count)+"&keyword="+str(keyword)
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"}
    html = requests.get(url, header)
    html.encoding = "UTF-8"
    search_return = json.loads(html.content)
    return search_return

def search_music(keyword,page=1,pagesize=30,tag="em"):
    url="http://songsearch.kugou.com/song_search_v2?keyword="+str(keyword)+"&page="+str(page)+"&pagesize="+str(pagesize)+"&userid=-1&clientver=&platform=WebFilter&tag="+str(tag)+"&filter=2&iscorrection=1&privilege_filter=0"
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"}
    html=requests.get(url,header)
    html.encoding="UTF-8"
    search_return=json.loads(html.content)
    return search_return

def search_mv(keyword,page=1,pagesize=30,tag="em"):
    url="http://mvsearch.kugou.com/mv_search?keyword="+str(keyword)+"&page="+str(page)+"&pagesize="+str(pagesize)+"&userid=-1&clientver=&platform=WebFilter&tag="+str(tag)+"&filter=2&iscorrection=1&privilege_filter=0&_=1521349524548"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"}
    html = requests.get(url, header)
    html.encoding = "UTF-8"
    search_return = json.loads(html.content)
    return search_return

def get_music_details(hash):
    url="http://www.kugou.com/yy/index.php?r=play/getdata&hash="+str(hash)+"&album_id=8132457&_=1521349321428"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"}
    html=requests.get(url,header)
    html.encoding="UTF-8"
    details_return=json.loads(html.content)
    return details_return