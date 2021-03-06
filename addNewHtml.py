class addNewHtml:

    id=0

    def __init__(self,id):
        self.id=id

    def addOneHtmlPage(self):
        path="./templates/streamRooms/"+str(self.id)+".html"
        f=open(path,"w",encoding="utf8")
        message="""
        <head>
    <meta charset="UTF-8">
    <title>{{streamroom.anchorname}}的直播间 随地学直播间</title>
    <script src="../static/libs/js/jquery/2.0.0/jquery.min.js"></script>
    <link href="../static/libs/css/bootstrap/3.3.6/bootstrap.min.css" rel="stylesheet">
    <script src="../static/libs/js/bootstrap/3.3.6/bootstrap.min.js"></script>
    <link href="https://vjs.zencdn.net/7.0.3/video-js.css" rel="stylesheet">
    <script src="https://vjs.zencdn.net/7.0.3/video.js"></script>
</head>
<style>
    /* 开始导航栏css */
    div.navigatorDiv{
        background-color: #e3dada;
    }
    div.navigatorDiv{
        height: 40px;
        line-height: 40px;
    }
    img.logoIcon{
        width: 40px;
        height: 37px;
    }
    div.firstNavigatorWordDiv{
        float: left;
    }
    div.navigatorWordDiv{
        float: left;
        margin-left: 95px;
    }
    a.indexWordHref{
        margin-left: 60px;
    }
    input.searchBarTextBox{
        height: 25px;
        margin-left: 200px;
    }
    img.navigatorSmallIcon{
        width: 20px;
        height: 20px;
    }
    div.navigatorSearchBarDiv{
        float: left;
    }
    div.navigatorWordRightDiv{
        float:right;
        margin-right: 40px;
    }
    div.leftOne{
        margin-right: 70px;
    }
    a.navigatorHref{
        font-size: 16px;
        font-family: Arial;
        color: #242323;
    }
    a.navigatorHref:hover{
        text-decoration: none;
        color: #d40c0c;
    }
    /* 结束导航栏css */
    div.midPart{
        width: 18%;
        height: 20px;
        background-color: #6b5958;
    }
    /* 左边部分css */
    div.leftAllStreamDiv{
        background-color: #6b5958;
        width: 18%;
        height: 570px;
        clear: both;
        float: left;
    }
    /* div.leftPartWordDiv a.allStreamColor{
        color: #5c1b17;
    } */
    div.leftPartWordDiv{
        padding-top: 12px;
        font-size: 26px;
        margin-bottom: 20px;
        margin-left: 20px;
    }
    div.leftPartWordDiv a{
        color: #c9645f;
    }
    div.leftPartWordDiv a:hover{
        text-decoration: none;
        color: red;
    }
    div.leftPartManyLinksDiv{
        height: 110px;
    }
    div.simpleLinkDiv{
        width: 48%;
        height: 20px;
        float: left;
        text-align: center;
        margin-top: 5px;
        background-color: #383232;
    }
    div.simpleLinkDiv a{
        color: white;
    }
    div.simpleLinkDiv a:hover{
        text-decoration: none;
        color: red;
    }
    div.oddSimpleDiv{
        margin-left: 5px;
    }
    /* 左边的部分 */
    /* 右边的部分 */
    div.streamRoomRightPartDiv{
        float: right;
        width: 82%;
        height: 570px;
    }
    div.mainStreamRoomWindow{
        width: 600px;
        padding-left: 70px;
        padding-top: 30px;
        float: left;
    }
    div.anchorPictureDiv{
        width: 50px;
        height: 50px;
        float: left;
    }
    img.anchorPicture{
        width: 45px;
        height: 45px;
    }
    div.rightTalkTextPartDiv{
        text-align: center;
        float: right;
        margin-right: 30px;
    }
    div.streamWindowTopDescDiv{
        margin-bottom: 40px;
    }
    div.streamTitleAndAnchorName{
        text-align: center;
    }
    span.streamBigTitle{
        display: block;
        margin-bottom: 8px;
        font-size: 20px;
        font-family: 黑体;
    }
    div.contentPartDiv{
        padding-top: 50px;
    }
    textarea.contentTextDiv{
        width: 300px;
        height: 400px;
    }
    div.sendMessagePartDiv{
        margin-top: 10px;
    }
    button.submitButton{
        margin-top: 10px;
        margin-left: 20px;
    }
    textarea.sendPartDiv{
        height: 50px;
    }
    

</style>



<div class="streamHomePageDiv">
    <!-- 导航栏 -->
    <div class="navigatorDiv">
        <div class="firstNavigatorWordDiv">
            <img src=../static/app/image/logo.png class="logoIcon">
            {% try %}
            {% if usrName %}
                {% set first="../homePageusername=" %}
                <a href={{strAdd(first,usrName)}} class="indexWordHref navigatorHref"><span>首页</span></a>
            {% end %}
            {% except %}
            <a href="../homePage.html" class="indexWordHref navigatorHref"><span>首页</span></a>
            {% end %}

        </div>
        <div class="navigatorWordDiv">
        {% try %}
            {% if usrName %}
                {% set first="../allSteamRoomPageusername=" %}
                <a href={{strAdd(first,usrName)}} class="navigatorHref"><span>直播</span></a>
            {% end %}
            {% except %}
            <a href="../allSteamRoomPage.html" class="navigatorHref"><span>直播</span></a>
            {% end %}
        </div>
        <div class="navigatorWordDiv"><a href="homePage.html" class="navigatorHref">
        {% try %}
            {% if usrName %}
                <a href={{strAdd("../allCategoryPageusername=",usrName)}} class="navigatorHref"><span>分类</span></a>
            {% end %}
            {% except %}
                <a href="../allCategoryPage.html" class="navigatorHref"><span>分类</span></a>
            {% end %}
        </div>
        <div class="navigatorSearchBarDiv">
            <form action="post">
                <input name="searchBarTextBox" class="searchBarTextBox" placeholder="why">
                <button class="btn btn-danger searchButton" type="submit">搜索</button>
            </form>
        </div>
        <div class="navigatorWordRightDiv">
            <img src="../static/app/image/loginLogo.png" class="navigatorSmallIcon">
            <a href="../login.html" class="navigatorHref">
                {% try %}
                {% if usrName %}
                    <span>{{usrName}}</span>
                {% end %}
                {% except %}
                    <span>登录</span>
                {% end %}
            </a>
            <span class="separateIcon">|</span>
            <a href="../register.html" class="navigatorHref"><span>注册</span></a>
        </div>
        <div class="navigatorWordRightDiv leftOne">
            <img src="../static/app/image/historyLogo.png" class="navigatorSmallIcon">
            <a href="#nowhere" class="navigatorHref"><span>历史</span></a>
        </div>
    </div>
    <div class="midPart"></div>
    <!-- 左边的部分 -->
    <div class="leftAllStreamDiv">
        <div class="leftPartWordDiv">
            <a href="#nowhere"><span>我的关注</span></a>
        </div>
        <div class="leftPartWordDiv">
            {% try %}
            {% if usrName %}
                <a href={{strAdd("../allSteamRoomPageusername=",usrName)}} class="allStreamColor"><span>全部直播</span></a>
            {% end %}
            {% except %}
                <a href="../allSteamRoomPage.html" class="allStreamColor"><span>全部直播</span></a>
            {% end %}
        </div>
        <div class="leftPartWordDiv">
            <a href="#nowhere"><span>推荐直播</span></a>
        </div>
        <div class="leftPartManyLinksDiv">
            <div class="simpleLinkDiv">
                {% try %}
                {% if usrName %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="7" %}
                {% set beforeUserName="username=" %}
                <a href={{strAdd4(roomURL,cid,beforeUserName,usrName)}}><span>高等数学</span></a>
                {% end %}
                {% except %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="7" %}
                <a href={{strAdd(roomURL,cid)}}><span>高等数学</span></a>
                {% end %}
            </div>
            <div class="simpleLinkDiv oddSimpleDiv">
                {% try %}
                {% if usrName %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="8" %}
                {% set beforeUserName="username=" %}
                <a href={{strAdd4(roomURL,cid,beforeUserName,usrName)}}><span>历史趣事</span></a>
                {% end %}
                {% except %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="8" %}
                <a href={{strAdd(roomURL,cid)}}><span>历史趣事</span></a>
                {% end %}
            </div>
            <div class="simpleLinkDiv"><a href="#nowhere">
                {% try %}
                {% if usrName %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="9" %}
                {% set beforeUserName="username=" %}
                <a href={{strAdd4(roomURL,cid,beforeUserName,usrName)}}><span>法学专栏</span></a>
                {% end %}
                {% except %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="9" %}
                <a href={{strAdd(roomURL,cid)}}><span>法学专栏</span></a>
                {% end %}
            </div>
            <div class="simpleLinkDiv oddSimpleDiv">
                {% try %}
                {% if usrName %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="1" %}
                {% set beforeUserName="username=" %}
                <a href={{strAdd4(roomURL,cid,beforeUserName,usrName)}}><span>Java开发</span></a>
                {% end %}
                {% except %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="1" %}
                <a href={{strAdd(roomURL,cid)}}><span>Java开发</span></a>
                {% end %}
            </div>
            <div class="simpleLinkDiv">
                {% try %}
                {% if usrName %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="10" %}
                {% set beforeUserName="username=" %}
                <a href={{strAdd4(roomURL,cid,beforeUserName,usrName)}}><span>建筑学科</span></a>
                {% end %}
                {% except %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="10" %}
                <a href={{strAdd(roomURL,cid)}}><span>建筑学科</span></a>
                {% end %}
            </div>
            <div class="simpleLinkDiv oddSimpleDiv">
                {% try %}
                {% if usrName %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="11" %}
                {% set beforeUserName="username=" %}
                <a href={{strAdd4(roomURL,cid,beforeUserName,usrName)}}><span>食品科学</span></a>
                {% end %}
                {% except %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="11" %}
                <a href={{strAdd(roomURL,cid)}}><span>食品科学</span></a>
                {% end %}
            </div>
            <div class="simpleLinkDiv">
                {% try %}
                {% if usrName %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="12" %}
                {% set beforeUserName="username=" %}
                <a href={{strAdd4(roomURL,cid,beforeUserName,usrName)}}><span>音乐艺术</span></a>
                {% end %}
                {% except %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="12" %}
                <a href={{strAdd(roomURL,cid)}}><span>音乐艺术</span></a>
                {% end %}
            </div>
            <div class="simpleLinkDiv oddSimpleDiv">
                {% try %}
                {% if usrName %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="13" %}
                {% set beforeUserName="username=" %}
                <a href={{strAdd4(roomURL,cid,beforeUserName,usrName)}}><span>语言学科</span></a>
                {% end %}
                {% except %}
                {% set roomURL="../categorySRPageCid=" %}
                {% set cid="13" %}
                <a href={{strAdd(roomURL,cid)}}><span>语言学科</span></a>
                {% end %}
            </div>
        </div>
        <div class="leftPartWordDiv">
            {% try %}
            {% if usrName %}
                <a href={{strAdd("../applyForStreamRoomusername=",usrName)}}><span>如何开启直播</span></a>
            {% end %}
            {% except %}
                <a href="../login.html"><span>如何开启直播</span></a>
            {% end %}
        </div>
        <div class="leftPartWordDiv">
            <a href="#nowhere"><span>随地学问题反馈</span></a>
        </div>
    </div>
    <!-- 右边的部分 -->
    <div class="streamRoomRightPartDiv">
        <div class="mainStreamRoomWindow">
            <div class="streamWindowTopDescDiv">
                <div class="anchorPictureDiv"><img src="../../static/app/image/3.jpg" class="anchorPicture"></div>
                <div class="streamTitleAndAnchorName">
                    <span class="streamBigTitle">{{streamroom.title}}</span>
                    <span class="anchorName">{{streamroom.anchorname}}</span>
                </div>
            </div>
            <div class="streamRoomVideoDiv">
                <video id="myVideo" class="video-js vjs-default-skin vjs-big-play-centered" controls preload="auto" width="550px" height="420px"  data-setup='{}'>
                    {% set one="http://10.70.84.174:8000/hls1/" %}
                    {% set three=".m3u8" %}
                <source id="source" type="application/x-mpegURL" src={{strAddThree(one,id,three)}} >
                </video>
            </div>
        </div>
        <div class="rightTalkTextPartDiv">
            <div class="contentPartDiv"><textarea class="contentTextDiv" id="contentTextDiv"></textarea></div>
            <form onsubmit="return false;">
                {% try %}
                {% if usrName %}
                <input id="checkIfLogin" hidden value={{usrName}}>
                <input id="username" name="username" class="username" hidden value={{usrName}}>
                {% end %}
                {% except %}
                <input id="checkIfLogin" hidden value="nologin">
                <input id="username" name="username" class="username" hidden value="游客">
                {% end %}
                <div class="sendMessagePartDiv">
                    <textarea class="sendPartDiv" id="sendPartDiv" name="message"></textarea>
                    <input id="room" name="room" class="room" hidden value={{id}}>
                    
                </div>
            <button class="submitButton" onclick="send(this.form.message.value)">提交</button>
            </form>
        </div>
    </div>
</div>

<script>
    var socket;
    if(!window.WebSocket){
        window.WebSocket=window.MozWebSocket;
    }
    if(window.WebSocket){
        var firstURLpart="ws://10.70.122.66:8000/chat";
        var element=document.getElementById('room');
        var element2=document.getElementById('username');
        var secondURLpart=element.value;
        var mid="username="
        var thirdURLpart=element2.value;
        var finalURL=firstURLpart+secondURLpart+mid+thirdURLpart;
        console.log(finalURL);
        socket=new WebSocket(finalURL);
        socket.onmessage=function(event){
            var preContent=document.getElementById('contentTextDiv');
            preContent.value=preContent.value+'\\n'+event.data;
        };
        socket.onopen=function(event){
            var preContent=document.getElementById('contentTextDiv');
            preContent.value='欢迎来到直播间！';
        };
        socket.onclose=function(event){
            var preContent=document.getElementById('contentTextDiv');
            preContent.value=preContent.value+'\\n'+event.data;
        }
    }else{
        alert("Your browser does not support web socket!");
    }
    function send(message){
        var element=document.getElementById('username');
        var flag=element.value;
        if(flag=="游客"){
            alert("您未登录！请先登录！");
            window.location.href="../login.html";
        }
        if(!window.WebSocket){return;}
        if(socket.readyState==WebSocket.OPEN){
            socket.send(message);
            var element=document.getElementById('sendPartDiv');
            element.value="";
        }else{
            alert('this socket is not opened!')
        }
    }

</script>

        """
        f.write(message)
        f.close()
