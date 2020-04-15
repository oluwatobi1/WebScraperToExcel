import urllib.request
from bs4 import BeautifulSoup
import csv

def scrapetoexcel(url, outputfile = 'Outputfile.csv', dest_path = ''):
    
    '''
    Scrapes data from a webpage to a excelsheet/csv file
    
    requires internet connection!
    NOTE:
    Note this line table = soup('table', {"class":"wikitable sortable"}) is subjected to change according to the website format
    Use 'Inspect Element' on  the table element on browser and replace tag('table') or class("wikitable sortable") 
    if any is different
        
    features="html.parser" might throw error when running on a different system   
    
    url : full url containing the data
    outputfile : Str name of destination excel file "should end with '.csv'"
    dest_path : str Path link of destination folder
    '''
    
    #reads the web page
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), features="html.parser")
    #open a file/writer to store the tabular data
    if len(dest_path)>1:
        dest_path =dest_path+'\\'
    f = open(dest_path+outputfile, 'w', newline = '')
    writer = csv.writer(f)
    #Finds the tabular portion of the webpage using tags check docs 'NOTE'
    table = soup('table', {"class":"wikitable sortable"})[0].find_all('tr')
    cnt = len(table)
    for row in table:
        cols = row.findChildren(recursive = False)
        cols = [elem.text.strip() for elem in cols]
        writer.writerow(cols)
        print(cnt, ' Row(s) left')
        cnt-=1
    print("Successful")
        
        
        
scrapetoexcel(url = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Nigeria',
              outputfile='Data.csv',
              dest_path= r'C:\Users\HP\Desktop\Vs_Work\Reispar')

#for more info 
# https://www.youtube.com/watch?v=OF8X47olcpg
