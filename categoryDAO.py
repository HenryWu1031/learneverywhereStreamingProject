from category import category
import pymysql
class categoryDAO:
    
    def __init__(self):
        pass

    def listAllCategories(self):
        ans = []  # 存放最终结果的数组
        db = pymysql.connect(host='localhost', user='root',
                             passwd='123456', db='streamdb', charset='utf8')
        cursor = db.cursor()
        sql = "select * from category"
        cursor.execute(sql)
        allTheData = cursor.fetchall()
        for row in allTheData:
            id=row[0]
            name=row[1]
            pictureId=row[2]
            category1=category(id,name,pictureId)
            ans.append(category1)
        db.close()
        return ans

    def getCategory(self,id):
        db = pymysql.connect(host='localhost', user='root',
                             passwd='123456', db='streamdb', charset='utf8')
        cursor = db.cursor()
        sql = "select * from category where id='%s'" % (id)
        cursor.execute(sql)
        data=cursor.fetchone()
        id=data[0]
        name=data[1]
        pictureId=data[2]
        categoryans=category(id,name,pictureId)
        db.close()
        return categoryans
    
