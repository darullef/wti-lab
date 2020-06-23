import time
import requests


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/'
    my_record = {"userID": 68, "movieID": 9123, "rating": 4.5, "genre-Action": 0, "genre-Adventure": 0,
                 "genre-Animation": 0, "genre-Children": 1, "genre-Comedy": 1, "genre-Crime": 0,
                 "genre-Documentary": 0, "genre-Drama": 0,"genre-Fantasy": 0, "genre-Film-Noir": 0,
                 "genre-Horror": 0, "genre-IMAX": 0, "genre-Musical": 1, "genre-Mystery": 0,
                 "genre-Romance": 1, "genre-Sci-Fi": 0, "genre-Short": 0, "genre-Thriller": 1,
                 "genre-War": 0, "genre-Western": 0}
    requests_list = []
    y1 = requests.get(url + 'ratings')
    requests_list.append(y1)
    time.sleep(0.01)
    y2 = requests.get(url + 'ratings/all')
    requests_list.append(y2)
    time.sleep(0.01)
    y3 = requests.get(url + 'ratings/68')
    requests_list.append(y3)
    time.sleep(0.01)
    x = requests.post(url + 'rating', data=my_record)
    requests_list.append(x)
    time.sleep(0.01)
    y2 = requests.get(url + 'ratings/all')
    requests_list.append(y2)
    time.sleep(0.01)
    y3 = requests.get(url + 'ratings/68')
    requests_list.append(y3)
    time.sleep(0.01)
    for i in requests_list:
        print("request url: " + str(i.url))
        print("request status_code: " + str(i.status_code))
        print("request headers: " + str(i.headers))
        print("request text: " + str(i.text))
        print("request request.headers: " + str(i.request.headers))
        print('-------------------------------------------------')
        print('-------------------------------------------------')