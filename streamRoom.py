class streamRoom:
    # id=0
    # title="直播间名称"
    # category="谈天说地"
    # anchorname="主播名称"
    # imgid="1"
    # onstream=0

    def __init__(self,id,title,category,anchorname,imgid,onstream):
        self.id=id
        self.title=title
        self.category=category
        self.anchorname=anchorname
        self.imgid=imgid
        self.onstream=onstream

    def isOnStream(self):
        return self.onstream==1

