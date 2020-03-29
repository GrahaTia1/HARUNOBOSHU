#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import pymysql
from django import db
from flask import Flask
from flask import request
from flask import jsonify
import requests
DBHOST = 'localhost'
DBUSER = 'root'
DBPASS = '123456'
DBNAME = 'STUDENT'
headers = {"Content-Type": "application/x-www-form-urlencoded"}
app = Flask(__name__,static_folder=r"/workspace_bbt\search")
@app.route("/workspace_bbt\search",methods=['POST'])
def getStu():
        data=request.get_json()
        TEL=data['Tel']

try:
        db = pymysql.connect(DBHOST, DBUSER, DBPASS, DBNAME,charset='utf8')
        print ("连接成功")
        cur = db.cursor()
        sql="SELECT * from stud where `Tel`=TEL"
        results=cur.execute(sql)
        returns = cur.fetchall()
        errCode=0
        for rows in returns:
            NA = rows[1]
            SE = rows[2]
            AG = rows[3]
            DI = rows[4]
            TE = rows[5]
            FI = rows[6]
            SECO = rows[7]
            ti = rows[8]
            FU = rows[9]
            SELFP = rows[10]

        dataa={"Name":"NA","SEX":"SE","AGE":"AG","College":"DI","Tel":"TE","FIRST":"FI","SECOND":"SECO","timing":"ti","FUCONG":"FU","SELFPRO":"SELFP","errcode":"errcode"}
        response=requests.post('C:/Users/AZUMATOGAKU/Desktop/c++/PY/search',json=dataa,headers=headers)
except pymysql.Error as e:
        print(".."+str(e))
db.close()



