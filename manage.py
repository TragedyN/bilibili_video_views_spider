import browser_driver as bd
from ip_pool.get_proxies import ProxiesSpider

count = 1
while True:
    bd.loop_ip_play()
    if count % 100 == 0:
        ProxiesSpider().run()
    count +=1
