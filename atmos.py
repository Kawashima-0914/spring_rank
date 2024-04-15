#温泉の雰囲気のランキング
#仕様はtotal.pyと同じ

import requests
from bs4 import BeautifulSoup
import csv
from japanmap import groups
from japanmap import pref_code

HEADER = ['rank_now', 'name', 'location', 'area']

#urlを取得して解析
url = "https://www.kankokeizai.com/100sen_36/atmosphere/"
html = requests.get(url) 
soup = BeautifulSoup(html.content, "html.parser")#

total_rank = soup.find_all("tr")

with open('atmos_rank.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    group = ['北海道','東北','関東','中部','近畿','中国', '四国','九州']
    for infs in total_rank:  
        d = [inf for inf in infs.find_all("td")]
        rank_now = d[0].text
        rank_name = d[2].text
        rank_loc = d[3].text
        num = pref_code(rank_loc)
        rank_area = '地方'
        for item in group:
            if(num in groups[item]):
                rank_area = item

        row = [rank_now,  rank_name, rank_loc, rank_area]

        writer.writerow(row)

