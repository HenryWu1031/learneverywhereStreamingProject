from categoryDAO import categoryDAO
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.websocket
import os.path
import pymysql
from streamRoom import streamRoom
from streamRoomDAO import streamRoomDAO
from category import category
from categoryDAO import categoryDAO


def strAddStr(str1, str2):
    return str1+str2

def strAddThree(str1,str2,str3):
    return str1+str2+str3

def strAdd4(str1,str2,str3,str4):
    return str1+str2+str3+str4

def ifUserIsLogin(usrname):
    db = pymysql.connect(host='localhost', user='root',
                         passwd='123456', db='streamdb', charset='utf8')
    cursor = db.cursor()
    sql="select loginin from userlogin where username='%s'" % (usrname)
    cursor.execute(sql)
    data=cursor.fetchone()
    if data[0]==1:
        return True
    else:
        return False

class BaseHandler(tornado.web.RequestHandler):
    pass

# 定义首页视图处理类，提示用户登录
class IndexHandler(BaseHandler):
    def get(self):
        self.render('homePage.html',strAdd=strAddStr,strAdd4=strAdd4)

# 定义登录视图处理类
class LoginHandler(BaseHandler):
    def get(self):
        # 获取用户登录的昵称
        # nickname=self.get_argument('nickname')
        # 将用户登录的昵称保存在cookie中，安全cookie
        # self.set_secure_cookie('nickname',nickname,expires_days=None)
        # self.render('chat.html',nickname=nickname)
        
        self.render("login.html")

class AllStreamHandler(BaseHandler):
    def get(self):
        srDao=streamRoomDAO()
        streamRoomList=srDao.getAllStreamRooms()
        self.render('allSteamRoomPage.html',rooms=streamRoomList,strAdd=strAddStr,strAddThree=strAddThree)


class ComplexAllStreamHandler(BaseHandler):
    def get(self,input):
        srDao = streamRoomDAO()
        streamRoomList = srDao.getAllStreamRooms()
        self.render('allSteamRoomPage.html',
                    rooms=streamRoomList, strAdd=strAddStr,usrName=input,strAdd4=strAdd4,strAddThree=strAddThree)


class RegisterPageHandler(BaseHandler):
    def get(self):
        self.render('register.html')

class RegisterHandler(BaseHandler):
    def post(self):
        usrname=self.get_argument('username')
        usrpsd=self.get_argument('password')
        db = pymysql.connect(host='localhost', user='root',passwd='123456', db='streamdb', charset='utf8')
        cursor = db.cursor()
        sql="insert into user values('%s','%s')" % (usrname,usrpsd)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        sql2="select count(*) from userlogin"
        cursor.execute(sql2)
        data=cursor.fetchone()
        id=str(data[0]+1)
        # print(id)
        db.close()
        db = pymysql.connect(host='localhost', user='root',
                             passwd='123456', db='streamdb', charset='utf8')
        cursor = db.cursor()
        sql3 = "insert into userlogin values('%s','%s','%s')" % (id,usrname, 0)
        try:
            cursor.execute(sql3)
            db.commit()
        except:
            db.rollback()
        db.close()
        self.render('registerSuccess.html')

class StreamHomePageHandler(BaseHandler):
    def get(self,input):
        # print(input)
        srDAO=streamRoomDAO()
        sR=srDAO.getStreamRoom(input)
        self.render("streamRooms/"+input+".html",id=input,streamroom=sR,strAdd=strAddStr,strAddThree=strAddThree)   #先试试

class ComplexStreamHomePageHandler(BaseHandler):
    def get(self,input,input2):
        srDAO=streamRoomDAO()
        sR=srDAO.getStreamRoom(input)
        self.render("streamRooms/"+input+".html",id=input,streamroom=sR,strAdd=strAddStr,strAddThree=strAddThree,usrName=input2)

class ComplexIndexHandler(BaseHandler):
    def get(self,input):
        # print(input)
        self.render("homePage.html",usrName=input,strAdd=strAddStr,strAdd4=strAdd4)

class ToApplyPageHandler(BaseHandler):
    def get(self,input):
        categorydao=categoryDAO()
        categories=categorydao.listAllCategories()
        self.render("applyForStreamRoomPage.html",usrName=input,clist=categories)

class AddStreamRoomHandler(BaseHandler):
    def post(self):
        id=self.get_argument('rid')
        title=self.get_argument('rtitle')
        anchorname=self.get_argument('ranchorname')
        category=self.get_argument('rcategory')
        imgid=self.get_argument('rimgid')
        srd=streamRoomDAO()
        srd.addOneStreamRoom(id,title,category,anchorname,imgid,0)
        self.render("streamRoomSuccessApply.html",usrName=anchorname)
        

class BackToIndexWithNameHandler(BaseHandler):
    def post(self):
        name=self.get_argument('username')
        self.render("homePage.html",usrName=name,strAdd=strAddStr)

class LoginProcessHandler(BaseHandler):
    def post(self):
        usrname=self.get_argument('username')
        usrpsd=self.get_argument('userpassword')
        db=pymysql.connect(host='localhost',user='root',passwd='123456',db='streamdb',charset='utf8')
        cursor=db.cursor()
        sql="select count(*) from user where name='%s' and password='%s' " % (usrname,usrpsd)
        cursor.execute(sql)
        data=cursor.fetchone()
        resultNum = data[0]
        # print(data[0])
        if resultNum!=0:
            sql2="update userlogin set loginin=1 where username='%s'" % (usrname)
            try:
                cursor.execute(sql2)
                db.commit()
            except:
                db.rollback()
            db.close()
            self.render("homePage.html", usrName=usrname,strAdd=strAddStr,strAdd4=strAdd4)
        else:
            self.render("loginFailed.html")

class AllCategoryPageHandler(BaseHandler):
    def get(self):
        categorydao=categoryDAO()
        categories=categorydao.listAllCategories()
        self.render("allCategoryPage.html",strAdd=strAddStr,categorylist=categories,strAddThree=strAddThree)

class ComplexAllCategoryPageHandler(BaseHandler):
    def get(self,input):
        categorydao = categoryDAO()
        categories = categorydao.listAllCategories()
        self.render("allCategoryPage.html",usrName=input,strAdd=strAddStr,strAddThree=strAddThree,strAdd4=strAdd4,categorylist=categories)

class SingleCategorySRHandler(BaseHandler):
    def get(self,input):
        categorydao=categoryDAO()
        categoryone=categorydao.getCategory(input)
        srDao=streamRoomDAO()
        srlist=srDao.getStreamRoomsByCategory(categoryone.name)
        self.render("categorySRpage.html",rooms=srlist, strAdd=strAddStr,categoryname=categoryone.name,strAddThree=strAddThree)


class ComplexSingleCategorySRHandler(BaseHandler):
    def get(self,id,name):
        categorydao = categoryDAO()
        categoryone = categorydao.getCategory(id)
        srDao = streamRoomDAO()
        srlist = srDao.getStreamRoomsByCategory(categoryone.name)
        self.render("categorySRpage.html", rooms=srlist, strAdd=strAddStr,categoryname=categoryone.name, strAddThree=strAddThree,usrName=name,strAdd4=strAdd4)

# class TestHandler(BaseHandler):
#     def get(self):
#         sr=streamRoomDAO().getStreamRoom("245")
#         self.render("streamHomePage.html",streamroom=sr,id=sr.id,strAddThree=strAddThree,strAdd=strAddStr)

# 定义接收/发送聊天消息的视图处理类，继承自websocket的WebSocketHandler
class ChatHandler(tornado.websocket.WebSocketHandler):
    # 定义一个集合，用来保存在线的所有用户
    online_users_dict = dict()
    # 从客户端获取cookie信息


    # 重写open方法，当有新的聊天用户进入的时候自动触发该函数
    def open(self,input,name):
        self.roomid=input
        self.usrname=name
        if input in self.online_users_dict:
            self.online_users_dict[input].add(self)
        else:
            self.online_users_dict[input] = set()
            self.online_users_dict[input].add(self)
        # 当有新的用户上线，将该用户加入集合中
        
        # 将新用户加入的信息发送给所有的在线用户
        for user in self.online_users_dict[input]:
            user.write_message('【%s】进入了聊天室' % name)

    # 重写on_message方法，当聊天消息有更新时自动触发的函数
    def on_message(self, message):
        # 将在线用户发送的消息通过服务器转发给所有的在线用户
        for user in self.online_users_dict[self.roomid]:
            user.write_message('%s:%s' % (self.usrname, message))

    # 重写on_close方法，当有用户离开时自动触发的函数
    def on_close(self):
        # 先将用户从列表中移除
        self.online_users_dict[self.roomid].remove(self)
        # 将该用户离开的消息发送给所有在线的用户
        for user in self.online_users_dict[self.roomid]:
            user.write_message('【%s】离开了聊天室~' % self.usrname)

    def check_origin(self, origin):
        return  True

# 程序运行入口
if __name__=='__main__':
    sRD = streamRoomDAO()
    sRD.addOneStreamRoom("245", "吴航宇的直播", "Java开发", "吴航宇","1", 0)
    sRD.addOneStreamRoom("1024", "数学之美", "理科天地", "lhy", "3", 0)
    sRD.addOneStreamRoom("77777", "405第一帅哥", "音乐艺术", "szy", "2", 0)
    sRD.addOneStreamRoom("1031", "springcloud讲解", "Java开发", "why", "1", 0)

    import os
    BASE_DIR=os.path.dirname(__file__)
    app=tornado.web.Application([
        (r'/',IndexHandler),
        (r'/login.html',LoginHandler),
        (r'/login', LoginProcessHandler),
        (r'/allSteamRoomPage.html', AllStreamHandler),
        (r'/chat(\d+)username=(.*)',ChatHandler),
        (r'/registerUser',RegisterHandler),
        (r'/register.html',RegisterPageHandler),
        (r'/streamHomePage/id=(\d+)', StreamHomePageHandler),
        (r'/homePage.html',IndexHandler),
        (r'/homePageusername=(.*)', ComplexIndexHandler),
        (r'/allSteamRoomPageusername=(.*)', ComplexAllStreamHandler),
        (r'/applyForStreamRoomusername=(.*)', ToApplyPageHandler),
        (r'/applyForStreamRoom', AddStreamRoomHandler),
        (r'/nameToIndex', BackToIndexWithNameHandler),
        (r'/streamHomePage/id=(\d+)username=(.*)',ComplexStreamHomePageHandler),
        (r'/allCategoryPage.html', AllCategoryPageHandler),
        (r'/allCategoryPageusername=(.*)', ComplexAllCategoryPageHandler),
        (r'/categorySRPageCid=(\d+)', SingleCategorySRHandler),
        (r'/categorySRPageCid=(\d+)username=(.*)', ComplexSingleCategorySRHandler),
        # (r'/streamHomePage', TestHandler),    #测试用


        
    ],
    template_path=os.path.join(BASE_DIR,'templates'),
    static_path=os.path.join(BASE_DIR,'static'),
    debug=True,
    login_url='/login',
    cookie_secret='CPFL2FJOTQGzR/8DXZEyfAjxS9hSTk0Bs0f/A12RMnwI8UvYUk5NAbNH/wNdkTJ8')
    server=tornado.httpserver.HTTPServer(app)
    server.listen(8000)
    # server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
    
