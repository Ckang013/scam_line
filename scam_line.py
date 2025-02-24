"""
    反詐騙資料- 詐騙line id
"""

import requests
import json

def get_LineID():
    url = "https://od.moi.gov.tw/api/v1/rest/datastore/A01010000C-001277-053"
    payload = {}
    headers = {
    'Cookie': 'JSESSIONID=6A30578A174A6F7BBDA336C7DD6064B4'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text
    data = json.loads(data) # 將 str 類型轉換成 dict 類型
    records = data['result']['records']
    lines = []
    for record in records[:10]:
        line = record['帳號']
        lines.append(line)
    return lines

def main():
    url = "https://od.moi.gov.tw/api/v1/rest/datastore/A01010000C-001277-053"

    payload = {}
    headers = {
    'Cookie': 'JSESSIONID=6A30578A174A6F7BBDA336C7DD6064B4'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.text

        data = json.loads(data) # 將 str 類型轉換成 dict 類型
        
        # 取得資料的 'records' 鍵裡面的資料
        records = data['result']['records']
        print(f"資料筆數: {len(records)}")

        # 取出line id的部分
        lines = []
        for record in records[:100]:
            line = record['帳號']
            lines.append(line)
        print(lines)
            

    else:   
        print(f"API 請求失敗，狀態碼: {response.status_code}")

if __name__ == "__main__":
    main()
