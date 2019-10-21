#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 19-10-21 下午3:13
# @Author  : Hubery
# @File    : views.py
# @Software: PyCharm
import random

from flask import Blueprint, render_template

from App.ext import db
from App.models import Student

bule = Blueprint('main', __name__)


def init_blue(app):
    app.register_blueprint(blueprint=bule)


@bule.route('/')
def index():
    return 'hello word'


@bule.route('/students/')
def get_students():

    quseryset = Student.query.all()

    query_list = [query.name for query in quseryset]

    return '%s' % query_list


@bule.route('/addstudent/')
def add_student():
    student = Student()
    flag = random.randrange(100)
    sex = random.randint(0, 1)
    student.name = '小明%s号' % flag
    student.sex = sex
    db.session.add(student)
    db.session.commit()
    return 'Add Success'