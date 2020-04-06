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
    r = requests.get('/workspace_bbt/page4.html')
    print (r.status_code)


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

def questionCapsuleCidPost(body, cid):
    u_info = database.getInfo(flask.session.get("open_id"))
    if u_info is None:
        return "NOT FOUND", 404
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())
        info = database.getQuestionCapsuleByID(u_info[0], cid)
        if not info:
            return "not found", 404
        if info[6]
            return "Already answered", 409
        print (body)
        if not body.answer:
            return "bad request", 400
        qid = int(info[3])
        database.updateQuestionCapsule(cid, body.answer)
        return {
            "id": info[0],
            "question": questions[qid // 100 - 1][qid % 100],
            "answer": info[4].decode("utf-8") == "voice" and "audio" or "text",
            "time": int(info[5].timestamp()),
            "new_answer": body.answer
        }
    return "Bad request", 400


def time_capsules_get():
    if not checkOpenID():
        return "please call api first", 401
    u_info = database.getInfo(flask.session.get("open_id"))
    if u_info is None:
        return "NOT FOUND", 404
    info = database.getTimeCapsules(u_info[2])
    ret = []
    for e in info:
        ret.append({
            "from": database.getNameByID(e[1]).decode("utf-8"),
            "to": e[2].decode("utf-8"),
            "type": e[4].decode("utf-8") == "voice" and "audio" or "text",
            "content": e[7] and getAudioPath(e[7]) or e[6].decode("utf-8"),
            "time": int(e[9].timestamp())
        })
        return ret