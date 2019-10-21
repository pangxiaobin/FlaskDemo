#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 19-10-21 下午3:17
# @Author  : Hubery
# @File    : models.py
# @Software: PyCharm

from App.ext import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16))
    sex = db.Column(db.Integer, default=0)