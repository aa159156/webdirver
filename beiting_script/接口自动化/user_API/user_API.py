#coding=utf-8
import requests
import json

errorNessage = "Success"
def login(url,username,password):
    """用户登录"""
    url = url+"/apiv1/web/user/login"
    print("接口："+url)
    header = {
        "Authorization": "",
        "Content-Type": "application/json"
    }
    data = {
                "mobilePhone":username,
                "password":password
           }
    data = json.dumps(data)
    request = requests.post(url=url,data=data,headers=header)
    response = json.dumps(request.json(), ensure_ascii=False, indent=4)
    token = json.loads(response)["data"]["token"]
    user_id = json.loads(response)["data"]["id"]
    print(response)
    if errorNessage in response:
        print("状态码：",request.status_code,"接口请求成功")
    else:
        print("状态码：",request.status_code,"接口请求失败")
        raise
    return user_id,token

def findOne(url,header,user_id):
    """根据认证用户ID查看认证用户信息"""
    url = url+"/apiv1/web/user/findOne"
    print("接口："+url)
    data = {
                "id":user_id
           }
    request = requests.get(url=url,params=data,headers=header)
    response = json.dumps(request.json(), ensure_ascii=False, indent=4)
    errorNessage = "Success"
    print(response)
    if errorNessage in response:
        print("状态码：",request.status_code,"接口请求成功")
    else:
        print("状态码：",request.status_code,"接口请求失败")
        raise

def modify(url,header,user_id,name,IdCard,phone,organization):
    """根据认证用户ID修改认证用户信息"""
    url = url + "/apiv1/web/user/modify"
    print("接口："+url)
    data = {
                "id": user_id,
                "realName": name,
                "idCard": IdCard,
                "mobilePhone": phone,
                "organization": organization
            }
    data = json.dumps(data)
    request = requests.post(url=url,data=data,headers=header)
    response = json.dumps(request.json(), ensure_ascii=False, indent=4)
    print()
    errorNessage = "Success"
    print(response)
    if errorNessage in response:
        print("状态码：", request.status_code, "接口请求成功")
    else:
        print("状态码：", request.status_code, "接口请求失败")
        raise

def findAll(url,header,page,pagesize):
    """分页查询所有认证用户信息"""
    url = url + "/apiv1/web/user/findAll"
    print("接口："+url)
    data = {
                "page": page,
                "pageSize":pagesize
           }
    request = requests.get(url=url, params=data, headers=header)
    response = json.dumps(request.json(), ensure_ascii=False, indent=4)
    errorNessage = "Success"
    print(response)
    if errorNessage in response:
        print("状态码：", request.status_code, "接口请求成功")
    else:
        print("状态码：", request.status_code, "接口请求失败")
        raise

def addIdentity(url,header,user_id,type,houseid,roomnumber):
    """新增认证用户身份"""
    url = url + "/apiv1/web/user/addIdentity"
    print("接口："+url)
    data = {
                "id": user_id,
                "roleType": type,
                "houseId": houseid,
                "roomNumber": roomnumber,
            }
    data = json.dumps(data)
    request = requests.post(url=url,data=data,headers=header)
    response = json.dumps(request.json(), ensure_ascii=False, indent=4)
    errorNessage = "Success"
    print(response)
    if errorNessage in response:
        print("状态码：", request.status_code, "接口请求成功")
    else:
        print("状态码：", request.status_code, "接口请求失败")
        raise

def deleteIdentity(url,header,user_id,type,houseid,roomnumber):
    """删除认证用户身份"""
    url = url + "/apiv1/web/user/deleteIdentity"
    print("接口："+url)
    data = {
                "id": user_id,
                "roleType": type,
                "houseId": houseid,
                "roomNumber": roomnumber,
            }
    data = json.dumps(data)
    request = requests.post(url=url,data=data,headers=header)
    response = json.dumps(request.json(), ensure_ascii=False, indent=4)
    errorNessage = "Success"
    print(response)
    if errorNessage in response:
        print("状态码：", request.status_code, "接口请求成功")
    else:
        print("状态码：", request.status_code, "接口请求失败")
        raise

def search(url,header,searchvalue,page,pagesize):
    """根据手机号或姓名模糊查询认证用户信息，分页显示"""
    url = url + "/apiv1/web/user/search"
    print("接口："+url)
    data = {
                "searchValue":searchvalue,
                "page": page,
                "pageSize":pagesize
           }
    request = requests.get(url=url, params=data, headers=header)
    response = json.dumps(request.json(), ensure_ascii=False, indent=4)
    errorNessage = "Success"
    print(response)
    if errorNessage in response:
        print("状态码：", request.status_code, "接口请求成功")
    else:
        print("状态码：", request.status_code, "接口请求失败")
        raise





if __name__ == "__main__":
    url = "https://beiting.haituke.com"
    token = login(url,18925662425,12345678)
    print(token[0])
    header = {
        "Authorization": "Bearer "+token[1],
        "Content-Type": "application/json;charset=UTF-8"
    }
    # Select_Attestation_User(url,header,user_id=token[0])
    Modify_Attestation_User(url, header, 41,"", "", "", "")




