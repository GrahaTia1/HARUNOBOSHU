#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import pymysql
from django import db
from flask import Flask
from flask import request
from flask import jsonify
DBHOST = 'localhost'
DBUSER = 'root'
DBPASS = '123456'
DBNAME = 'STUDENT'
app = Flask(__name__,static_folder=r"/workspace_bbt\CC")
@app.route("/workspace_bbt\CC",methods=['POST'])
def getStu():
    data=request.get_json()
    Na=data['Name']
    SE=data['SEX']
    AG=data['AGE']
    DI=data['College']
    TE=data['Tel']
    FI=data['FIRST']
    SECO=data['SECOND']
    ti=data['timing']
    FU==data['FUCONG']
    SELFP = data['SELFPRO']
    rem=False
    if(data['remember']):
        rem=True


def _init_(self):
        self.db = pymysql.connect(DBHOST, DBUSER, DBPASS, DBNAME,charset='utf-8')
        print("连接上了")
        self.cur = db.cursor()
def uploaddata(self,NA,SE,AG,DI,TE,FI,SECO,ti,FU,SELFP):
        args=((NA,SE,AG,DI,TE,FI,SECO,ti,FU,SELFP))
        self.cur.execute('Insert into `stud` values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")',args)
        self.db.commit()
        print ("添加成功")
        return True
