import mysql.connector as con

class credential(object):

    def __init__(self):
        self.db= con.connect(
            host = "localhost",
            user = "root",
            password = "snehasindhu@3",
            database = "pro"
        )
        self.cur = self.db.cursor(buffered=True)


    def login(self, mail, passs):
        mail_t = (mail,)
        self.cur.execute('select uid from user1 where umail=%s',mail_t)
        uid_fet = self.cur.fetchone()
        if uid_fet == None:
            return False
        elif len(uid_fet) == 0:
            return False
        else:
            self.cur.execute('select upass from user1 where uid=%s',uid_fet)
            upass_fet = self.cur.fetchone()
            up = upass_fet[0]
            if up == passs:
                return True
            else:
                return False


    def signin(self, mail):
        sql = "select * from user1 where umail=%s"
        val = (mail,)
        self.cur.execute(sql,val)
        us_fet = self.cur.fetchall()
        if us_fet == None:
            return False
        elif len(us_fet) == 0:
            return False
        else:
            return True
