import sys
import datetime
import os
import operator
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QMenu,QLineEdit,QMessageBox
from PyQt5.QtCore import pyqtSignal,Qt,QRectF,QPoint,QPointF

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import   QPainter ,QPixmap,QPen,QColor
from PyQt5.QtWidgets import (QGraphicsItem, QGraphicsObject,QGraphicsScene, QGraphicsView)
from PyQt5.QtWidgets import QListWidgetItem, QCheckBox
import json


from use_sqlite import sqlitefun
from basicsfunction import basicsfun

from UI.Ui_RGISMainActivity import Ui_RGISMain  # 使用vscode生成的调用方法
from UI.Ui_create_project import Ui_creatProject 
from UI.Ui_open_project import Ui_open_project
from UI.Ui_set_panel_info import Ui_setPanelInfo
from UI.Ui_num_dialog import Ui_numDialog
from UI.Ui_row_column_dialog import  Ui_row_Column_Dialog
from UI.Ui_update_panel_info import Ui_Upadte_Panel_info
from UI.Update_Number_Row_rc import Ui_Update_number_Dialog


class MyRGISMain(QMainWindow,Ui_RGISMain):
    signalMousePos = pyqtSignal(list,list,int)

    def __init__(self,parent = None):
        super(MyRGISMain, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("RGIS-地理信息标注系统v0001-20191219")
        self.rownum = 2 #单行标注点击次数
        self.row_column = 4 #多行点击次数
        self.rowvalue1=[] #单行第一次点击的点
        self.rowvalue2=[] #单行第二次点击的点
        self.rowcolumn = [[0,0],[0,0],[0,0],[0,0]] #多行第一次点击的点
        # self.rowcolumn2 = [] #多行第二次点击的点
        # self.rowcolumn3 = [] #多行第三次点击的点
        # self.rowcolumn4 = [] #多行第四次点击的点
        self.movemode = 0 # 0表示固定 1 表示移动
        self.MapImage.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.cb_label_mode.addItems(["查看","单点标注","单行标注","多行标注"])
        self.bool_getpanel_wh = 0  # 获取组件长宽

        self.panel_info_all_list = []  # 原始信息列表 保持和数据库中的一直
        self.panel_info_dictlist = []  # 面板全部信息  用列表字典保存
        self.general_panel_showlist = []  # 一般显示列表  通常全部组件是一种颜色 用绿色表示
        self.clicked_panel_showlist = [] # 选中组件显示列表  一般表示多个或者一个选中的显示 颜色用红色表示


        self.bool_region_move_panel = 0 #用于控制是否允许移动组件
        self.bool_updage_number = 0

        self.selectItem = []
        #初始化三个显示颜色面板
        self.redboxlist = []
        self.greenboxlist = []
        self.blueboxlist = []
        self.pos_check = []


        self.action_create_project.triggered.connect(self.create_project) # 创建GIS项目
        self.action_history_project.triggered.connect(self.history_project) # 打开历史项目

        self.but_zoomout.clicked.connect(self.MapimageZoonOut) # 放大按钮
        self.but_zoomin.clicked.connect(self.MapimageZoonIn) # 缩小按钮
        self.but_rest.clicked.connect(self.MapimageZoonRest)  # 刷新按钮
        self.but_movemode.clicked.connect(self.changeMoveMode) # 改变点击模式 切换拖动和点击
        self.but_getpanel_wh.clicked.connect(self.getpanel_wh) # 获取组件宽高
        self.but_setpanel_info.clicked.connect(self.setpanelInfo) # 设置组件信息


        self.listPanelID.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listPanelID.customContextMenuRequested.connect(self.select_right_menu)#绑定列表
        #self.listPanelID.itemDoubleClicked.connect(self.updateItem)  # 设置条目点击事件
        self.listPanelID.itemClicked.connect(self.select_panel_item)  # 条目单点事件

        self.btn_move_no.setVisible(False)
        self.btn_move_ok.setVisible(False)
        self.btn_move_ok.clicked.connect(self.start_fun_ok)#确定开始功能事件
        self.btn_move_no.clicked.connect(self.end_fun_no)#取消功能事件
        self.btn_move_panel.clicked.connect(self.region_loc_alter)#多面板位置改动

        self.btn_update_number.clicked.connect(self.update_number)#重新编号




        # win_Num_Dialog = Num_Dialog(self)
        # win_Num_Dialog.show()
    #修改条目
    def update_number(self):
        print("item  重新编号")
        if self.cb_label_mode.currentText() == "查看":

            if self.bool_region_move_panel ==0:
                #self.bool_region_move_panel=1 #设置为1的时候  允许移动组件
                #self.MapImage.setDragMode(QGraphicsView.RubberBandDrag) #设置为可以拉框
                self.btn_move_panel.setEnabled(False) #设置为不可点击
                self.bool_updage_number = 1

                # for box in self.general_panel_showlist:
                #     box.bool_IsMovable = 1
                #     box.setFlag(QGraphicsItem.ItemIsMovable,True)
        else:
            QMessageBox.information(self, "消息", "请将操作状态改为查看才可选择要重新编号的组件", QMessageBox.Yes)
        # number_value = self.listPanelID.currentItem().text()
        # print(number_value)
        # self.update_dialog = Update_Number_dialog(self)
        # self.update_dialog.setT(number_value,self.listPanelID.currentItem())
        # self.update_dialog.Update_Number_dialog_Signal.connect(self.getDialogSignal)
        # self.update_dialog.show()
    #list单点事件
    def select_panel_item(self):
        print("点击事件")
        number_value = self.listPanelID.currentItem().text()
        for panel_item_info in self.panel_info_all_list:
            panel_info_dict = json.loads(panel_item_info[1])  # 转为字典

            if number_value == panel_info_dict["panel_name"]:
                for box in self.general_panel_showlist:
                    if box.key in panel_item_info[0]:
                        box.setSelected(True)
                    else:
                        box.setSelected(False)

    def select_right_menu(self,pos):
        number_Item = self.listPanelID.currentItem()
        for panel_item_info in self.panel_info_all_list:
            panel_info_dict = json.loads(panel_item_info[1])  # 转为字典

            if number_Item.text() == panel_info_dict["panel_name"]:
                for box in self.general_panel_showlist:
                    if box.key in panel_item_info[0]:
                        box.setSelected(True)
                    else:
                        box.setSelected(False)
        print("右键点击",number_Item.text())
        menu = QMenu()
        opt1 = menu.addAction("修改信息")
        opt2 = menu.addAction("删除")
        action = menu.exec_(QtGui.QCursor.pos())
        if action == opt1:
            print("修改信息")
        if action == opt2:
            print("删除")
            #delItem = self.listPanelID.selectedItems()
            # if delItem:
            #     panel_id = str(delItem[0].text()).split(" ")[0]
            # else:
            #     print("没有选中面板 删除失败")
            reply = QMessageBox.question(self,"删除提示","你确定要删除编号["+number_Item.text()+"]面板?",QMessageBox.Yes|QMessageBox.No)
            if reply == QMessageBox.Yes:
                print("删除当前面板")
                for panelinfo in self.panel_info_all_list:
                    panel_info_dict = json.loads(panelinfo[1])  # 转为字典
                    if number_Item.text() == panel_info_dict["panel_name"]:
                        panelId = panelinfo[0]
                        sqlitefun.sqlit_delete_panelinfo_json(self.projecttime, panelId)
                        self.panel_info_all_list.remove(panelinfo)
                        self.getlSignal_refresh([0,panelId])


    def keyPressEvent(self, event):
        # 键盘监听
        if event.key() == QtCore.Qt.Key_P:
            self.MapimageZoonOut()
            
        if event.key() == QtCore.Qt.Key_O:
            self.MapimageZoonIn()
          
        if event.key() == QtCore.Qt.Key_I:
            self.MapimageZoonRest()

        if event.key() == QtCore.Qt.Key_F:
            self.changeMoveMode()
        
        if event.key() == QtCore.Qt.Key_G:
            self.getpanel_wh()

        if event.key() == QtCore.Qt.Key_H:
            self.setpanelInfo()
        if event.key() == QtCore.Qt.Key_M:
            #设置组件移动
            self.region_loc_alter()
        if event.key() == QtCore.Qt.Key_Escape:
            #取消组件移动
            self.end_fun_no()
        
        
        
    def numDialog(self,type):
        if(type == 0 ):
            win_Num_Dialog = NumDialog(self)
            win_Num_Dialog.NumDialog_Signal.connect(self.getNumvalue)
            win_Num_Dialog.show()
        if(type == 1):
            win_Row_Column_Dialog = Row_Column_Dialog(self)
            win_Row_Column_Dialog.Row_Column_Dialog_Signal.connect(self.getNumvalue)
            win_Row_Column_Dialog.show()

    def setpanelInfo(self):
        win_SetPanelInfo = SetPanelInfo(self)
        win_SetPanelInfo.show()

    def getpanel_wh(self):
        print("获取组件宽高")
        self.bool_getpanel_wh = 1 


    def create_project(self):
        print("创建标注项目")
        win_CreateProject = CreateProject(self)
        win_CreateProject.createproject_Signal.connect(self.getDialogSignal)
        win_CreateProject.show()
    
    def history_project(self):
        print("打开标注项目")
        win_OpenProject = OpenProject(self)
        win_OpenProject.OpenProject_Signal.connect(self.getDialogSignal)
        win_OpenProject.show()
    
    def getDialogSignal(self, lists):
        print("主界面收到各种信号",lists)
        #修改编号
        if lists[0] == "Update_Number_dialog":
            number_value = lists[1]
            selectItem_x = self.selectItem[0]
            selectItem_y = self.selectItem[1]
            update_item_lists = []
            print("编号格式",number_value)
            print("选中面板X值",selectItem_x)
            print("选中面板Y值",selectItem_y)
            #获取Y值相差不大于一个组件高的范围值，获取同行数据将颜色标记为黄色
            for panel_item_info in self.panel_info_all_list:
                panel_info_dict = json.loads(panel_item_info[1])  # 转为字典
                panel_pos_y = int(panel_info_dict["panel_pos"].split(',')[1])
                panel_pos_x = int(panel_info_dict["panel_pos"].split(',')[0])
                panel_h = int(panel_info_dict["panel_wh"].split(',')[1])
                if abs(int(selectItem_y-panel_pos_y))<int(panel_h/2):
                    print("同一行的ID",panel_item_info[0])
                    for box in self.general_panel_showlist:
                        if panel_item_info[0] == box.key:
                            box.setSelected(True)
                            item_info = [box.key,panel_pos_x]
                            update_item_lists.append(item_info)
            update_item_lists.sort(key=operator.itemgetter(1))
            for update_item in update_item_lists:
                print("qqqqqqqqqqqq",update_item[1])
                #进行重新编号 并保存到数据库中
            #new update_list = sorted(update_item_lists,key=lambda x:update_item_lists[])

        #修改面板信息
        elif lists[0] == "Update_Panel_info":
            #修改内容
            number_value = lists[1]
            listItem = lists[2]
            itemvalue = listItem.text()
            isItem = False;
            listcount = self.listPanelID.count()
            selectIndex = self.listPanelID.row(listItem)
            self.panel_info_all_list = sqlitefun.sqlite_select_panelinfolist(self.projecttime)  # 获取全部组件列表信息
            if number_value != itemvalue:
                for i in range(listcount):
                    if number_value == self.listPanelID.item(i).text():
                        isItem = True;
                        break;
                    else:
                        isItem = False;
                if isItem:
                    QMessageBox.information(self,"消息","编号已存在，请重新输入",QMessageBox.Yes | QMessageBox.No)
                else:
                    select_panel_info = self.panel_info_all_list[selectIndex]
                    panel_info_dict = json.loads(select_panel_info[1])  # 转为字典
                    panel_info_dict["panel_name"] = number_value
                    panel_info_json = json.dumps(panel_info_dict, ensure_ascii=False)
                    sqlitefun.sqlite_insert_panelinfo_json(self.projecttime, panel_info_dict["panel_index"], panel_info_json)
                    listItem.setText(number_value)
                    self.update_dialog.close()
            else:
                self.update_dialog.close()

        else:
            self.projecttime = lists[1]  # 获取当前打开项目的索引值
            self.lab_projectName.setText(lists[1]+" / "+lists[2])
            sqlitefun.sqlite_create_panelinfo(self.projecttime)
            print("调试 看一下字典信息对不对",self.panel_info_dictlist)
            if lists[0] == "CreateProject":
                panoramic_bin = sqlitefun.sqlite_select_imagebin(lists[1],"panoramic")[0][0]
                self.showPanoramic(panoramic_bin)

            if lists[0] == "OpenProject":
                panoramic_bin = sqlitefun.sqlite_select_imagebin(lists[1],"panoramic")[0][0]
                self.showPanoramic(panoramic_bin)

    def getNumvalue(self,list):

        if list[0] == "NumDialog": #单行标注
            self.numValue = int(list[1])
            rowvalue1_x = int(self.rowvalue1[0])
            rowvalue2_x = int(self.rowvalue2[0])
            rowvalue1_y = int(self.rowvalue1[1])
            rowvalue2_y = int(self.rowvalue2[1])

            value_x = (abs(rowvalue2_x-rowvalue1_x))/(self.numValue)
            value_y = (abs(rowvalue2_y-rowvalue1_y))/(self.numValue-1)
            num= int(list[1]) -2
            index = 0
            panel_pos_int_w = int(self.panel_wh_text.split(",")[0])
            panel_pos_int_h = int(self.panel_wh_text.split(",")[1])
            while index < num:
                index+=1
                if(int(value_x)>5 and int(value_y)<5):
                    #横向
                    if(rowvalue1_x < rowvalue2_x):
                        map_x = (rowvalue1_x + (value_x+panel_pos_int_w/int(list[1]))* index);
                        map_y = rowvalue1_y - (value_y*index)
                    else:
                        map_x = (rowvalue2_x + (value_x + panel_pos_int_w / int(list[1])) * index);
                        map_y = rowvalue2_y - (value_y*index)
                if(int(value_x)<5 and int(value_y)>5):
                    #竖向
                    if (rowvalue1_y < rowvalue2_y):
                        map_x = rowvalue1_x + (value_x * index)
                        map_y = (rowvalue1_y + (value_y * index));
                    else:
                        map_x = rowvalue2_x + (value_x * index)
                        map_y = (rowvalue2_y + (value_y * index));
                if(int(value_x)>5 and int(value_y)>5):
                    #斜
                    if(rowvalue1_x < rowvalue2_x) and (rowvalue1_y< rowvalue2_y):
                        map_x = (rowvalue1_x + (value_x + panel_pos_int_w / int(list[1])) * index);
                        map_y = (rowvalue1_y + (value_y * index));
                        print("1")
                    elif (rowvalue1_x > rowvalue2_x) and (rowvalue1_y < rowvalue2_y):
                        map_x = (rowvalue1_x - (value_x + panel_pos_int_w / int(list[1])) * index);
                        map_y = (rowvalue1_y + (value_y * index));
                        print("2")
                    elif (rowvalue1_x < rowvalue2_x) and (rowvalue1_y > rowvalue2_y):
                        map_x = (rowvalue2_x - (value_x + panel_pos_int_w / int(list[1])) * index);
                        map_y = (rowvalue2_y + (value_y * index));
                        print("3")
                    elif (rowvalue1_x > rowvalue2_x) and (rowvalue1_y > rowvalue2_y):
                        map_x = (rowvalue2_x + (value_x + panel_pos_int_w / int(list[1])) * index);
                        map_y = (rowvalue2_y + (value_y * index));
                        print("4")

                arg1 = [map_x, map_y]
                self.add_panel_info(arg1)
        if list[0] == "Row_Column_Dialog": #多行标注
            Columnvalue = int(list[1])
            rowValue = int(list[2])
            row_column1 = self.rowcolumn[0]
            row_column2 = self.rowcolumn[1]
            row_column3 = self.rowcolumn[2]
            row_column4 = self.rowcolumn[3]
            value1_x = (abs(row_column4[0] - row_column1[0])) / Columnvalue
            value1_y = (abs(row_column4[1] - row_column1[1])) / (Columnvalue - 1)
            value2_x = (abs(row_column3[0] - row_column2[0])) / Columnvalue
            value2_y = (abs(row_column3[1] - row_column2[1])) / (Columnvalue - 1)
            column_num = Columnvalue - 2 #列
            row_num = rowValue -2 #行
            column_arr1 = []
            column_arr2 = []
            panel_pos_int_w = int(self.panel_wh_text.split(",")[0])
            column_arr1.append(row_column1)
            column_arr1.append(row_column4)
            column_arr2.append(row_column2)
            column_arr2.append(row_column3)
            index = 0
            while index < column_num:
                index+=1
                if (int(value1_x) < 5 and int(value1_y) > 5):
                    #竖向
                    if (row_column1[1] < row_column4[1]):
                        map_x_1 = row_column1[0] + (value1_x * index)
                        map_y_1 = row_column1[1] + (value1_y * index)
                    else:
                        map_x_1 = row_column4[0] + (value1_x * index)
                        map_y_1 = row_column4[1] + (value1_y * index)
                elif (int(value1_x) > 5 and int(value1_y) > 5):
                    #斜方向
                    # 斜方向
                    coordinate1_x = row_column1[0]
                    coordinate2_x = row_column4[0]
                    coordinate1_y = row_column1[1]
                    coordinate2_y = row_column4[1]
                    if (coordinate1_x < coordinate2_x) and (coordinate1_y < coordinate2_y):
                        map_x_1 = (coordinate1_x + (value1_x + panel_pos_int_w / rowValue) * index);
                        map_y_1 = (coordinate2_y + (value1_y * index));
                        print("1")
                    elif (coordinate1_x > coordinate2_x) and (coordinate1_y < coordinate2_y):
                        map_x_1 = (coordinate1_x - (value1_x + panel_pos_int_w / rowValue) * index);
                        map_y_1 = (coordinate1_y + (value1_y * index));
                        print("2")
                    elif (coordinate1_x < coordinate2_x) and (coordinate1_y > coordinate2_y):
                        map_x_1 = (coordinate2_x - (value1_x + panel_pos_int_w / rowValue) * index);
                        map_y_1 = (coordinate2_y + (value1_y * index));
                        print("3")
                    elif (coordinate1_x > coordinate2_x) and (coordinate1_y > coordinate2_y):
                        map_x_1 = (coordinate2_x + (value1_x + panel_pos_int_w / rowValue) * index);
                        map_y_1 = (coordinate2_y + (value1_y * index));
                        print("4")
                if (int(value2_x) < 5 and int(value2_y) > 5):
                    if (row_column2[1] < row_column3[1]):
                        map_x_2 = row_column2[0] + (value2_x * index)
                        map_y_2 = row_column2[1] + (value2_y * index)
                    else:
                        map_x_2 = row_column3[0] + (value2_x * index)
                        map_y_2 = row_column3[1] + (value2_y * index)
                elif (int(value2_x) > 5 and int(value2_y) > 5):
                    #斜方向
                    coordinate1_x = row_column2[0]
                    coordinate2_x = row_column3[0]
                    coordinate1_y = row_column2[1]
                    coordinate2_y = row_column3[1]
                    if (coordinate1_x < coordinate2_x) and (coordinate1_y < coordinate2_y):
                        map_x_2 = (coordinate1_x + (value2_x + panel_pos_int_w / rowValue) * index);
                        map_y_2 = (coordinate2_y + (value2_y * index));
                        print("1")
                    elif (coordinate1_x > coordinate2_x) and (coordinate1_y < coordinate2_y):
                        map_x_2 = (coordinate1_x - (value2_x + panel_pos_int_w / rowValue) * index);
                        map_y_2 = (coordinate1_y + (value2_y * index));
                        print("2")
                    elif (coordinate1_x < coordinate2_x) and (coordinate1_y > coordinate2_y):
                        map_x_2 = (coordinate2_x - (value2_x + panel_pos_int_w / rowValue) * index);
                        map_y_2 = (coordinate2_y + (value2_y * index));
                        print("3")
                    elif (coordinate1_x > coordinate2_x) and (coordinate1_y > coordinate2_y):
                        map_x_2 = (coordinate2_x + (value2_x + panel_pos_int_w / rowValue) * index);
                        map_y_2 = (coordinate2_y + (value2_y * index));
                        print("4")

                arg1 = [map_x_1, map_y_1]
                arg2 = [map_x_2, map_y_2]
                column_arr1.append(arg1)
                column_arr2.append(arg2)
                self.add_panel_info(arg1)
                self.add_panel_info(arg2)
            for i in range(Columnvalue):
                value1_x = column_arr1[i][0]
                value1_y = column_arr1[i][1]
                value2_x = column_arr2[i][0]
                value2_y = column_arr2[i][1]
                value_x = (abs(value2_x - value1_x)) / rowValue
                value_y = (abs(value2_y - value1_y)) / (rowValue - 1)
                row_index = 0
                while row_index<row_num:
                    row_index += 1
                    if (int(value_x) > 5 and int(value_y) < 5):
                        # 横向
                        if (value1_x < value2_x):
                            map_x = (value1_x + (value_x + panel_pos_int_w / rowValue) * row_index);
                            map_y = value1_y - (value_y * row_index)
                        else:
                            map_x = (value2_x + (value_x + panel_pos_int_w / rowValue) * row_index);
                            map_y = value2_y - (value_y * row_index)
                    arg1 = [map_x, map_y]
                    self.add_panel_info(arg1)


    def showPanoramic(self,image_bin):
        # 显示全景图地图
        print("显示全景地图")
        self.general_panel_showlist=[]
        self.panel_info_all_list = []
        self.panel_info_dictlist = []
        self.showMapImage()  # 初始化全景图控件
        self.loadImage(image_bin)
        self._scene.signalMousePos.connect(self.cliskMapMovepos) # 连接信号
        self.whlabel = ImagerectboxItem_wh("whlabel")
        # 显示 基本组件图例
        self.panel_info_all_list = sqlitefun.sqlite_select_panelinfolist(self.projecttime)  # 获取全部组件列表信息
        for panel_info_json in self.panel_info_all_list:
            panel_info_dict = json.loads(panel_info_json[1])  # 转为字典
            self.panel_info_dictlist.append(panel_info_dict)  # 加入字典列表方便使用

            # 列表显示增加
            self.listPanelID.addItem(panel_info_dict["panel_name"])

           # 大地图显示组件增加
            panel_pos_int_w = int(panel_info_dict["panel_wh"].split(",")[0])
            panel_pos_int_h = int(panel_info_dict["panel_wh"].split(",")[1])
            panel_pos_int_x = int(panel_info_dict["panel_pos"].split(",")[0]) - panel_pos_int_w/2
            panel_pos_int_y = int(panel_info_dict["panel_pos"].split(",")[1]) - panel_pos_int_h/2

            lightGreenboxIte=PanelrectboxItem(key = panel_info_dict["panel_index"])
            lightGreenboxIte.rectpos = [panel_pos_int_x,panel_pos_int_y,panel_pos_int_w,panel_pos_int_h]
            lightGreenboxIte.color = QColor(0,255,0) # 绿色
            lightGreenboxIte.setFlag(QGraphicsItem.ItemIsSelectable)
            self._scene.addItem(lightGreenboxIte)
            self.general_panel_showlist.append(lightGreenboxIte)

    def cliskMapMovepos(self,arg1,arg2,mode):
        # 监听大地图点击操作 包括 点击 移动 释放
        # arg1 是按下时的点
        # arg2 是移动后的点,释放时也是这个点
        # mode 1 表示 按下  0 表示 释放
        if self.movemode == 0:  # 固定状态下才允许进行其他操作
            #print("当前点击状态",self.cb_label_mode.currentText())
            print("点击参数",arg1,arg2,mode)
            self.selectItem = arg1
            if self.bool_updage_number == 1:
                #修改编号
                if mode == 0:
                    update_number_dialog = Update_Number_dialog(self)
                    update_number_dialog.Update_Number_dialog_Signal.connect(self.getDialogSignal)
                    update_number_dialog.show()

            if self.cb_label_mode.currentText() == "查看":
                #print("当前状态下允许点击组件 查看信息 和修改信息 和获取组件大小")
                if mode == 1 or mode == 0:
                    if self.bool_getpanel_wh == 1 :
                        self._scene.removeItem(self.whlabel)
                        self.whlabel.rectpos = [int(float(arg1[0])),int(float(arg1[1])),int(float(arg2[0]-arg1[0])),int(float(arg2[1]-arg1[1]))]
                        self.whlabel.color = QtGui.QPen(Qt.green,2,Qt.SolidLine)

                        self._scene.addItem(self.whlabel)
                        panel_w = str(abs(int(float(arg2[0]-arg1[0]))))
                        panel_h = str(abs(int(float(arg2[1]-arg1[1]))))
                        self.te_bottom_hint.setText("当前获取到宽高:"+"宽 "+panel_w+" 高 "+panel_h)
                        if mode == 0:
                            self.te_bottom_hint.setText("当前获取到宽高:"+"宽 "+panel_w+" 高 "+panel_h)
                            sqlitefun.sqlite_create_config()
                            sqlitefun.sqlite_insert_config("panel_wh",panel_w+","+panel_h)  # 写进数据库  读取好用
                            print("宽",panel_w,"高",panel_h)
                            self.bool_getpanel_wh = 0 # 左键释放 停止绘图
            if self.cb_label_mode.currentText() == "单点标注":
                if mode == 1 or mode == 0:
                    print("当前模式 单点标注 坐标",arg1)
                    self.add_panel_info(arg1)

            if self.cb_label_mode.currentText() == "单行标注":

                #先点击两个点记录下来，选择行内个数
                if mode == 1 or mode == 0:
                    if(self.rownum==2):
                        self.rownum = self.rownum-1
                        self.rowvalue1=arg1
                        self.add_panel_info(arg1)
                    elif(self.rownum==1):
                        self.rownum=2
                        #弹出弹出框，提示每行显示几个
                        self.rowvalue2 = arg1
                        self.add_panel_info(arg1)
                        self.numDialog(0)

                pass
            if self.cb_label_mode.currentText() == "多行标注":
                if mode == 1 or mode == 0:
                    if (self.row_column == 1):
                        self.rowcolumn[4 - self.row_column] = arg1
                        self.add_panel_info(arg1)
                        self.numDialog(1)
                        self.row_column=4
                    elif (self.row_column <= 4):
                        self.rowcolumn[4-self.row_column]= arg1
                        self.add_panel_info(arg1)
                        self.row_column = self.row_column - 1
                pass
    def get_panel_info(self):
        print("从数据库中获取一次当前面板的信息")
        sqlitefun.sqlite_create_panelinfo(self.projecttime)  # 创建组件信息记录表
        self.label_type_text = sqlitefun.sqlite_select_config("label_type")
        self.panel_model_text = sqlitefun.sqlite_select_config("panel_model")
        self.panel_power_text = sqlitefun.sqlite_select_config("panel_power")
        self.panel_wh_text = sqlitefun.sqlite_select_config("panel_wh")
        self.panel_altitude_text = sqlitefun.sqlite_select_config("panel_altitude")
        self.panel_angle_text = sqlitefun.sqlite_select_config("panel_angle")

        if len(self.label_type_text) == 0:
            self.label_type_text = "光伏组件"
        else:
            self.label_type_text = self.label_type_text[0][0]

        if len(self.panel_model_text) == 0:
            self.panel_model_text = "标准型号"
        else:
            self.panel_model_text = self.panel_model_text[0][0]

        if len(self.panel_power_text) == 0:
            self.panel_power_text = "0"
        else:
            self.panel_power_text = self.panel_power_text[0][0]
       
        if len(self.panel_wh_text) == 0:
            self.panel_wh_text = "10,10"
        else:
            self.panel_wh_text = self.panel_wh_text[0][0]

        if len(self.panel_altitude_text) == 0:
            self.panel_altitude_text = "0"
        else:
            self.panel_altitude_text = self.panel_altitude_text[0][0]

        if len(self.panel_angle_text) == 0:
            self.panel_angle_text = "0"
        else:
            self.panel_angle_text = self.panel_angle_text[0][0]

    def add_panel_info(self,pos):
        print("增加面板点信息")
        self.get_panel_info() # 获取当前组件的信息
        self.panel_pos_text = str(int(pos[0]))+","+str(int(pos[1]) ) # 组件的中心坐标
        self.panel_index_text = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')  # 组件索引 不进行修改的
        self.panel_info_all_list = sqlitefun.sqlite_select_panelinfolist(self.projecttime)  # 获取全部组件列表信息
        self.panel_name_text ="0,"+str(len(self.panel_info_all_list)) #设置一下组件的名称 可以修改

        panel_info_dict = {}
        panel_info_dict["panel_index"] = self.panel_index_text
        panel_info_dict["panel_pos"] = self.panel_pos_text
        panel_info_dict["panel_name"] = self.panel_name_text
        panel_info_dict["label_type"] = self.label_type_text
        panel_info_dict["panel_model"] = self.panel_model_text
        panel_info_dict["panel_power"] = self.panel_power_text
        panel_info_dict["panel_wh"] = self.panel_wh_text
        panel_info_dict["panel_altitude"] = self.panel_altitude_text
        panel_info_dict["panel_angle"] = self.panel_angle_text
        panel_info_json = json.dumps(panel_info_dict,ensure_ascii=False)
        print("调试json信息",panel_info_json)
        sqlitefun.sqlite_insert_panelinfo_json(self.projecttime,self.panel_index_text,panel_info_json) # 写入或者更新组件信息


         # 列表显示增加
        self.listPanelID.addItem(panel_info_dict["panel_name"])

           # 大地图显示组件增加
        panel_pos_int_w = int(panel_info_dict["panel_wh"].split(",")[0])
        panel_pos_int_h = int(panel_info_dict["panel_wh"].split(",")[1])
        panel_pos_int_x = int(panel_info_dict["panel_pos"].split(",")[0]) - panel_pos_int_w/2
        panel_pos_int_y = int(panel_info_dict["panel_pos"].split(",")[1]) - panel_pos_int_h/2

        lightGreenboxIte=PanelrectboxItem(key = panel_info_dict["panel_index"])
        lightGreenboxIte.rectpos = [panel_pos_int_x,panel_pos_int_y,panel_pos_int_w,panel_pos_int_h]
        lightGreenboxIte.color = QColor(0,255,0) # 绿色
        lightGreenboxIte.setFlag(QGraphicsItem.ItemIsSelectable)  # 设置图形项可以选择
        self._scene.addItem(lightGreenboxIte)
        self.general_panel_showlist.append(lightGreenboxIte)

    
    def getlSignal_refresh(self,lists):
        print("用于接收刷新信号")
        #删除面板
        if lists[0]==0:
            print("收到删除信号 进行局部刷新2  局部刷新")
            print("需要删除:", lists[1])
            self.showPanelList()
            for box in self.general_panel_showlist:
                if lists[1] == box.key:
                    self._scene.removeItem(box)
                    self.general_panel_showlist.remove(box)

    def showPanelList(self):
        self.listPanelID.clear()
        for panel_info_json in self.panel_info_all_list:
            panel_info_dict = json.loads(panel_info_json[1])  # 转为字典
            self.panel_info_dictlist.append(panel_info_dict)  # 加入字典列表方便使用
            # 列表显示增加
            self.listPanelID.addItem(panel_info_dict["panel_name"])

    def showMapImage(self):
        self._zoom = 0
        self._empty = True
        self._scene = RGISGraphicsScene() # 使用自定义的QGraphicsScene
        self._scene.signalMousePos.connect(self.selectPiont)
        #self._scene.selectItem.connect(self.selectPiont)
        self._photo = QtWidgets.QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.MapImage.setScene(self._scene)
        self.MapImage.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.MapImage.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.MapImage.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MapImage.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MapImage.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(30, 30, 30)))
        self.MapImage.setFrameShape(QtWidgets.QFrame.NoFrame)
    
    def changeMoveMode(self):
        # 改变地图点击模式/移动模式
        if self.movemode == 0:
            # 现在是固定模式 变更到移动模式
            self.MapImage.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            self.but_movemode.setText("拖动")
            self.movemode = 1
        else:
            self.MapImage.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self.but_movemode.setText("固定")
            self.movemode = 0

    
    def MapimageZoonOut(self):
        # 放大
         if self.hasPhoto():
            factor = 1.25
            self._zoom += 1
            if self._zoom > 0:
                self.MapImage.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0
            
    def MapimageZoonIn(self):
        # 缩小
         if self.hasPhoto():
            factor = 0.75
            self._zoom -= 1
            if self._zoom > 0:
                self.MapImage.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0
    def MapimageZoonRest(self):
        # 还原
        self.clickboxItem_list = []  # 刷新 清空选中列表
        self.getlSignal_refresh([1]) # 刷新 重载全部元素
    
    def hasPhoto(self):
        return not self._empty

    def fitInView(self, scale=True):
        rect = QtCore.QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            self.MapImage.setSceneRect(rect)
            if self.hasPhoto():
                unity = self.MapImage.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.MapImage.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.MapImage.viewport().rect()
                scenerect = self.MapImage.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.MapImage.scale(factor, factor)
            self._zoom = 0
    def setPhoto(self, pixmap=None):
        self._zoom = 0
        if pixmap :
            self._empty = False
            
            self._photo.setPixmap(QtGui.QPixmap(QtGui.QImage.fromData(pixmap)))
        else:
            self._empty = True
            
            self._photo.setPixmap(QtGui.QPixmap())
        self.fitInView()
        
    def loadImage(self,mapimage_bin):
        self.setPhoto(mapimage_bin)

    def region_loc_alter(self):
        #多面板位置移动
        if self.cb_label_mode.currentText() == "查看":
            print("多面板位置移动")
            self.btn_move_ok.setVisible(True)
            self.btn_move_no.setVisible(True)
            print("是否允许面板移动",self.bool_region_move_panel)
            if self.bool_region_move_panel ==0:
                self.bool_region_move_panel=1 #设置为1的时候  允许移动组件
                self.MapImage.setDragMode(QGraphicsView.RubberBandDrag) #设置为可以拉框
                self.btn_move_panel.setEnabled(False) #设置为不可点击
                for box in self.general_panel_showlist:
                    box.bool_IsMovable = 1
                    box.setFlag(QGraphicsItem.ItemIsMovable,True)
        else:
            QMessageBox.information(self, "消息", "请将操作状态改为查看才可移动组件", QMessageBox.Yes)


    def start_fun_ok(self): #确定移动
        print("点击确定按钮")
        # 功能确认
        if self.bool_region_move_panel == 1:
            # 关闭区域选中 修改位置
            self.bool_region_move_panel = 0
            self.btn_move_panel.setEnabled(True)
            self.btn_move_ok.setVisible(False)  # 隐藏掉功能按钮的取消键
            self.btn_move_no.setVisible(False)  # 隐藏掉功能按钮的确认键
            # 模式还原到使用之前
            if self.movemode == 1:
                self.MapImage.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            else:
                self.MapImage.setDragMode(QtWidgets.QGraphicsView.NoDrag)

            box_moved_pos_dist = {}  # 保存移动完成后的坐标和组件编号
            sqlite_panel_info_all = []
            for box in self.general_panel_showlist:
                box.bool_IsMovable = 0
                # box.setFlag(QGraphicsItem.ItemIsMovable, False)  # 设置为不可移动状态
                box_x = str(int(box.sceneBoundingRect().topLeft().x()))
                box_y = str(int(box.sceneBoundingRect().topLeft().y()))
                box_moved_pos_dist.update({box.key: [box_x, box_y]})

                for panel_info in self.panel_info_all_list:
                    if panel_info[0] == box.key:
                        panel_info_dict = json.loads(panel_info[1])  # 转为字典
                        w = int(panel_info_dict["panel_wh"].split(',')[0])
                        h = int(panel_info_dict["panel_wh"].split(',')[1])
                        box_x = str(int(int(box_x)+(w/2)))
                        box_y = str(int(int(box_y)+(h/2)))
                        panel_info_dict["panel_pos"] = box_x+","+box_y


                        panel_info_json = json.dumps(panel_info_dict, ensure_ascii=False)
                        sqlite_panel_info_all.append([panel_info[0],panel_info_json])
            sqlitefun.sqlite_insert_panelinfo_all_json(self.projecttime,sqlite_panel_info_all)




    def end_fun_no(self): #取消移动
        print("点击取消")
        if self.bool_region_move_panel == 1:
            # 关闭区域选中 修改位置
            self.bool_region_move_panel = 0
            self.btn_move_panel.setEnabled(True)
            self.btn_move_ok.setVisible(False)  # 隐藏掉功能按钮的取消键
            self.btn_move_no.setVisible(False)  # 隐藏掉功能按钮的确认键
            # 模式还原到使用之前
            if self.movemode == 1:
                self.MapImage.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            else:
                self.MapImage.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        box_moved_pos_dist = {}  # 保存移动完成后的坐标和组件编号
        for box in self.general_panel_showlist:
            box.bool_IsMovable = 0
            box.setFlag(QGraphicsItem.ItemIsMovable, False)  # 设置为不可移动状态
            box_x = str(int(box.intPos[0]))
            box_y = str(int(box.intPos[1]))
            box_moved_pos_dist.update({box.key: [box_x, box_y]})
            box.setPos(float(box_x), float(box_y))

    def selectPiont(self,arg1,arg2,mode):
        if (mode == 3):
            if len(arg1) > 0:
                self.selectItem = arg1



class RGISGraphicsScene(QGraphicsScene):
    # 自定义QGraphicsScene 场景 用于事件的传送
    selectItem = pyqtSignal(list)
    signalMousePos = pyqtSignal(list,list,int)
    #signalMousePos = pyqtSignal(list)

    def __init__(self,parent = None):
        super(RGISGraphicsScene, self).__init__(parent)
        self.pix =  QPixmap()  # 实例化一个 QPixmap 对象
        self.lastPoint =  QPoint() # 起始点
        self.endPoint =  QPoint() #终点    

    def mousePressEvent(self, event) :   
		# 鼠标左键按下
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton :
            self.lastPoint = event.scenePos()
            self.endPoint = self.lastPoint
            # print("libra按下坐标:",self.lastPoint,self.endPoint)
            #self.mapclickpos = [event.scenePos().x(), event.scenePos().y(), self.selectedItems()]
            #self.mapclickpos = self.selectedItems()
            self.signalMousePos.emit(self.selectedItems(),[],3)

            
	# 鼠标移动事件
    def mouseMoveEvent(self, event):	
        # 鼠标左键按下的同时移动鼠标
        super().mouseMoveEvent(event)
        if event.buttons() and Qt.LeftButton :
            self.endPoint = event.scenePos()
            self.signalMousePos.emit([self.lastPoint.x(),self.lastPoint.y()],[self.endPoint.x(),self.endPoint.y()],1)
            # print("libra移动坐标:",self.lastPoint,self.endPoint)
            #进行重新绘制


    # 鼠标释放事件
    def mouseReleaseEvent( self, event):
		# 鼠标左键释放
        super().mouseReleaseEvent(event)
        if event.button() == Qt.LeftButton :
            self.endPoint = event.scenePos()
            self.signalMousePos.emit([self.lastPoint.x(),self.lastPoint.y()],[self.endPoint.x(),self.endPoint.y()],0)
            # print("libra释放坐标:",self.lastPoint,self.endPoint)
			#进行重新绘制

class PanelrectboxItem(QGraphicsItem):
 # 面板矩形框填充
    def __init__(self,key):
        super(PanelrectboxItem, self).__init__()
        self.color = Qt.blue     # 显示面板的颜色
        self.rectpos = [0,0,100,100]  # 显示面板的坐标
        self.key = key
        self.name = "-1,-1"
        self.bool_IsMovable = 0
        self.intPos = [self.rectpos[0], self.rectpos[1], self.rectpos[2], self.rectpos[3]]



    def boundingRect(self):
        # return PanelrectboxItem.Rect
        return QRectF(self.rectpos[0],self.rectpos[1],self.rectpos[2],self.rectpos[3])
    def resname(self):
        # 用于返回key名称
        return self.key
 
    def paint(self, painter, option, widget):
        # 画个矩形框
        if self.isSelected():
            painter.setPen(Qt.white)  # 选中的颜色
            painter.setBrush(Qt.yellow)
        else:
            painter.setPen(self.color)
            painter.setBrush(self.color)
        painter.drawRect(self.rectpos[0],self.rectpos[1],self.rectpos[2],self.rectpos[3])
        if self.bool_IsMovable == 1:
            self.setFlag(QGraphicsItem.ItemIsMovable, True)  #  故障组件设置为可移动状态
        if self.bool_IsMovable == 0:
            self.setFlag(QGraphicsItem.ItemIsMovable, False)

    def mousePressEvent(self,event):
        # self.mapclickpos = [event.pos().x(),event.pos().y()]
        # print(self.mapclickpos)
        super().mousePressEvent(event)  # 将点击坐标传递下去


class ImagerectboxItem_wh(QGraphicsItem):
 # 面板矩形框
    def __init__(self,PlanetType):
        super(ImagerectboxItem_wh, self).__init__()
        self.color = Qt.blue     # 显示面板的颜色
        self.rectpos = [0,0,0,0]  # 显示面板的坐标
        self.type = PlanetType
        self.boundingRect = [self.rectpos[0],self.rectpos[1],self.rectpos[2],self.rectpos[3]]
        
    def boundingRect(self):
        return QRectF(self.rectpos[0],self.rectpos[1],self.rectpos[2],self.rectpos[3])
 
    def paint(self, painter, option, widget):
        # 画个矩形框
        painter.setPen(self.color)
        painter.drawRect(self.rectpos[0],self.rectpos[1],self.rectpos[2],self.rectpos[3])

class OpenProject(QMainWindow,Ui_open_project):
    # 打开选择历史UI界面
    OpenProject_Signal = pyqtSignal(list) # 自定义信号
    def __init__(self,parent = None):
        super(OpenProject, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.projectlist = sqlitefun.sqlite_select_localist()
        for prlist in self.projectlist:
            self.lw_local_PN.addItem(prlist[0]+ ' / '+prlist[1])
        self.but_open.clicked.connect(self.butOpenClicked)

    def butOpenClicked(self):
        # 历史列表打开
        checkItems = self.lw_local_PN.selectedItems()
        if checkItems:
            self.project_time = str(checkItems[0].text()).split(" / ")[0]
            self.project_name = str(checkItems[0].text()).split(" / ")[1]
            self.send_main_Signal()
            self.close()

    def send_main_Signal(self):
        print("发送相关信息给主界面")
        lists = ["OpenProject",self.project_time,self.project_name]
        self.OpenProject_Signal.emit(lists) # 发射信号 


class NumDialog(QMainWindow,Ui_numDialog):
    NumDialog_Signal = pyqtSignal(list)  # 自定义信号
    def __init__(self,parent = None):
        super(NumDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.Ok_button.clicked.connect(self.butOkClicked)

    def butOkClicked(self):
        self.numValue = self.Num_value.text()
        self.send_main_Signal()
        self.close()

    def send_main_Signal(self):
        print("发送相关信息给主界面")
        lists = ["NumDialog", self.numValue]
        self.NumDialog_Signal.emit(lists)  # 发射信号

class Row_Column_Dialog(QMainWindow, Ui_row_Column_Dialog):
    Row_Column_Dialog_Signal = pyqtSignal(list)  # 自定义信号

    def __init__(self, parent=None):
        super(Row_Column_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ok_row_column_btn.clicked.connect(self.butOkrcClicked)

    def butOkrcClicked(self):
        self.row_value = self.row_num_value.text()
        self.column_value = self.column_num_value.text()
        self.send_main_Signal()
        self.close()

    def send_main_Signal(self):
        print("发送相关信息给主界面")
        lists = ["Row_Column_Dialog", self.row_value,self.column_value]
        self.Row_Column_Dialog_Signal.emit(lists)  # 发射信号

        #self.OK_button.clicked.connect(self.OK_buttonClicked)
class SetPanelInfo(QMainWindow,Ui_setPanelInfo):
    # 设置组件信息
    SetPanelInfo_Signal = pyqtSignal(list) # 自定义信号
    def __init__(self,parent = None):
        super(SetPanelInfo, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.label_type_text = sqlitefun.sqlite_select_config("label_type")
        if len(self.label_type_text) == 0:
            self.label_type_text = "光伏组件"
        else:
            self.label_type_text = self.label_type_text[0][0]
        self.le_label_type.setText(self.label_type_text)


        self.panel_model_text = sqlitefun.sqlite_select_config("panel_model")
        if len(self.panel_model_text) == 0:
            self.panel_model_text = "标准型号"
        else:
            self.panel_model_text = self.panel_model_text[0][0]
        self.le_panel_model.setText(self.panel_model_text)

        self.panel_power_text = sqlitefun.sqlite_select_config("panel_power")
        if len(self.panel_power_text) == 0:
            self.panel_power_text = "0"
        else:
            self.panel_power_text = self.panel_power_text[0][0]
        self.le_panel_power.setText(self.panel_power_text)

        self.panel_wh_text = sqlitefun.sqlite_select_config("panel_wh")
        if len(self.panel_wh_text) == 0:
            self.panel_wh_text = "10,10"
        else:
            self.panel_wh_text = self.panel_wh_text[0][0]
        self.le_panel_wh.setText(self.panel_wh_text)

        self.panel_altitude_text = sqlitefun.sqlite_select_config("panel_altitude")
        if len(self.panel_altitude_text) == 0:
            self.panel_altitude_text = "0"
        else:
            self.panel_altitude_text = self.panel_altitude_text[0][0]
        self.le_panel_altitude.setText(self.panel_altitude_text)

        self.panel_angle_text = sqlitefun.sqlite_select_config("panel_angle")
        if len(self.panel_angle_text) == 0:
            self.panel_angle_text = "0"
        else:
            self.panel_angle_text = self.panel_angle_text[0][0]
        self.le_panel_angle.setText(self.panel_angle_text)

        self.but_save.clicked.connect(self.butSaveClicked)  # 保存信息
    
    def butSaveClicked(self):

        sqlitefun.sqlite_insert_config("label_type",self.le_label_type.text())
        sqlitefun.sqlite_insert_config("panel_model",self.le_panel_model.text())
        sqlitefun.sqlite_insert_config("panel_power",self.le_panel_power.text())
        sqlitefun.sqlite_insert_config("panel_wh",self.le_panel_wh.text())
        sqlitefun.sqlite_insert_config("panel_altitude",self.le_panel_altitude.text())
        sqlitefun.sqlite_insert_config("panel_angle",self.le_panel_angle.text())
        print("组件信息保存成功")
        self.close()

class CreateProject(QMainWindow,Ui_creatProject):
    createproject_Signal = pyqtSignal(list) # 自定义信号
    def __init__(self,parent = None):
        super(CreateProject, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.project_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')   #  获取毫秒时间戳
        self.projectName = ""
        self.lab_projectTime.setText("项目创建时间:"+self.project_time)

        self.but_create.clicked.connect(self.butCreateClicked)
        self.but_map_path.clicked.connect(self.openMapPath)
        sqlitefun.sqlite_init_execute()  # 初始化项目信息表
        
        
    
    def butCreateClicked(self):
        # 相应创建项目按钮事件
        self.projectName = self.le_projectName.text()
        self.mappath = self.le_map_path.text()
        
        if self.projectName == "":
            return False
        sqlitefun.sqlite_create_projecttime(self.project_time,self.projectName)  # 向数据库写入项目时间和项目名称
        basicsfun.savaImagebinSqlite(self.project_time,"panoramic",self.mappath) # 全景图片写入数据库
        print("创建项目名称:"+self.projectName)
        self.send_main_Signal()
        self.close()
    
    def send_main_Signal(self):
        print("发送相关信息给主界面")
        lists = ["CreateProject",self.project_time,self.projectName]
        self.createproject_Signal.emit(lists) # 发射信号
        
    
    def openMapPath(self):
        filename,  _ = QFileDialog.getOpenFileName(self, '请选择地图文件', None,"*.jpg")
        self.le_map_path.setText(filename)

class Update_Panel_info(QMainWindow,Ui_Upadte_Panel_info):
    Update_Panel_info_Signal = pyqtSignal(list)  # 自定义信号
    def __init__(self, parent=None):
        super(Update_Panel_info, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.Ok_button.clicked.connect(self.butOkClicked)

    def butOkClicked(self):
        self.number_value = self.new_number_value.text()
        self.send_main_Signal()

    def setT(self,number_value,item):
        self.new_number_value.setText(number_value)
        self.listItem = item
    def send_main_Signal(self):
        print("发送相关信息给主界面")
        lists = ["Update_Panel_info", self.number_value,self.listItem]
        self.Update_Panel_info_Signal.emit(lists)  # 发射信号

class Update_Number_dialog(QMainWindow,Ui_Update_number_Dialog):
    Update_Number_dialog_Signal = pyqtSignal(list)  # 自定义信号
    def __init__(self, parent=None):
        super(Update_Number_dialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.Ok_button.clicked.connect(self.butOkClicked)

    def butOkClicked(self):
        self.number_value = self.Number_value.text()
        self.send_main_Signal()
        self.close()
    # def setT(self,number_value,item):
    #     self.new_number_value.setText(number_value)
    #     self.listItem = item
    def send_main_Signal(self):
        print("发送相关信息给主界面")
        lists = ["Update_Number_dialog", self.number_value]
        self.Update_Number_dialog_Signal.emit(lists)  # 发射信号


if __name__ =='__main__':
    app = QApplication(sys.argv)

    myWin = MyRGISMain()
    myWin.show()   

    sys.exit(app.exec_()) 