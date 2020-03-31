import json


import requests

print("初始化内容")
developer_user = "libra@zklf.com"
developer_pass = "fu110110110"
url = "http://ai.zklf-tech.com"
# self.url = "http://127.0.0.1:8000"
auth = ""
class RequestsPost():

    def getToken():
        # 获取身份秘钥
        print("api 测试 获取身份秘钥")
        api = "/api/v1/auth/"
        from_data = {'developer_user': developer_user , 'developer_pass': developer_pass}
        r_json = requests.post(url+api,from_data)
        print("获取到的身份秘钥 原始json",r_json.text)
        r_dict = json.loads(r_json.text)
        token = r_dict["result"]["token"]
        
        return token
    def plant_chain_init(plant_id,token):
        #print("api 测试 初始化电站区块信息")
        #token = RequestsPost.getToken()
        api = "/api/v1/plant_chain_init/"
        from_data = {"token":token,'developer_user': developer_user , 'developer_pass': developer_pass,"plant_id":plant_id}
        r_json = requests.post(url+api,from_data)
        #print("初始化电站区块信息 原始json",r_json.text)
        r_dict = json.loads(r_json.text)
        result = r_dict["result"]
        
        return result
    def plant_chain_tabel_all_select(token):
        print("api 查询  全部电站区块表信息")
        #token = RequestsPost.getToken()
        api = "/api/v1/plant_chain_tabel_all_select/"
        from_data = {"token":token,'developer_user': developer_user , 'developer_pass': developer_pass}
        r_json = requests.post(url+api,from_data)
        print("全部电站区块表信息 原始json",r_json.text)
        r_dict = json.loads(r_json.text)
        result = r_dict["result"]
        
        return result
    def plant_chain_info_select(table_name,token):
        print("api 查询  某一个区块详细信息")
        #token = RequestsPost.getToken()
        api = "/api/v1/plant_chain_info_select/"
        from_data = {"token":token,'developer_user': developer_user , 'developer_pass': developer_pass,"table_name":table_name}
        r_json = requests.post(url+api,from_data)
        print("某一个区块详细信息 原始json",r_json.text)
        r_dict = json.loads(r_json.text)
        result = r_dict["result"]
        return result
    
    def plant_chain_add_info(token,plant_id,chain_hand_id,chain_tail_id,chain_type,chain_num,creat_id,json_data):
        print("api 增加  某一个区块详细信息")
        #token = RequestsPost.getToken()
        api = "/api/v1/plant_chain_add_info/"
        from_data = {"token":token,'developer_user': developer_user , 'developer_pass': developer_pass}
        from_data.update({"plant_id":plant_id})
        from_data.update({"chain_hand_id":chain_hand_id})
        from_data.update({"chain_tail_id":chain_tail_id})
        from_data.update({"chain_type":chain_type})
        from_data.update({"chain_num":chain_num})
        from_data.update({"creat_id":creat_id})
        from_data.update({"json_data":json_data})
        r_json = requests.post(url+api,from_data)
        print("增加  某一个区块详细信息 原始json",r_json.text)
        r_dict = json.loads(r_json.text)
        result = r_dict["result"]
        return result

    #上传图片到MongoDB
    def image_upload(imageFile,token):
        api = "/api/v1/upload_mongodb_image/"
        from_data = {"token": token, 'developer_user': developer_user, 'developer_pass': developer_pass}
        from_data.update({'imageFile': imageFile})
        r_json = requests.post(url+api,from_data)
        print("image返回数据",r_json.text)
        r_dict = json.loads(r_json.text)
        result = r_dict["result"]
        return result


        

