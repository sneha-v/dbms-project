import mysql.connector as con
from flask import flash

class insert:

    def __init__(self):
        self.db= con.connect(
         host = "localhost",
         user = "root",
         password = "snehasindhu@3",
         database = "pro"
        )
        self.cur = self.db.cursor()

    def insert_user(self,uname,upass,uphone,umail):
        sql = """insert into user1(uname,upass,uphone,umail) values (%s,%s,%s,%s)"""
        val = (uname,upass,uphone,umail)
        self.cur.execute(sql,val)
        self.db.commit()

    def enroll_user(self,cid, uid):
        sql = "insert into enroll values(%s,%s)"
        val = (cid,uid)
        self.cur.execute(sql,val)
        self.db.commit()


    def insert_courses(self, cname,cdura):
        sql1 = """insert into course(cname,cduration) values (%s,%s)"""
        sql2 = """select cid from course where cname=%s"""
        val1 = (cname,)
        val2 = (cdura,)
        val3 = (cname,cdura)
        self.cur.execute(sql2,val1)
        cthere = self.cur.fetchone()
        if cthere == None:
            self.cur.execute(sql1,val3)
        else:
            error ="course already exists"
            return error
        self.db.commit()


    def topics(self, cname, topicname, topicdur):
        sql1 = """select cid from course where cname =%s"""
        val1 = (cname,)
        self.cur.execute(sql1,val1)
        cidd = self.cur.fetchone()
        if cidd==None:
            error = "course doesnot exist"
            return error
        else:
            sql2 = """insert into topics(tname,tduration,cid) values (%s,%s,%s)"""
            val2 = (topicname,topicdur,cidd[0])
            self.cur.execute(sql2,val2)
            self.db.commit()

    def quest(self, cname, quest,answer,options):
        sql1 = """select cid from course where cname =%s"""
        val1 = (cname,)
        self.cur.execute(sql1,val1)
        cidd = self.cur.fetchone()
        if cidd==None:
            error = "course doesnot exist"
            return error
        else:
            sql2 = """insert into test1(answer,quest,cid,options) values (%s,%s,%s,%s)"""
            val2 = (answer,quest,cidd[0],options)
            self.cur.execute(sql2,val2)
            self.db.commit()


    def collection(self, topicname, coll,col_type):
        sql3 = """select tid from topics where tname=%s"""
        val3 = (topicname,)
        self.cur.execute(sql3,val3)
        tidd = self.cur.fetchone()
        if tidd == None:
            error = "topic doesnot exist"
            return error
        sql4 = """insert into collection1(coltype,collink,tid) values(%s,%s,%s)"""
        val4 = (col_type,coll,tidd[0])
        self.cur.execute(sql4,val4)
        self.db.commit()

    def insert_profile(self,cid, uid):
        sql3="insert into profile1 values(%s,%s)"
        val3 =(uid,cid)
        self.cur.execute(sql3,val3)
        self.db.commit()

# if __name__=="__main__":
#     innn= insert()
#     chc = input("do you want to enter a course? yes/no")
#     if chc=='yes':
#         while True:
#             n=input("enter the new course name")
#             d = input("enter the duration of the course")
#             innn.insert_courses(n,d)
#             choice = input("do you want to insert another course? yes/no")
#             if choice=='no':
#                 break
#     cht = input("do you want to insert a topic under any course? yes/no")
#     if cht == 'yes':
#         while True:
#             cname = input("enter the course name under which topic is to be inserted")
#             topicname = input("enter the topic name")
#             tdur= input("enter the topic duration")
#             y=innn.topics(cname,topicname,tdur)
#             if y==0:
#                 break
#             choi = input("do you want to add more topics? yes/no")
#             if choi == "no":
#                 break
#     chc = input("do you want to insert collection for any topic? yes/no")
#     if chc == "yes":
#         while True:
#             tname = input("enter the topic name under which collection has to be inserted")
#             colink = input("enter the collection link")
#             coltype= input("enter the collection type")
#             x=innn.collection(tname,colink,coltype)
#             if x==0:
#                 break
#             ch = input("do you still want to add the collection under this topic?")
#             if ch=='no':
#                 break
#     print("thank you")
