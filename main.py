#Application Detection Earthquake Indo BMKG
from realtime_detection import extract_data, view_data

if __name__ == "__main__":
    print("Aplikasi Utama")
    result = extract_data()
    view_data(result)
