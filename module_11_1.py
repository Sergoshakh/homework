import requests
from PIL import Image, ImageFilter
from io import BytesIO
import time

print()
print(' ******** пример использования библиотеки REQUESTS ********')

wthr_url = "https://api.open-meteo.com/v1/forecast"
#wthr_url = "https://api.open-meteo.com/v2/forecast"    # для проверки на ошибку

params = {"latitude": 56.004, "longitude": 37.848,
          "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum,sunrise,sunset,wind_speed_10m_max,wind_gusts_10m_max",
          "timezone": "Europe/Moscow"}
response = requests.get(wthr_url, params=params)
if response.status_code == 200:
    data = response.json()
    tomorrow_temp_min = data['daily']['temperature_2m_min'][1]
    tomorrow_temp_max = data['daily']['temperature_2m_max'][1]
    tomorrow_precipitation = data['daily']['precipitation_sum'][1]
    tomorrow_sunrise = data['daily']['sunrise'][1]
    tomorrow_sunset = data['daily']['sunset'][1]
    tomorrow_wind_speed_10m_max = data['daily']['wind_speed_10m_max'][1]
    tomorrow_wind_gusts_10m_max = data['daily']['wind_gusts_10m_max'][1]

    string_time = str(tomorrow_sunrise)
    string_sunrise = string_time[-5:]
    string_time = str(tomorrow_sunset)
    string_sunset = string_time[-5:]

    print()
    print(f"   Прогноз погоды в Пушкино на завтра:")
    print(f"Минимальная температура: {tomorrow_temp_min}°C")
    print(f"Максимальная температура: {tomorrow_temp_max}°C")
    print(f"Ожидаемое количество осадков: {tomorrow_precipitation} мм")
    print(f"Восход солнца: {string_sunrise}")
    print(f"Заход солнца: {string_sunset}")
    print(f'Скорость ветра: {round(tomorrow_wind_speed_10m_max * 1000 / 3600, 1)} м/с')
    print(f'Порывы ветра до: {round(tomorrow_wind_gusts_10m_max * 1000 / 3600, 1)} м/с')
else:
    print(f"Ошибка - {response.status_code}: {response.text}")
print()
input(' ...для продолжения нажмите ENTER')

print()
print('***********************************')
print('All data from API:')
print(data)
print('***********************************')
print()
print(' - Данные с сайта "open-meteo.com" в текстовом формате: ')
print()
input(' ...для продолжения нажмите ENTER')
print()
r = requests.get('https://open-meteo.com/')
print(r.text)

print()
print()
print(' ******** далее пример использования библиотек PILLOW и REQUESTS ********')
input(' ...для продолжения нажмите ENTER')

planes = ['https://kartinki.pics/uploads/posts/2022-03/1647052498_31-kartinkin-net-p-samolet-krasivie-kartinki-38.jpg',
'https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/VQ-BEI_%286919052100%29.jpg/1200px-VQ-BEI_%286919052100%29.jpg',
'https://kartinki.pics/uploads/posts/2021-07/1625242269_30-kartinkin-com-p-fon-aeroport-krasivie-foni-34.jpg',
'https://kartinki.pics/uploads/posts/2022-12/1670538620_21-kartinkin-net-p-krasivie-kartinki-samoletov-v-nebe-krasivo-21.jpg',
'https://kartinki.pics/uploads/posts/2022-12/1670538605_24-kartinkin-net-p-krasivie-kartinki-samoletov-v-nebe-krasivo-24.jpg']

img = []                 # список оригинальных картинок
img_L = []               # ниже - списки модифицированных картинок
img_emboss = []
img_edges_smooth = []

for i in range(len(planes)):
    response = requests.get(planes[i])              # запрос на получение картинки по URL
    a = Image.open(BytesIO(response.content))
    a.thumbnail((1200, 800))                        # ограничиваем картинки по размеру
    img.append(a)
    b = a.convert("L")                              # переводим их в оттенки серого
    img_L.append(b)
    img_gray_smooth = img_L[i].filter(ImageFilter.SMOOTH)    # фильтры...
    c = img_gray_smooth.filter(ImageFilter.EMBOSS)
    img_emboss.append(c)
    img_gray_smooth = img_L[i].filter(ImageFilter.SMOOTH)
    d = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
    img_edges_smooth.append(d)
    print(f'обработана пара картинок №{i+1} из 5')

print()
print('Картинки будут открываться по 5 штук штатным средством операционной системы с шагом в 1,5 сек.')
print('в порядке: ОРИГИНАЛЬНЫЕ, ВЫПУКЛЫЕ, ИНВЕРСИВНЫЕ_ТРАФАРЕТЫ')
input(' ...для продолжения нажмите ENTER')

for i in range(len(planes)):
    img[i].show()
    time.sleep(1.5)

for i in range(len(planes)):
    img_emboss[i].show()
    time.sleep(1.5)

for i in range(len(planes)):
    img_edges_smooth[i].show()
    time.sleep(1.5)
