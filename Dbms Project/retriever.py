import mysql.connector as con

class retrieve(object):

    def __init__(self):
        self.db= con.connect(
         host = "localhost",
         user = "root",
         password = "snehasindhu@3",
         database = "pro"
        )
        self.cur = self.db.cursor()

    def get_cour(self):
        self.cur.execute("select cname from course")
        n = self.cur.fetchall()
        return n

    def get_topic(self):
        self.cur.execute("select tname from topics")
        t = self.cur.fetchall()
        return t

    def top_disp(self):
        self.cur.execute("select cid from course")
        cid = self.cur.fetchall()
        cidd=[]
        for i in cid:
            cidd.append(i[0])
        cidtop={}
        for i in cidd:
            sql = "select tname from topics where cid=%s"
            val = (i,)
            self.cur.execute(sql,val)
            cidtop[i]= self.cur.fetchall()
        ct = []
        temp = []
        for j in cidtop.keys():
            for k in range(len(cidtop[j])):
                temp.append(cidtop[j][k][0])
            ct.append(temp)
            temp = []
        return ct

    def topic_cou(self, cname):
        sql1 = "select cid from course where cname=%s"
        val1 = (cname,)
        self.cur.execute(sql1,val1)
        cid = self.cur.fetchone()
        sql2 = "select tname from topics where cid=%s"
        self.cur.execute(sql2,cid)
        top = self.cur.fetchall()
        tp_nm = []
        for i in top:
            tp_nm.append(i[0])
        return tp_nm

    def col_cou(self, cname):
        sql1 = "select cid from course where cname=%s"
        val1 = (cname,)
        self.cur.execute(sql1,val1)
        cid = self.cur.fetchone()
        sql2 = "select tid from topics where cid=%s"
        self.cur.execute(sql2,cid)
        top = self.cur.fetchall()
        tp_nm = []
        for i in top:
            tp_nm.append(i[0])
        di = {}
        for ke in tp_nm:
            sql3="select collink from collection1 where tid=%s"
            val3=(ke,)
            self.cur.execute(sql3,val3)
            cl= self.cur.fetchall()
            di[ke]=cl
        ct = []
        temp = []
        for j in di.keys():
            for k in range(len(di[j])):
                temp.append(di[j][k][0])
            ct.append(temp)
            temp = []
        return ct

    def get_name(self, mail):
        sql = "select uname from user1 where umail =%s"
        val = (mail,)
        self.cur.execute(sql,val)
        na = self.cur.fetchone()
        return na[0]

    def enroll(self, cname, mail):
        sql1 = "select cid from course where cname=%s"
        val1 = (cname,)
        self.cur.execute(sql1,val1)
        cid = self.cur.fetchone()
        sql2 = "select uid from user1 where umail=%s"
        val2 = (mail,)
        self.cur.execute(sql2,val2)
        uid = self.cur.fetchone()
        return cid[0],uid[0]

    def check_enroll(self,cid, uid):
        sql="select uid from enroll where cid=%s"
        val = (cid,)
        self.cur.execute(sql,val)
        uids = self.cur.fetchall()
        uidss=[]
        for i in uids:
            uidss.append(i[0])
        if uid in uidss:
            return True
        else:
            return False


    def get_cidli(self):
        cids=[]
        sql1 = "select cid from course"
        self.cur.execute(sql1)
        cid = self.cur.fetchall()
        for i in cid:
            cids.append(i[0])
        return cids

    def get_id(self, mail):
        sql = "select uid from user1 where umail =%s"
        val = (mail,)
        self.cur.execute(sql,val)
        na = self.cur.fetchone()
        return na[0]

    def get_cname(self, cid):
        sql = "select cname from course where cid =%s"
        val = (cid,)
        self.cur.execute(sql,val)
        ca = self.cur.fetchone()
        return ca[0]

    def test_sheet(self,cname):
        sql1 = "select cid from course where cname = %s"
        val1 =(cname,)
        self.cur.execute(sql1,val1)
        cid =self. cur.fetchone()
        sql2 = "select quest,answer,options from test1 where cid=%s"
        val2 = (cid[0],)
        self.cur.execute(sql2,val2)
        qao = self.cur.fetchall()
        return qao

    def prof_list(self,uid):
        sql1 = "select cid from profile1 where uid=%s"
        val1 = (uid,)
        self.cur.execute(sql1,val1)
        cid = self.cur.fetchall()
        name=[]
        for i in cid:
            sql2 = "select cname from course where cid=%s"
            val2 = (i[0],)
            self.cur.execute(sql2,val2)
            cn = self.cur.fetchone()
            name.append(cn[0])
        return name

    def delete_enroll(self,cid,uid):
        sql1 = "delete from enroll where cid=%s and uid=%s"
        val1=(cid,uid)
        self.cur.execute(sql1,val1)
        self.db.commit()

    def cou_count(self,li):
        count=0
        cou_li={}
        for i in li:
            for j in li:
                if i==j:
                    count+=1

            cou_li[i]= count
            count =0
        return cou_li

    def remove_dup(self,prof_list):
        rem=[]
        cou=[]
        for i in prof_list.keys():
            if i not in rem:
                rem.append(i)
                cou.append(prof_list[i])
        return rem,cou


    # def get_con(self):
    #     self.db= con.connect(
    #         host = "localhost",
    #         user = "root",
    #         password = "snehasindhu@3",
    #         database = "pro"
    #     )
    #     self.cur=con.cursor()
    #     return self.db,self.cur
