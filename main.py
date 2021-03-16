import requests
import json
import time
import re

# config
# POST请求的目标URL
url1 = "https://jdsd.gzhu.edu.cn/coctl_gzhu/index_wx.php/"

headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
         "Content-Type": "application/x-www-form-urlencoded",
         'Connection': 'keep-alive',
         'Cache-Control': 'max-age=0',
         'Host': 'jdsd.gzhu.edu.cn',
         'Referer': 'https://servicewechat.com/wxb78a5743a9eed5bf/15/page-frame.html',
         }

# proxy1={'http' : 'http://127.0.0.1:8888', 'https' : 'https://127.0.0.1:8888',}

#需要抓包去查看自己账号对应的key是什么，建议抓手机微信端的key
user_key = 'CxCGyAJ7wqyJbZMB3hW7gk3MZ+yVXFQsgU7Ozrr44MNXIcDzAuTxSGZOSQEaoijZ'


#登录
def login():
    data1 = {
        "route": "get_config",
        "key": user_key,
    }

    data2 = {
        "route": "user_status",
        "key": user_key,
    }

    data3 = {
        "route": "user_info",
        "key": user_key,
    }
    data4 = {
        "route": "wxlogin",
        "userInfo":  {"js_code":"0211Ky00018BmL1cqd300LkZNU01Ky01"} ,
        "system_info" : {"albumAuthorized":"true","benchmarkLevel":-1,"bluetoothEnabled":"false","brand":"microsoft","cameraAuthorized":"true","fontSizeSetting":15,"language":"zh_CN","locationAuthorized":"true","locationEnabled":"true","microphoneAuthorized":"true","model":"microsoft","notificationAuthorized":"true","notificationSoundEnabled":"true","pixelRatio":1,"platform":"windows","power":100,"safeArea":{"bottom":692,"height":692,"left":0,"right":414,"top":0,"width":414},"screenHeight":736,"screenWidth":414,"statusBarHeight":20,"system":"Windows 10 x64","theme":"light","version":"7.0.9","wifiEnabled":"true","windowHeight":692,"windowWidth":414,"SDKVersion":"2.13.2","devicePixelRatio":1} ,
        "version" : "undefined"
    }

    request = requests.post(url1, headers=headers, data=data1, verify=False)
    print(request.json())
    time.sleep(0.5)
    request = requests.post(url1, headers=headers, data=data2, verify=False)
    print(request.json())
    request = requests.post(url1, headers=headers, data=data4, verify=False)
    print(request.json())



#每日签到
def checkin():
    data = {
        "route" : "signin",
        "key" : user_key,
    }
    request = requests.post(url1, headers=headers, data=data, verify=False)
    print(request.json())


#诗词鉴赏
def reading():
    for x in range(1,6):
        data4 = {
            "route" : "classic_time",
            "addtime" : "0",
            "type" : str(x),
            "key" : user_key,
        }

        data5 = {
            "route" : "classic_time",
            "addtime" : "4",
            "type" : str(x),
            "key" : user_key,
        }
        data6 = {
            "route" : "classic_time",
            "addtime" : "86",
            "type" : str(x),
            "key" : user_key,
        }

        #进入阅读
        request = requests.post(url1, headers = headers ,data =data4 , verify=False)
        request = requests.post(url1, headers = headers ,data =data5 , verify=False)
        request = requests.post(url1, headers = headers ,data =data6 , verify=False)


        print(request.status_code)
        print(request.json())
        print("第",x,"篇已经阅读完成")


# 以下为随机匹配的刷题
def battle():
    for x in range(0,15):
        match = '"status":1'
        data7 = {
            "route": "get_counterpart",
            "key": user_key,
            "counter": str(x),
            "find_type": "0",
        }

        request = requests.post(url1, headers=headers, data=data7, verify=False)
        print(request.status_code)
        print(request.json())
        r = json.loads(request.text)
        if(r['status'] == 1):
            gaming_key = r['question_bag']['gaming_key']
            print('gaming_key is : ',gaming_key)
            break
        time.sleep(1)


    for x in range (0,180):
        data8 = {
                "route": "ask_opponent_score",
                "key": user_key,
                "gaming_key": gaming_key,
        }
        print("现在是第",x,"秒")
        request = requests.post(url1, headers=headers, data=data8, verify=False)
        print(request.text)
        time.sleep(1)

#每日一练
def pratice():
    data = {
        "route": "train_list_get",
        "dfiff" : "0",
        "key": user_key,
    }

    request = requests.post(url1, headers=headers, data=data, verify=False)
    print(request.json())
    r = json.loads(request.text)
    train_id = r["re"]["train_id"]
    print("train_id is :",train_id)
    train_result = []
    for i in r["re"]["question_bag"]:
        train_result.append(i["num"])
    print ("train_result is :",train_result)
    train_result1 = r'[["{0}","1"],["{1}","1"],["{2}","1"],["{3}","1"],["{4}","1"]]'.format(train_result[0],train_result[1],train_result[2],train_result[3],train_result[4])
    print(train_result1)

    data1 = {
        "route": "train_finish",
        "train_result":  train_result1 ,
        "train_id" : train_id,
        "key": user_key,
    }
    request = requests.post(url1, headers=headers, data=data1, verify=False)
    print(request.json())


if __name__ == '__main__':
    #登录
    login()
    #签到
    # checkin()
    #每日阅读
    # reading()
    #每日一练
    # for i in range(0,3):
        # pratice()
    #随机匹配
    # battle()
