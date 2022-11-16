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
        date = soup.find('span', {'class': 'waktu'})
        time = date.text.split(', ')[1]

        # print(soup.prettify())


    result = dict()
    result['date'] = date.text.split(', ')[0] #"16 November 2022"
    result['time'] = time #"16:22:45 WIB"
    result['magnitudo'] = "5.3"
    result['depth'] = "26 km"
    result['geo'] = {
        'ls' : 5.38,
        'bt' : 102.38,
        'location' : "Pusat gempa berada di laut 12 km Tenggara Enggano",
    }
    result['scale'] = "Dirasakan (Skala MMI): II Enggano"

    return result


def view_data(result):
    print("Data Gempa Terakhir Berdasarkan BMKG")
    print(f"Tanggal {result['date']} Pada Jam {result['time']}")
    print(f"Dengan Kekuatan Gempa Sebesar {result['magnitudo']} magnitudo")
    print(f"Di Kedalaman {result['depth']}")
    print(f"Lokasi di {result['geo']['ls']} Lintang Selatan - {result['geo']['bt']} Bujur Timur")
    print(f"{result['geo']['location']} {result['scale']}")