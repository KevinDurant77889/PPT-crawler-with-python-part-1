
import urllib.request
import re

req = urllib.request.urlopen("https://disp.cc/b/62-brN5")
temp = req.read().decode()
target = re.findall("http://i.imgur.com/\w\w\w\w\w\w\w.jpg", temp)
target = list(set(target))


image_num = 1
for element in target:
    image_req = urllib.request.urlopen(element)
    image = image_req.read()
    with open("howhow_" + str(image_num) + '.jpg', 'wb') as file:
        file.write(image)
    image_num+=1
