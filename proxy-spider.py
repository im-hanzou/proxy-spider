from time import sleep
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from colorama import *

print(Fore.RED+'''
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗    ███████╗██████╗ ██╗██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ███████╗██████╔╝██║██║  ██║█████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ╚════██║██╔═══╝ ██║██║  ██║██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ███████║██║     ██║██████╔╝███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
Credits to: https://github/xtekky                                                                                         
''')

print('Starting Spider')
sleep(2)

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = wd.Chrome('C:/chromedriver.exe', options=chrome_options)
wait = WebDriverWait(driver, 15)

ip_list = []
port_list = []

class Proxy_selector:
    global proxy_list
    driver.get('https://free-proxy-list.net/')
    ip_list = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//td[@class='hx' and text()='yes']/../td[1]")))]
    port_list =  [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//td[@class='hx' and text()='yes']/../td[2]")))]

    full_proxy = [item for sublist in zip(ip_list, port_list) for item in sublist]
    proxy_list = [ ':'.join(x) for x in zip(full_proxy[0::2], full_proxy[1::2]) ]
    print(Fore.WHITE+'Https Proxies: ', proxy_list)



for i in proxy_list:
    proxy_ip_port = i

    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = proxy_ip_port
    proxy.ssl_proxy = proxy_ip_port
    capabilities = webdriver.DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome('C:/chromedriver.exe', desired_capabilities=capabilities, options=chrome_options)
    driver.set_page_load_timeout(10)

    try:
        driver.get('https://www.tiktok.com/signup/phone-or-email/email')
        print('\r', end="")
        print(Fore.WHITE+"Proxy:", proxy_ip_port, " - valid - Code [0]")
        driver.close()
        print(Fore.YELLOW+'Loading...', end="")

    except:
        print('\r', end="")
        print("Proxy:", proxy_ip_port, " - invalid - Code [1]")
        driver.close()
        print(Fore.YELLOW+'Loading...', end="")

if __name__ == "__main__":
    Proxy_selector()

