import requests
from lxml import html

import dotenv
import os
import datetime
import matplotlib.pyplot as plt

from scraping_utils import get_url, parse

# load the environment variables
dotenv.load_dotenv()

filename = './crawled-page.html'
data = []

# get page
page = get_url(os.getenv('URL'), filename)

# parse the page to html
tree = parse(page, 'html')

# get tables from the desired sections
tables = tree.xpath(os.getenv('TABLE_XPATH'))
tables = tables[3:18]

#get data in table
table_contents = [table.text_content() for table in tables]

#global variables to hold data
dog_data = []

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
            if data == "Dogs":
                continue
            else:
                dog_data.append(data)
            print(data)
            
#TODO: plot dog data
print(dog_data)
#create plot
fig, ax = plt.subplots()
plt.show()

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

