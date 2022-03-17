from selenium import webdriver
from selenium.webdriver.common.proxy import ProxyType, Proxy
from colorama import *

with open('proxy.txt') as f:
    proxy_ip = f.readlines()

count = 0
for line in proxy_ip:
    count += 1
    proxy_ip = line

    proxy =Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = proxy_ip
    proxy.ssl_proxy = proxy_ip

    capabilities = webdriver.DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)

    driver = webdriver.Chrome('C:/chromedriver.exe', desired_capabilities=capabilities)

    try:
        driver.get('https://www.tiktok.com/signup/phone-or-email/email')
        print('\r', end="")
        print(Fore.WHITE + "Proxy:", proxy_ip, " - valid - Code [0]")
        driver.close()
        print(Fore.YELLOW + 'Loading...', end="")

    except:
        print('\r', end="")
        print("Proxy:", proxy_ip, " - invalid - Code [1]")
        driver.close()
        print(Fore.YELLOW + 'Loading...', end="")


