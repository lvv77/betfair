#import requests
#import json


#from Miner import Archiver

#import threading


#url ='https://api.stocktwits.com/api/2/streams/symbol/AAPL.json'
#data = {'since' : '51840090'}
#data = {'limit' : '30'}
#resp = requests.get(url, data)
#out = json.loads(resp.content)

#stream = StockTwitsStream(json = out['messages'])
#print('test')


#import matplotlib.pyplot as plt
#import time
#import random
#from collections import deque
#import numpy as np


#a1 = deque([0]*100)
#ax = plt.axes(xlim=(0, 20), ylim=(0, 40))

#line, = plt.plot(a1)
#plt.ion()
#plt.ylim([0,40])
#plt.show()

#stream = StockTwitsStream()
#url ='https://api.stocktwits.com/api/2/streams/symbol/AAPL.json'
#resp = requests.get(url)
#out = json.loads(resp.content)
#stream.add_tweets(out['messages'])
#xml = stream.dum_to_xml()
#Archiver.save_xml_file(xml, './data/ST/', 'test.xml')

#stream =  StockTwitsStream(path = './data/ST/test.xml')
#stream.update('AAPL')
#Archiver.save_xml_file(stream.dum_to_xml(), './data/ST/', 'test.xml')
#for i in range(0,20):
    
#    resp = requests.get(url)
#    out = json.loads(resp.content)
#    a1.appendleft(stream.add_tweets(out))
#    datatoplot = a1.pop()
#    line.set_ydata(a1)
#    plt.draw()
#    print a1[0]
#    i += 1
#    time.sleep(60)
#    plt.pause(0.0001)   

#from Miner import MarketWatch

#MM = MarketWatch('AAPL', True, 8000, './data/',0,0)
#MM.start()
#time.sleep(20)
#print('still here')


#MarketWatch.monitor_spread('AAPL', True, 1, 1, './data/')

#import requests
#import time
#while True:
#    quotes = requests.get("http://download.finance.yahoo.com/d/quotes.csv?s=GOOG&e=.csv&f=nt1l1f6k3s7p2").text
#    print(quotes)
#    time.sleep(1)

#from Miner import TorControl

#def worker(num):
#    """thread worker function"""
#    tor = TorControl(num, num+1)
#    tor.start_tor()
#    tor.enable_proxy()
#    while True:
#        print 'Worker: %s' % num
#        tor.new_identity(True)
#    return

#threads = []
#for i in range(1,3):
#    t = threading.Thread(target=worker, args=(i*3000,))
#    threads.append(t)
#    t.start()





#import requests
#import requesocks

#from Miner import TorControl
#tor = TorControl(9150, 9151)
#tor.start_tor()
#session = requesocks.session()

#session.proxies = {
#    'http': 'socks5://127.0.0.1:9150',
#    'https': 'socks5://127.0.0.1:9150'
#}

#resp = requests.get('https://api.ipify.org?format=json', timeout=5)
#j = json.loads(resp.content)
#print('New IP: '+ j['ip'])

#resp = session.get('https://api.ipify.org?format=json', timeout=5)
#j = json.loads(resp.content)
#print('New IP: '+ j['ip'])

#Factor test
#-----------
#from factors import shortratio
#from network import torcontrol
from Factors import ShortRatio
from Network import TorControl
#with TorControl() as tor:
#    short = ShortRatio('AAPL', proxies = tor.get_proxies())
#print(short.value)

#Screening test
#---------------
#from DataSources import GoogleFinance
#print GoogleFinance.screen_stocks(0, 5)

#Short squeeze strategy test
#---------------------------
from ShortSqueeze import ShortSqueeze
#from Network import TorControl
#from DataSources import YahooFinance as yf
#with TorControl() as tor:
#    ShortSqueeze.get_initial_universe(tor.get_proxies())
#print 'done'

#ShortSqueeze.update_universe_prices()
#ShortSqueeze.update_universe_short_ratios()
from Utility import Logger
from colorama import Fore
#u.log("test", 0, True, Fore.GREEN, True)
#from Network import TorControl
#with TorControl() as tor:
#    for i in range(5):
#        tor.new_identity()
#        print(tor.get_current_ip())





#logger = logging.getLogger(__name__)
#logger.info('INFO')
#logger.error('ERROR')
#logger.debug('DEBUG')
#u.test()
#logger = Logger()
#logger.critical("Test", level=3, color=Fore.LIGHTRED_EX, b_separator=True)

#XML validation test
from Xml import XmlValidator, XmlTransform
xsd = './XML/Universe_sample.xsd'
xml = './XML/Universe_sample.xml'
xslt = './XML/Transform.xslt'

#validator = XmlValidator(xsd)
#test = validator.validate(xml)
#print(test)
#transform = XmlTransform(xslt)
#result = transform.transform(xml)
#print(result)

#Sreener test
from DataSources import Universe
test_screener = Universe(xml,xslt,xsd)
#with TorControl() as tor:
#    test_screener.screener.handler.screen_one_page(proxies=tor.get_proxies(), start_at=10)
#    pass
test_screener.screen_all(True, 20)