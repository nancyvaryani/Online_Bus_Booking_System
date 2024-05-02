from sqlite3 import *
mycon=connect('pro_database.db')
mycur=mycon.cursor()

qry='create table operator (opid int primary key ,name varchar(40),address varchar(100),phone char(10),email varchar(40))'
mycur.execute(qry)

qry2='insert into operator values(1,"Rayeen","AB Road Guna",9911012344,"rayeenoffice@gmail.com"),(2,"Kamla","AB Road Guna",9476378383,"kamlaoffice@gmail.com"),(3,"Kamna","AB Road Guna",9955012344,"kamnasss@gmail.com");'
mycur.execute(qry2)

qry3='select * from operator '
mycur.execute(qry3)

qry='create table bus (busid int primary key,type  char(15),capacity int,fare int,operid int references operator(opid) on delete cascade, routeid int  )'
mycur.execute(qry)
qry2='insert into bus values(1,"AC 2X2",30,1000,1,1),(2,"AC 3X2",50,800,1,2),(3,"Non AC 2X2",30,600,1,3),(4,"Non AC 3X2",30,600,1,4)'
mycur.execute(qry2)

qry3='select * from bus '
mycur.execute(qry3)
f=mycur.fetchall()

qry='create table route (rid int references bus(routeid) on delete cascade ,sid int ,station_name varchar(30),primary key(rid,sid)  )'
mycur.execute(qry)
qry2='insert into route values(1,1,"Guna"),(1,2,"JayPee College"),(1,3,"Binagunj"),(1,4,"Biora"),(1,5,"Bhopal"),(2,1,"Guna"),(2,2,"JayPee College"),(2,3,"Binagunj"),(2,4,"Biora"),(2,5,"Bhopal")'
mycur.execute(qry2)

qry='create table runs (bid int references bus(busid) on  delete cascade  , rundate date,seats int,primary key(bid,rundate) )'
mycur.execute(qry)
qry2='insert into runs values(1,"2022-12-01",30),(1,"2022-12-02",30),(1,"2022-12-04",30),(1,"2022-12-05",30),(1,"2022-12-06",30),(2,"2022-12-01",30),(2,"2022-12-02",30),(2,"2022-12-04",30),(2,"2022-12-05",30),(2,"2022-12-06",30)'
mycur.execute(qry2)
qry= '''Create table bkd (bkgid int not null ,pname varchar(40),pnum char(10), gender varchar(20),nseat int,fare int ,age int,rt_id int ,src_id int ,
dst_id int ,bkdon date ,trvl date,primary key(bkgid,pnum));'''
mycur.execute(qry)

mycon.commit()



 
