import os
import cv2
import re
import math
import numpy as np

from use_sqlite import sqlitefun
x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 扁率
class basicsfun():
    
    def checkFileGroup(filepaths):
        # 检查文件组是否存在
        for filepath in filepaths:
            if os.path.exists(filepath) == False:
                print(filepath)
                return False
        return True
    def rectContourPoint(posarr):
        # 计算四点最小外轮廓
        pos = cv2.boundingRect(posarr)
        return pos
    def posChangeCnt(posstr,k):
        # 普通的字符串pos装cnt型
        # k作为缩放系数
        poslist = re.findall('\d+',posstr)
        poscnt = np.array([[int(poslist[0])*k,int(poslist[1])*k],[int(poslist[2])*k,int(poslist[3])*k],[int(poslist[4])*k,int(poslist[5])*k],[int(poslist[6])*k,int(poslist[7])*k]])
        
        return poscnt
    def count_dirs_num(path):
        # 统计文件夹下文件夹数量
        count = 0
        for file in os.listdir(path): #file 表示的是文件名
            count = count+1
        return count
    def readIRpath_filename(ir_path):
        # 读取红外文件夹地址 返回所有红外文件地址
        ir_file_name_list = []
        if os.path.exists(ir_path):
            dir_fils = os.listdir(ir_path)
            print("红外数据文件夹存在")
            for file_name in dir_fils:
                file_gps = ir_path+"/"+file_name+"/"+"GPS"+file_name[-3:]+".txt"
                list_txtlist = open(file_gps)
                for list_txt in list_txtlist:
                    if list_txt.find("raw") >=0:
                        ir_filename = ir_path+"/"+file_name+"/"+list_txt[0:9]
                        ir_file_name_list.append(ir_filename)
        else:
            print("红外数据文件夹不存在")
        return ir_file_name_list
    
    def savaImagebinSqlite(projecttime, key, path):
        # 任意地址图片写入数据库
        print("向图片数据库写入:", key)
        fp = open(path, 'rb')
        image_bin = fp.read()
        sqlitefun.sqlite_create_panelimage(projecttime)
        sqlitefun.sqlite_insert_imagebin(projecttime, key, image_bin)  # 写入图片数据库

    def getGPSpos(inputxystr,inputgpsstr,inputposstr):

            # 测试
            # inputxystr = "1,1 2,1 2,2 2,1"
            # inputgpsstr = "2,2 4,2 4,4 4,2"
            # inputposstr = "1,1 2,1 2,2 2,1 3,4 6,8"
            inputxy = []
            inputgps = []
            inputpos = []
            inputxylist = inputxystr.split(" ")
            inputgpslist = inputgpsstr.split(" ")
            inputposlist = inputposstr.split(" ")

            for inputxyliststr in inputxylist:
                inputxy.append(inputxyliststr.split(","))

            for inputgpsliststr in inputgpslist:
                inputgps.append(inputgpsliststr.split(","))

            for inputposliststr in inputposlist:
                inputpos.append(inputposliststr.split(","))

            res = basicsfun.get_transform_mat(
                inputxy, inputgps, inputpos)  # 计算gps并获取返回值
            #ret = {'code': 1000, 'msg': None, 'result': res}
            return res
    
#计算GPS值
    def get_transform_mat(inputxy, inputgps,inputpos):
        # inputxy = [1 2 3 4]
        # inputgps = [2 4 6 8]
        # 计算gps到全景图坐标映射矩阵
        print("选中点xy",inputxy)
        print("选中点gps", inputgps)
        print("所有xy", inputpos)
        img_point = np.zeros((len(inputxy),2), np.float32)
        gps_point = np.zeros((len(inputgps),2), np.float32)
        

        for i in range(len(inputxy)):
            img_point[i][0] = float(inputxy[i][0])
            img_point[i][1] = float(inputxy[i][1])
        for i in range(len(inputgps)):
            gps_point[i][0] = float(inputgps[i][0])
            gps_point[i][1] = float(inputgps[i][1])

        transform_mat = cv2.findHomography(img_point,gps_point)[0]

        pts = np.float32(inputpos).reshape(-1, 1, 2)  # four corners
        dst = cv2.perspectiveTransform(pts, transform_mat)
        print("dst   ",dst)
        res = ""
        for dstlist in dst:
            res = res + str("%.8f" % dstlist[0][0]) + "," + str("%.8f" % dstlist[0][1]) + " "
        return res.strip()

    def wgs84togcj02(lng, lat):
        # """
        # WGS84转GCJ02(火星坐标系)
        # :param lng:WGS84坐标系的经度
        # :param lat:WGS84坐标系的纬度
        # :return:
        # """
        if basicsfun.out_of_china(lng, lat):  # 判断是否在国内
            return lng, lat
        dlat = basicsfun.transformlat(lng - 105.0, lat - 35.0)
        dlng = basicsfun.transformlng(lng - 105.0, lat - 35.0)
        radlat = lat / 180.0 * pi
        magic = math.sin(radlat)
        magic = 1 - ee * magic * magic
        sqrtmagic = math.sqrt(magic)
        dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
        dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
        mglat = lat + dlat
        mglng = lng + dlng
        #return [mglng, mglat]
        return [mglat, mglng]

    def out_of_china(lng, lat):
        # """
        # 判断是否在国内，不在国内不做偏移
        # :param lng:
        # :param lat:
        # :return:
        # """
        if lng < 72.004 or lng > 137.8347:
            return True
        if lat < 0.8293 or lat > 55.8271:
            return True
        return False

    def transformlat(lng, lat):
        ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
              0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
        ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
                math.sin(2.0 * lng * pi)) * 2.0 / 3.0
        ret += (20.0 * math.sin(lat * pi) + 40.0 *
                math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
        ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
                math.sin(lat * pi / 30.0)) * 2.0 / 3.0
        return ret

    def transformlng(lng, lat):
        ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
              0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
        ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
                math.sin(2.0 * lng * pi)) * 2.0 / 3.0
        ret += (20.0 * math.sin(lng * pi) + 40.0 *
                math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
        ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
                math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
        return ret
    def update_html(htmlName):
        if os.path.exists(htmlName):
            htmlf = open(htmlName, 'r', encoding="utf-8")
            htmlcont = htmlf.read()
            htmlcont = htmlcont.replace("https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.js", "js/leaflet.js")
            htmlcont = htmlcont.replace('https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js',
                                        'js/bootstrap.min.js')
            htmlcont = htmlcont.replace(
                'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js',
                'js/leaflet.awesome-markers.js')
            htmlcont = htmlcont.replace('https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.css', 'css/leaflet.css')
            htmlcont = htmlcont.replace('https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css', 'css')
            htmlcont = htmlcont.replace('https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css',
                                        'css/font-awesome.min.css')
            htmlcont = htmlcont.replace(
                'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css',
                'css/leaflet.awesome-markers.css')
            htmlcont = htmlcont.replace(
                'https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css',
                'css/leaflet.awesome.rotate.css')
            new_html = open(htmlName, 'w')
            new_html.write(htmlcont)
            new_html.close()
            htmlf.close()
            return True
        else:
            return False
            





