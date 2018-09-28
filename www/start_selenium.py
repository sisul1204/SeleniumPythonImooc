#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest


driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(2)
print(EC.title_contains("注册"))
email_element = driver.find_element_by_id('register_email')
driver.save_screenshot('E:/imooc.png')
code_element = driver.find_element_by_id('getcode_num')
print(code_element.location)#{'x':123,'y':345}
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
button = code_element.size['height']+top
im = Image.open('E:/imooc.png')
img = im.crop((left,top,right,button))
img.save('E:/imooc1.png')
img = im.resize((256,256),Image.ANTIALIAS)


r = ShowapiRequest("http://route.showapi.com/184-4","75939","734014a3cdd44a05be2ce47661ec7be9" )
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"E:/imooc1.png")
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
time.sleep(2)
driver.find_element_by_id('captcha_code').send_keys(text)
time.sleep(2)
driver.close()





