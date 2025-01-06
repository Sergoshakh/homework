import requests
from PIL import Image, ImageFilter
import time
from io import BytesIO

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
    response = requests.get(planes[i])
    a = Image.open(BytesIO(response.content))
    a.thumbnail((1200, 800))
    img.append(a)
    b = a.convert("L")
    img_L.append(b)
    img_gray_smooth = img_L[i].filter(ImageFilter.SMOOTH)
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
