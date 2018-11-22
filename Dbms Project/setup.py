import mysql.connector as con

db = con.connect(
    host = "localhost",
    user = "root",
    password = "snehasindhu@3",
    database = "pro"
)
cur = db.cursor()
cur.execute('create table user1(uid bigint not null auto_increment,umail varchar(100) not null, uname varchar(100) not null,upass varchar(50) not null,uphone bigint not null, constraint p11 primary key(uid))')
cur.execute('create table course(cid bigint not null auto_increment,cname varchar(100) not null, cduration bigint not null,constraint p12 primary key(cid))')
cur.execute('create table enroll(cid bigint not null,uid bigint not null,constraint p13 primary key(cid,uid),constraint p21 foreign key(uid) references user1(uid) on delete cascade,constraint p31 foreign key(cid) references course(cid) on delete cascade)')
cur.execute('create table topics(tid bigint not null auto_increment, tname varchar(100) not null, tduration bigint not null, cid bigint not null, constraint p14 primary key(tid),constraint p41 foreign key(cid) references course(cid) on delete cascade)')
cur.execute('create table collection1(colid bigint not null auto_increment, coltype varchar(100) not null,collink varchar(1000) not null,tid bigint not null, constraint p18 primary key(colid),constraint p81 foreign key(tid) references topics(tid) on delete cascade)')
cur.execute('create table test1(qid bigint not null auto_increment,answer varchar(10) not null, quest varchar(1000) not null,cid bigint not null,options varchar(1000) not null, constraint p16 primary key(qid), constraint p61 foreign key(cid) references course(cid) on delete cascade)')
cur.execute('create table profile1(uid bigint not null, cid bigint not null,constraint p88 foreign key(uid) references user1(uid) on delete cascade, constraint p99 foreign key(cid) references course(cid) on delete cascade)')
db.commit()
