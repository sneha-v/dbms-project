import mysql.connector as con
db = con.connect(
    host = "localhost",
    user = "root",
    password = "snehasindhu@3",
    database = "pro"
)
cur = db.cursor()
# cname = "PYTHON"
# sql1 = "select cid from course where cname = %s"
# val1 =(cname,)
# cur.execute(sql1,val1)
# cid = cur.fetchone()
# sql2 = "select quest,answer,options from test1 where cid=%s"
# val2 = (cid[0],)
# cur.execute(sql2,val2)
# qao = cur.fetchall()
# print(qao)
# DELIMITER $$
#
# CREATE PROCEDURE call_cid1(IN cname VARCHAR(100))
#     BEGIN
#  SELECT cid FROM course
#  WHERE cname = cname;
#     END$$
#
# DELIMITER ;
cur.callproc('call_cid1')
# CALL call_cid('MACHINELEARNING',@cid)
# result = cur.stored_results()
# print(result)
for result in cur.stored_results():
    print(result.fetchall())
# print(re)
# SELECT @cid;
