from bs4 import BeautifulSoup
import pickle
import sys
import csv
#  sys.setrecursionlimit(100000)

def cpi_table_to_list(html):
    """
    arg1: a object with readline method and html contents that got from national statistic site
    return: a list contents [[header], [content], ...]
    """
    print('Processing ')
    html = ''.join(html.readlines())

    # remove some useless tag that may inpact to parse with bs4
    html = '<table class="pxtable">' + html.split('<table class="pxtable">')[1]
    html = html.split('</blockquote>')[0]
    html = html.replace('\t', '').replace('\r', '').replace('\n', '')
    html_soup = BeautifulSoup(html)

    print('\tGrab header')
    header=[ s.string.strip() for s in html_soup.findAll('th', {'class':'headlast', 'colspan':'1'})]
    header.insert(0, 'year/month')

    # contents
    print('\tGrab contents')
    contents = []
    a = html_soup.find('td', {"class":"stub1"})
    while a.get('class') != ["footnote"]:
        row = []
        if a.get('class') == ["stub1"]:
            row.append(a.string.strip())
            a = a.findNext('td')
            while a.get('class') != ["stub1"]:
                if a.get('class') == ["footnote"]: break
                row.append(a.string.strip())
                a = a.findNext('td')
        contents.append(row)

    contents.insert(0, header)
    return contents

def main():
    table_dir = 'cpi_table_1981_2014M8/'
    table_fn = ['TW_CPI_1981to1991_utf8.html', 'TW_CPI_1992to2001_utf8.html', 'TW_CPI_2002to2014M8_utf8.html']
    #  table_fn = ['TW_CPI_1981to1991_utf8.html']
    cpi_table_html = [table_dir+fn for fn in table_fn]

    #html table to csv format
    for cpi_html in cpi_table_html:
        with open(cpi_html, 'r') as f:
            rows = cpi_table_to_list(f)

            csv_fn = cpi_html.replace('.html', '.csv')
            with open(csv_fn, 'w') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                [csv_writer.writerow(row) for row in rows]

        #  import IPython; IPython.embed()

if __name__ == '__main__':
    main()

