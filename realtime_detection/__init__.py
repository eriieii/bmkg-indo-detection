"""
Date : 16 November 2022
Time : 16:22:45 WIB
Magnitudo : 5.3
Depth : 26 km
Geo : 5.38 LS - 102.38 BT
Location : Pusat gempa berada di laut 12 km Tenggara Enggano
Scale : Dirasakan (Skala MMI): II Enggano
"""

def extract_data():
    result = dict()
    result['date'] = "16 November 2022"
    result['time'] = "16:22:45 WIB"
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