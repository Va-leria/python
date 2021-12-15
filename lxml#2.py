#Скачиваем все изображения со страницы
import sys
from pathlib import Path
from urllib.parse import urljoin
import requests
from lxml import html

response = requests.get('https://www.theartstory.org/artist/rubens-peter-paul/')
parsed_body = html.fromstring(response.text)

# Парсим ссылки с картинками при помощи XPath
images = parsed_body.xpath('//img/@src')
if not images:
    sys.exit("images Not Found")

# Конвертирование всех относительных ссылок в абсолютные
images = [
    urljoin(response.url, url)
    for url in images
]
print('Found {} images'.format(len(images)))

# Скачиваем только первые 10
for url in images[0:10]:
    r = requests.get(url)
    target = Path(
        'E:/devops/задания для лекций/python/downloaded_images/{}'.format(
            url.split('/')[-1]  # file name from URL
        )
    )
    target.write_bytes(r.content)

