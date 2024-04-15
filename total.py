#総合ランキングを取得する
import requests
from bs4 import BeautifulSoup
import csv
from japanmap import groups
from japanmap import pref_code

HEADER = ['rank_now', 'name', 'location', 'area']

#urlを取得して解析
url = "https://www.kankokeizai.com/100sen_36/"
html = requests.get(url) 
soup = BeautifulSoup(html.content, "html.parser")#

total_rank = soup.find_all("tr") #全てのtr要素を取得

with open('total_rank.csv', 'w', encoding='utf-8') as f:
    #csvファイルへの書き込み
    writer = csv.writer(f)
    writer.writerow(HEADER)
    group = ['北海道','東北','関東','中部','近畿','中国', '四国','九州'] #温泉の場所がどの地方か分けるための配列
    for infs in total_rank:  
        d = [inf for inf in infs.find_all("td")] #すべてのtd要素を取得し1つずつ配列に格納
        rank_now = d[0].text #ランキング
        rank_name = d[2].text #温泉の名前
        rank_loc = d[3].text #温泉の場所(県)
        num = pref_code(rank_loc) #場所(県)によって番号を振り分ける
        rank_area = '地方'
        for item in group:
            if(num in groups[item]):
                rank_area = item #場所によってどの地方か判別し代入

        row = [rank_now,  rank_name, rank_loc, rank_area]
        #ファイルへの書き込み
        writer.writerow(row)

