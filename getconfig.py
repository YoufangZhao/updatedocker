# _*_ coding=utf-8 _*_
import urllib
import urllib2

values = {"username":"163.com","password":""}
data = urllib.urlencode(values)
#url = "https://passport.csdn.net/account/login?ref=toolbar"
url = "https://passport.csdn.net/account/login"
geturl1 = url + "?"+data
print geturl1
#request1 = urllib2.Request("https://www.baidu.com")
#responese1 = urllib2.urlopen("https://www.baidu.com")
#response2 = urllib2.urlopen("http://www.cninfo.com.cn/eipo/index.jsp")
request = urllib2.Request(geturl1)
response = urllib2.urlopen(request)
print response.read()
