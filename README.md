crackzf
=======
首先测试将正方教务的/default2.aspx后缀改为/default_ysdx.aspx能否访问，并且网址中没有hash字符串，可使用此程序

#此程序依赖BeautifulSoup4和pycurl

使用方法:


将jw_url = ""修改为你的教务ip

使用字典生成器生成字典，替换dict.txt


python pwtest.py 学号

例如

python pwtest 12111001

