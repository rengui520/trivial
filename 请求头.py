
from fake_useragent import UserAgent

for i in range(10):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    print(headers)
	
'''


#甚至你可以制定生产某种浏览器的请求头
from fake_useragent import UserAgent
ua = UserAgent()
# ie user agent
print(ua.ie)
# opera user agent
print(ua.opera)
# chrome user agent
print(ua.chrome)
# firefox user agent
print(ua.firefox)
# safri user agent
print(ua.safari)
'''