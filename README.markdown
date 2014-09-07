Data
----
* [消費者物價商品性質分類指數月](http://ebas1.ebas.gov.tw/pxweb/Dialog/..%5CDialog%5Cvarval.asp?ma=PR0101A2M&ti=%AE%F8%B6O%AA%CC%AA%AB%BB%F9%B0%F2%A5%BB%A4%C0%C3%FE%BA[%B6%B5%A5%D8%B8s%AB%FC%BC%C6-%A4%EB&path=../PXfile/PriceStatistics/&lang=9&strList=L)
	* 1981 ~ now
	* only statistic value



* [物價統計月報](http://www.stat.gov.tw/lp.asp?CtNode=488&CtUnit=333&BaseDSD=7&mp=4)
	* 2007 ~ now
	* there are to provide the xls file.



* **cpi_table_1981_2014M8**
	* download table from [消費者物價商品性質分類指數月](http://ebas1.ebas.gov.tw/pxweb/Dialog/..%5CDialog%5Cvarval.asp?ma=PR0101A2M&ti=%AE%F8%B6O%AA%CC%AA%AB%BB%F9%B0%F2%A5%BB%A4%C0%C3%FE%BA[%B6%B5%A5%D8%B8s%AB%FC%BC%C6-%A4%EB&path=../PXfile/PriceStatistics/&lang=9&strList=L) manully and conver the charset from big5 to utf8 with iconv
		* iconv -f big5 -t utf8 -c <big5.html> -o <utf8.html>

Tools
-----

* cpi_table_parser.py - cpi_table_html to csv


TODO
----

* automatically fetch the national statistic from <http://ebas1.ebas.gov.tw/pxweb/Dialog/price.asp>
* cpi_table_html to json or cvs to json
* front-end



