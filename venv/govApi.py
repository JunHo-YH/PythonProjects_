# from urllib2 import Request, urlopen
# from urllib import urlencode, quote_plus
#
# url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
# queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('numOfRows') : '10', quote_plus('pageNo') : '1', quote_plus('stationName') : '종로구', quote_plus('dataTerm') : 'DAILY', quote_plus('ver') : '1.3' })
#
# request = Request(url + queryParams)
# request.get_method = lambda: 'GET'
# response_body = urlopen(request).read()
# print response_body
#
#


import requests
from bs4 import BeautifulSoup
service_key = 'UztJsnDttd26Ql9Ab3%2B2LJpC2vdQ54cK6bvYPLcDmow4kZRQb0UFcjyWmyuXjcuoececMmVvTnZoE%2FzWwkF1RQ%3D%3D'
params = '&numOfRows=10&pageNo=1&stationName=강서구&dataTerm=DAILY'
open_api = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?ServiceKey=' + service_key + params

res = requests.get(open_api)
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.find_all('item')
for item in data:
    covalue = item.find('covalue')
    o3grade = item.find('o3grade')
    print(covalue, o3grade)
    print()