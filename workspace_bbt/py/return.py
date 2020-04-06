#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import json
import pymysql
from flask import Flask
from flask import request
from flask import  jsonify
DBHOST = 'localhost'
DBUSER = 'root'
DBPASS = '123456'
DBNAME = 'STUDENT1'


try:
        db = pymysql.connect(DBHOST, DBUSER, DBPASS, DBNAME,charset='utf8')
        print ("连接成功")
        cur = db.cursor()
        sql="SELECT * from stud"
        results=cur.execute(sql)
        returns=cur.fetchall()
        desc = cur.description
        for field in desc:
                print(field[0])
        for rows in returns:
                id=rows[0]
                NA=rows[1]
                SE=rows[2]
                AG = rows[3]
                DI = rows[4]
                TE = rows[5]
                FI = rows[6]
                SECO = rows[7]
                ti = rows[8]
                FU = rows[9]
                SELFP = rows[10]
        args = ((id, NA, SE, AG, DI, TE, FI, SECO, ti, FU, SELFP))
        print(args)
except pymysql.Error as e:
        print("baiogechuangjianshibai"+str(e))

db.close()


