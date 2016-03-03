# coding=UTF-8
import requests

# 尝试爬取手机端的内容
weibo = 'http://weibo.cn/'
# cookies = {'_T_WM':'03436a0abbb03345a25c3bbe4116b8f9', 'H5_INDEX':'3', 'H5_INDEX_TITLE':'%E5%BE%AE%E7%AC%91%E7%9A%84%E5%A5%BD%E5%90%A7', 'M_WEIBOCN_PARAMS':'uicode%3D20000173', 'SUB':'_2A2570SE8DeTxGedL41YU9i_JzD2IHXVZOk90rDV6PUJbrdBeLVDDkW1LHet7rsbiQJ_IBsvhaX0VZifTk0UJpg..','SUHB':'0S7TFVdcN4Vel_', 'SSOLoginState':'1456820588'}
cookies = {'T_WM':'03436a0abbb03345a25c3bbe4116b8f9', 'SUHB':'0k1TnIrIJUMxUc', 'gsid_CTandWM':'4uXGCpOz5EJ0NZUEtLVnS6Edr9d', 'SUB':'_2A2570-WlDeTxGedL41YU9i_JzD2IHXVZP4vtrDV6PUJbrdAKLUv6kW1LHetmRZA1-ZUU_RwJNK5owb7L8mN64g..'}
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}

# 这里查看一下get的请求的原型
# get_url = 'http://www.httpbin.org/get'
# r = requests.get(get_url, headers=headers, cookies=cookies)
# print r.content

r = requests.get(weibo, headers=headers, cookies=cookies)
print r.content
# r = requests.get(weibo)
# print r.text