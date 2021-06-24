import pymysql
from streamRoom import streamRoom 
from addNewHtml import addNewHtml
class streamRoomDAO:

    def __init__(self):
        pass

    def getAllStreamRooms(self):
        ans = [] #存放最终结果的数组
        db = pymysql.connect(host='localhost', user='root',passwd='123456', db='streamdb', charset='utf8')
        cursor=db.cursor()
        sql="select * from streamroom"
        cursor.execute(sql)
        allTheData=cursor.fetchall()
        for row in allTheData:
            id=row[0]
            title=row[1]
            category=row[2]
            anchorname=row[3]
            imgid=row[4]
            onstream=row[5]
            streamroom1=streamRoom(id,title,category,anchorname,imgid,onstream)
            ans.append(streamroom1)
        db.close()
        return ans

    def addOneStreamRoom(self,id,title,category,anchorname,imgid,onstream):
        db = pymysql.connect(host='localhost', user='root',passwd='123456', db='streamdb', charset='utf8')
        cursor = db.cursor()
        sql="insert into streamroom values('%s','%s','%s','%s','%s','%s')" % (id,title,category,anchorname,imgid,onstream)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()
        aNH=addNewHtml(id)
        aNH.addOneHtmlPage()
        
    def getStreamRoom(self,id):
        db = pymysql.connect(host='localhost', user='root',passwd='123456', db='streamdb', charset='utf8')
        cursor = db.cursor()
        sql="select * from streamroom where id='%s'" % (id)
        cursor.execute(sql)
        data=cursor.fetchone()
        sr=streamRoom(data[0],data[1],data[2],data[3],data[4],data[5])
        return sr
                            
    def getStreamRoomsByCategory(self,name):
        ans = []  # 存放最终结果的数组
        db = pymysql.connect(host='localhost', user='root',
                             passwd='123456', db='streamdb', charset='utf8')
        cursor = db.cursor()
        sql = "select * from streamroom where category='%s'" % (name)
        cursor.execute(sql)
        allTheData = cursor.fetchall()
        for row in allTheData:
            id = row[0]
            title = row[1]
            category = row[2]
            anchorname = row[3]
            imgid = row[4]
            onstream = row[5]
            streamroom1 = streamRoom(
                id, title, category, anchorname, imgid, onstream)
            ans.append(streamroom1)
        db.close()
        return ans

