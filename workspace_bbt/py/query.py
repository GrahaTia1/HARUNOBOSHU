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
        if results.count()==0:
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
        else:
            errcode=404
            dataa = {"Name": "NA", "SEX": "SE", "AGE": "AG", "College": "DI", "Tel": "TE", "FIRST": "FI","SECOND": "SECO", "timing": "ti", "FUCONG":"FU","SELFPRO":"SELFP","errcode":"errcode"}
            response = requests.post('C:/Users/AZUMATOGAKU/Desktop/c++/PY/search', json=dataa, headers=headers)
except pymysql.Error as e:
        print(".."+str(e))
db.close()


def questionCapsuleCidPost(body, cid):
    if not checkOpenID():
        return "please call api first", 401
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

