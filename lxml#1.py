#знакомство с модулем lxml (part #1)
import requests
from lxml import html

response = requests.get('http://ya.ru')
parsed_body = html.fromstring(response.text)

print(parsed_body.xpath('//title/text()')[0])  
print(parsed_body.xpath('//a/@href'))  
