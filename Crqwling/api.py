import requests
# from bs4 import BeautifulSoup
import openpyxl
client_id = 'PZWP3KbKm6_wRS1QHXXF'
clinent_secret = 'cxf4vrogt4'

start, num = 1, 0

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].width = 100
excel_sheet.column_dimensions['C'].width = 100
excel_sheet.append(['랭킹', '제목', '링크'])



for index in range(10):
    start_number = start + (index * 100)
    naver_open_api = 'https://openapi.naver.com/v1/search/news.json?query=갤럭시 S21&display=100&start=' + str(start_number)
    header_params = {"X-Naver-Client-id": client_id, "X-Naver-Client-Secret": clinent_secret}
    res = requests.get(naver_open_api, headers=header_params)
    if res.status_code == 200:
        data = res.json()
        for item in data['items']:
           num += 1
           title = item['title'].replace('<b>', '').replace('</b>', '')
           excel_sheet.append([num, title, item['link']])
    else:
        print("Error Code", res.status_code)


excel_file.save('Crawling.xlsx')
excel_file.close()
print('엑셀처리 완료')