import requests
from lxml import html

import dotenv
import os
import datetime

# load the environment variables
dotenv.load_dotenv()

# year = int(os.getenv('YEAR', 2024))
# filename = os.getenv('FILENAME', "crawled-page-{year}.html").format(year=year)
filename = './crawled-page.html'
data = []

# check if the page exists
if not os.path.exists(filename):

    # fetch the page if it doesn't exist
    page = requests.get(os.getenv('URL'), verify=False)

    # save the page to a file
    with open(filename, 'w', encoding='UTF8') as f:
        f.write(page.text)

    page = page.text

else:
    # if the page exists, read it from the file
    with open(filename, 'r', encoding='UTF8') as f:
        page = f.read()

# parse the page to html
tree = html.fromstring(page)

# get the desired sections
tables = tree.xpath(os.getenv('TABLE_XPATH'))
tables = tables[3:18]

#get data in table
table_contents = [table.text_content() for table in tables]

#access data in table rows
for table in tables:
    # TODO: get other rows
    dog_row = table.xpath(os.getenv('DOG_ROW_XPATH'))
    for item in dog_row:
        # print(item)
        # print(str(item))
        dog_row_contents = item.xpath(os.getenv('ROW_DATA_XPATH'))
        for content in dog_row_contents:
            data = str(content.text_content()).strip()
            print(data)
            
#TODO: plot dog data

# print the rows
# row_num = 3
# for row in rows:
#     columns = row.xpath(os.getenv('COL_XPATH'))
#     columns = [column.text_content() for column in columns]
#     columns = [column.strip() for column in columns]
#     row_string = " ".join(columns).strip()

#     # skip empty rows
#     if row_string.strip() == "":
#         continue

#     row_num += 1

#     print(f'Row {row_num}: {row_string}')

#     month = int(columns[0])
#     day = int(columns[1])
            
#     for i in range(2, len(columns), 2):
#         if columns[i] != "":
#             # get the time in HHMM format
#             hour = columns[i][:2]
#             minute = columns[i][2:]

#             dt = datetime.datetime(year,month,day,int(hour),int(minute))
#             value = columns[i+1]
#             print(f'{dt} - {value}')            

