"""
Date : 16 November 2022
Time : 16:22:45 WIB
Magnitudo : 5.3
Depth : 26 km
Geo : 5.38 LS - 102.38 BT
Location : Pusat gempa berada di laut 12 km Tenggara Enggano
Scale : Dirasakan (Skala MMI): II Enggano
"""
from bs4 import BeautifulSoup
import requests

def extract_data():

    try:
        content = requests.get('https://www.bmkg.go.id/')
        content.status_code

    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        date = result[0]
        time = result[1]


        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')

        i = 0
        for res in result:
            #print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                depth = res.text
            elif i == 3:
                geo = res.text.split(' - ')
                ls = geo[0]
                bt = geo[1]
            elif i == 4:
                location = res.text
            elif i == 5:
                scale = res.text
            i = i + 1


    result = dict()
    result['date'] = date #"16 November 2022"
    result['time'] = time #"16:22:45 WIB"
    result['magnitudo'] = magnitudo #"5.3"
    result['depth'] = depth #"26 km"
    result['geo'] = {
        'ls' : ls,
        'bt' : bt,
        'location' : location,
    }
    result['scale'] = scale

    return result


def view_data(result):
    print("Data Gempa Terakhir Berdasarkan BMKG")
    print(f"Tanggal {result['date']} Pada Jam {result['time']}")
    print(f"Dengan Kekuatan Gempa Sebesar {result['magnitudo']} magnitudo")
    print(f"Di Kedalaman {result['depth']}")
    print(f"Lokasi di {result['geo']['ls']} - {result['geo']['bt']}")
    print(f"{result['geo']['location']} {result['scale']}")