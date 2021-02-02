import requests
import openpyxl
from bs4 import BeautifulSoup


def write_excel_template(filename, sheetname, listdata):
    # Workbook()으로 엑셀 파일 생성
    excel_file = openpyxl.Workbook()
    # 엑셀 파일이 생성되면 디폴트 쉬트가 생성되며, 엑셀파일변수.active 로 해당 쉬트를 선택할 수 있음
    excel_sheet = excel_file.active
    #dolumn_dimensions['열'] : 해당 열 너비 설정
    excel_sheet.column_dimensions['A'].width = 100
    excel_sheet.column_dimensions['B'].width = 30

    if sheetname != '':
        excel_sheet.title = sheetname

    for item in listdata:
        excel_sheet.append(item)
    excel_file.save(filename) # 저장
    excel_file.close() # 종료

product_lists = list()

for page_num in range(10): # 여러 페이지 크롤링하기
    if page_num == 0:
        res = requests.get("https://davelee-fun.github.io/")
    else:
        res = requests.get("https://davelee-fun.github.io/page" + str(page_num + 1)) # 페이지 수
    soup = BeautifulSoup(res.content, 'html.parser')

    data = soup.select('div.card')
    for item in data:
        product_name = item.select_one('div.card-body h4.card-text')
        product_data = item.select_one('div.wrapfooter span.post-date')
        product_info = [product_name.string.strip(), product_data.string]
        product_lists.append(product_info)

write_excel_template('tmp.xlsx', '상품정보', product_lists)
