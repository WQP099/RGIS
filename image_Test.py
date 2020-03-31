import base64
import requests
import json

print("初始化内容")
developer_user = "libra@zklf.com"
developer_pass = "fu110110110"
url = "http://ai.zklf-tech.com"
# self.url = "http://127.0.0.1:8000"
auth = ""
def image_name():
    token = getToken()
    # 获取图片
    panoramic_bin = sqlitefun.sqlite_select_imagebin(select_project_time, "panoramic")[0][0]
    image_byte_list = []
    image_name_list = []
    #图片分割
    for i in range(len(panoramic_bin)):
        lens = i + 10240
        if lens > len(panoramic_bin):
            lens = len(panoramic_bin) - 1
        bst = panoramic_bin[i:lens]
        icon_byte = base64.b64encode(bst)
        icon_str = icon_byte.decode('ascii')
        print("bst  ", bst)
        image_name = image_upload(icon_str, token)
        print(image_name)
        image_name_list.append(image_name)
        # image_byte_list.append()
        i = lens
#上传图片到MongoDB
def image_upload(imageFile,token):
    api = "/api/v1/upload_mongodb_image/"
    from_data = {"token": token, 'developer_user': developer_user, 'developer_pass': developer_pass}
    from_data.update({'imageFile': imageFile})
    r_json = requests.post(url+api,from_data)
    print("image返回数据",r_json.text)
    r_dict = json.loads(r_json.text)
    print("r_dict",r_dict.text())
    result = r_dict["result"]
    return result
def getToken():
    # 获取身份秘钥
    print("api 测试 获取身份秘钥")
    api = "/api/v1/auth/"
    from_data = {'developer_user': developer_user , 'developer_pass': developer_pass}
    r_json = requests.post(url+api,from_data)
    print("获取到的身份秘钥 原始json",r_json.text)
    r_dict = json.loads(r_json.text)
    token = r_dict["result"]["token"]