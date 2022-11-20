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

class Disaster:
    def __init__(self, url, description):
        self.description = description #"Latest Earthquake Data Based on BMKG"
        self.result = None
        self.url = url

    def view_description(self):
        print(self.description)

    def extract_data(self):
        pass

    def view_data(self):
        pass

    def run(self):
        self.extract_data()
        self.view_data()

class EarthQuakeIndo(Disaster):
    def __init__(self, url):
        super(EarthQuakeIndo, self).__init__(url, "Latest Earthquake Data Based on BMKG")

    def extract_data(self):

        try:
            content = requests.get(self.url)
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

            self.result = result
        else:
            return None


    def view_data(self):
        #print("Data Gempa Terakhir Berdasarkan BMKG")
        print(f"Tanggal {self.result['date']} Pada Jam {self.result['time']}")
        print(f"Dengan Kekuatan Gempa Sebesar {self.result['magnitudo']} magnitudo")
        print(f"Di Kedalaman {self.result['depth']}")
        print(f"Lokasi di {self.result['geo']['ls']} - {self.result['geo']['bt']}")
        print(f"{self.result['geo']['location']} {self.result['scale']}")


class FloodIndo(Disaster):
    def __init__(self, url):
        super(FloodIndo, self).__init__(url, "NOT YET IMPLEMENTED, but it should return last flood in Indonesia")

    def view_description(self):
        print(f"UNDER CONTSTRUCTION {self.description}")
    def extract_data(self):
        pass

    def view_data(self):
        pass


if __name__ == '__main__':
    disaster_EarthQuakeIndo = EarthQuakeIndo('https://www.bmkg.go.id/')
    #print(disaster_EarthQuakeIndo.description)
    disaster_EarthQuakeIndo.view_description()
    disaster_EarthQuakeIndo.run()

    disaster_FloodIndo = FloodIndo('NOT YET')
   # print(disaster_FloodIndo.description)
    disaster_FloodIndo.view_description()
    disaster_FloodIndo.run()

    list_disaster = [disaster_EarthQuakeIndo, disaster_FloodIndo]
    print("\nALl List Disaster")
    for Disaster in list_disaster:
        Disaster.view_description()


