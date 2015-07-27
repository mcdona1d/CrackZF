crackzf
=======
首先测试将正方教务的`/default2.aspx`后缀改为`/default_ysdx.aspx`能否访问，并且网址中没有hash字符串，可使用此程序

此程序依赖`BeautifulSoup4`和`pycurl`

## 使用方法:


将`jw_url = ""`修改为`你的教务ip`

使用字典生成器生成字典，替换`dict.txt`


`python pwtest.py 学号`

例如

`python pwtest.py 12111001`

