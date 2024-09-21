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
tables = tables[2:17]
# print('Total tables: ', len(tables))

#get data in table
table_contents = [table.text_content() for table in tables]

#global variables to hold data
year_data = []
dog_data = []

#access data in table rows
for table in tables:
    # TODO: get other animal rows
    dog_row = table.xpath(os.getenv('DOG_ROW_XPATH'))
    # dog_alt_row = table.xpath(os.getenv('DOG_ROW_ALT_XPATH'))
    
    # access each column in the dog rows
    for col in dog_row:
        dog_row_contents = col.xpath(os.getenv('ROW_DATA_XPATH'))

        #tables have varying structures so check for empty rows
        if not len(dog_row_contents) == 0:
            #get year data
            year_header = table.xpath(os.getenv('YEAR_XPATH'))
            for header in year_header:
                year_string = str(header.text_content())[:-5]
            year_data.append(year_string.removeprefix('Fiscal Year ')) 

            #get dog data
            for content in dog_row_contents:
                data = str(content.text_content()).strip()
                # print(data)
                if data == "Dogs":
                    continue
                elif '%' in data:
                    continue
                else:
                    dog_data.append(data)

#get the "Animals In" data from the row
dogs_in = []
for stat in range(0, len(dog_data), 3):
    dogs_in.append(dog_data[stat])

# create and show plot
fig, ax = plt.subplots()
data_len = len(year_data)
# remember to convert data from string to int
ax.plot([int(year_data[data]) for data in range(data_len)], [int(dogs_in[data]) for data in range(data_len)])
plt.show()


