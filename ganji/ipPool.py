import requests
from lxml import etree
import codecs
import time
def get_url(url):
	url_list=[]
	for i in range(1,2):
		url_new=url+'/'+str(i)
		url_list.append(url_new)
	return url_list
def get_content(url):
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
	headers = {'User-Agent': user_agent}
	r=requests.get(url,headers=headers)
	content=r.text
	return content.encode('utf-8')
def get_info(content):
	selector=etree.HTML(content)
	#data_ip=selector.xpath('//*[@id="nav_btn01"]/div[6]/table/tbody/tr/td[1]/text()')
	#data_port=selector.xpath('//*[@id="nav_btn01"]/div[6]/table/tbody/tr/td[2]/text()')
	data_ip=selector.xpath("//div[@id='body']/table/tr/td[2]/text()")
	data_port=selector.xpath("//div[@id='body']/table/tr/td[3]/text()")
	with codecs.open('data.txt','a') as f:
		for i in range(len(data_ip)):
			out=u''
			out+=u"" + data_ip[i]
			out+=u":" + data_port[i]
			f.write(out + u"\n")
def verify(ip,port):
	user_agent ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
	headers = {'User-Agent':user_agent}
    
	url_test='https://www.baidu.com'
	proxies = {'http':'http://%s:%s'%(ip,port)}
	print(proxies)
	r=requests.get(url_test,proxies=proxies)
	content=r.text
	time.sleep(3)

	try:
		if r.status_code==200:
			print('that is ok')
			with codecs.open('data3.txt','a') as f:
				out='"ipaddr":'+ip + u":" + port
				#out='"ipaddr":'+'"{}:{}"'.format(ip,port)
				f.write(out)
		else:
			print('that is not ok')
	except requests.HTTPError as e:
	    print(e.reason)
if __name__ == '__main__':
	
	url = 'http://www.xicidaili.com/nn'
	url_list = get_url(url)
	for i in url_list:
		print(i)
		content = get_content(i)
		time.sleep(3)
		get_info(content)
		
	with open("data.txt", "r") as f:
		datas = f.readlines()
		for data in datas:
			print(data.split(u":")[0])
        # print('%d : %d'%(out[0],out[1]))
			verify(data.split(u":")[0],data.split(u":")[1])
    	


