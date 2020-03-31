import sqlite3 as sqlite3  # 支持大于1G的blob
import os



locapath=os.path.dirname(os.path.realpath(__file__))   #表示当前所处的文件夹的绝对路径 
locasql = sqlite3.connect(locapath+"/data/database.db",check_same_thread=False)
cur_locasql = locasql.cursor()




class sqlitefun():
    def sqlite_select_config(key):
        # 查询配置信息
        sql = '''select value from soft_config where key = '%s';'''%key
        cur_locasql.execute(sql)
        res = cur_locasql.fetchall()
        return res
    def sqlite_select_config_all():
        sql = 'select key from soft_config'
        cur_locasql.execute(sql)
        res = cur_locasql.fetchall()
        return res
    def sqlite_insert_config(key,value):
        # 给config key value
        # 先删除 后 重新插入
        sql = '''DELETE FROM soft_config WHERE key = '%s';'''%key
        cur_locasql.execute(sql)
        locasql.commit()

        sql = '''insert into soft_config (key,value) 
        values (:st_key,:st_value)'''
        cur_locasql.execute(sql,{'st_key':key,'st_value':value})
        locasql.commit()
    def sqlite_create_config():
        # 创建软件信息key value表
        sql = '''CREATE TABLE IF NOT EXISTS soft_config(key TEXT UNIQUE,value TEXT)'''
        cur_locasql.execute(sql)
        locasql.commit()

    #已使用模板
    def sql_create_use_template():
        sql = '''CREATE TABLE IF NOT EXISTS use_template(model_name TEXT UNIQUE,use_project_id TEXT)'''
        cur_locasql.execute(sql)
        locasql.commit()
    #添加已使用模板
    def sqlite_insert_use_template(model_name,project_time):
        sql = '''insert or ignore into use_template (model_name,use_project_id) values (:st_model,:project_id)'''
        cur_locasql.execute(sql, {'st_model': model_name,'project_id':project_time})
        locasql.commit()
    #查询已使用模板
    def sqlite_select_use_template(model_name):
        sql = '''select use_project_id from use_template where model_name = '%s';''' % model_name
        cur_locasql.execute(sql)
        res = cur_locasql.fetchall()
        return res

    def sqlite_select_all_use_template():
        sql = '''select * from use_template'''
        cur_locasql.execute(sql)
        res = cur_locasql.fetchall()
        return res
    #修改已使用模板
    def sqlite_update_use_template(model_name,project_time):
        sql = '''update use_template set use_project_id = :st_project_id 
                       where model_name = :st_model'''
        cur_locasql.execute(sql, {'st_project_id': project_time, 'st_model': model_name})
        locasql.commit()


    #创建模板表
    def sqlite_create_template():
        sql = '''CREATE TABLE IF NOT EXISTS soft_template(key TEXT UNIQUE,value TEXT)'''
        cur_locasql.execute(sql)
        locasql.commit()
    #插入信息
    def sqlite_insert_template(key,value):
        # 给config key value
        # 先删除 后 重新插入
        sql = '''DELETE FROM soft_template WHERE key = '%s';'''%key
        cur_locasql.execute(sql)
        locasql.commit()

        sql = '''insert into soft_template (key,value) 
        values (:st_key,:st_value)'''
        cur_locasql.execute(sql,{'st_key':key,'st_value':value})
        locasql.commit()
    #修改单个模板
    def sqlite_update_template(key,value):
        sql = '''update soft_template set value = :st_value 
               where key = :st_key'''
        cur_locasql.execute(sql, {'st_key': key, 'st_value': value})
        locasql.commit()
    #查询全部模板信息
    def sqlite_select_template_all():
        sql = 'select key from soft_template'
        cur_locasql.execute(sql)
        res = cur_locasql.fetchall()
        return res
    #查询单个模板信息
    def sqlite_select_template(key):
        # 查询配置信息
        sql = '''select value from soft_template where key = '%s';'''%key
        cur_locasql.execute(sql)
        res = cur_locasql.fetchall()
        return res

    def sqlite_delete_template(key):
        sql = '''DELETE FROM soft_template WHERE key = '%s';''' % key
        cur_locasql.execute(sql)
        locasql.commit()

    def sqlite_create_panelimage(projecttime):
        # 创建项目面板图片缓存信息
        sql = '''CREATE TABLE IF NOT EXISTS image_'''+projecttime+'''
        (panelid TEXT UNIQUE,image LONGBLOB)'''
        cur_locasql.execute(sql)
        locasql.commit()
    def sqlite_create_panelinfo(projecttime):
        #  创建项目面板信息缓存表
        sql = '''CREATE TABLE IF NOT EXISTS panelinfo_'''+projecttime+''' 
        (panelid TEXT UNIQUE,panelinfo TEXT)'''
        cur_locasql.execute(sql)
        locasql.commit()
    
    def sqlite_init_execute():
        # 初始化表单
        sql = '''CREATE TABLE IF NOT EXISTS projectinfo 
        (id integer primary key,projecttime TEXT,projectname TEXT)'''
        cur_locasql.execute(sql)
        locasql.commit()

    def sqlite_create_projecttime(arg1,arg2):
        # 插入项目基本信息
        sql = '''insert into projectinfo (projecttime,projectname) values (:st_projecttime,:st_projectname)'''
        cur_locasql.execute(sql,{'st_projecttime':arg1,'st_projectname':arg2})
        locasql.commit()

    def sqlite_select_panelinfolist(projecttime):
        # 查询历史打开报告的面板记录表
        sql = "SELECT * FROM panelinfo_"+projecttime+" ;"
        cur_locasql.execute(sql)
        res = cur_locasql.fetchall()
        return res

    def sqlite_delete_panelinfo(projecttime):
        sql ="DELETE FROM projectinfo where projecttime='"+projecttime+"'"
        print(sql)
        cur_locasql.execute(sql)
        sql = "DROP TABLE image_"+projecttime
        cur_locasql.execute(sql)
        sql = "DROP TABLE panelinfo_"+projecttime
        cur_locasql.execute(sql)
        locasql.commit()

    
    def sqlite_vacuum_clean():
        print("清空图片缓存")
        print("释放物理存储空间")
        sql = "VACUUM"
        cur_locasql.execute(sql)
        locasql.commit()
        print("释放物理存储空间 完成") 
    
    def sqlite_insert_imagebin(projecttime,key,image):
        # 图片加入数据库
        # insert or replace 图片添加的时候如果相同则覆盖
        # insert or ignore 相同则忽略
        sql = '''insert or replace into image_'''+projecttime+''' (panelid,image) 
        values (:st_panelid,:st_image)'''
        cur_locasql.execute(sql,{'st_panelid':key,'st_image':image})
        locasql.commit()
    
    def sqlite_insert_panelinfo_json(projecttime,index,info_json):
        # 图片加入数据库
        # insert or replace 图片添加的时候如果相同则覆盖
        # insert or ignore 相同则忽略
        sql = '''insert or replace into panelinfo_'''+projecttime+''' (panelid,panelinfo) 
        values (:st_panelid,:st_panelinfo)'''
        cur_locasql.execute(sql,{'st_panelid':index,'st_panelinfo':info_json})
        locasql.commit()
    def sqlite_update_panelinfo_json(projecttime,index,info_json):
        sql= '''update panelinfo_'''+projecttime+''' set panelinfo = :st_panelinfo 
        where panelid = :st_panelid'''
        cur_locasql.execute(sql, {'st_panelid': index, 'st_panelinfo': info_json})
        locasql.commit()
    def sqlite_insert_panelinfo_all_json(projecttime,info_json_list):
        # 图片加入数据库
        # insert or replace 图片添加的时候如果相同则覆盖
        # insert or ignore 相同则忽略
        for panel_info_json in info_json_list:
            index = panel_info_json [0]
            info_json = panel_info_json [1]
            sql = '''insert or replace into panelinfo_'''+projecttime+''' (panelid,panelinfo) 
            values (:st_panelid,:st_panelinfo)'''
            cur_locasql.execute(sql,{'st_panelid':index,'st_panelinfo':info_json})
        locasql.commit()
    def sqlite_update_panelinfo_all_json(projecttime,info_json_list):
        for panel_info_json in info_json_list:
            index = panel_info_json [0]
            info_json = panel_info_json [1]
            sql = '''update panelinfo_''' + projecttime + ''' set panelinfo = :st_panelinfo 
                    where panelid = :st_panelid'''
            cur_locasql.execute(sql,{'st_panelid':index,'st_panelinfo':info_json})
        locasql.commit()
    #删除
    def sqlit_delete_panelinfo_json(projecttime,panelid):
        sql = '''delete from panelinfo_'''+projecttime+''' where panelid='%s';'''%panelid
        cur_locasql.execute(sql)
        locasql.commit()
    
    def sqlite_select_imagebin(projecttime,key):
        # 图片查询
        sql = '''select image from image_'''+projecttime +''' where panelid = '%s';'''%key
        cur_locasql.execute(sql)
        res = cur_locasql.fetchall()
        return res
    
    def sqlite_select_localist():
        # 查询本数据库源的列表
        sql = '''select projecttime,projectname from projectinfo'''
        cur_locasql.execute(sql)
        res = cur_locasql.fetchall()
        return res

    
        
        
        
        

                

            
        
    
    
        