from pdb import post_mortem
from re import S
from typing import get_args
from webbrowser import get
from flask import render_template, Blueprint, render_template_string, request
from pickle import NONE
from pprint import pprint

from flask import Flask
from flaskr import ttt
from calendar import TextCalendar
from calendar import HTMLCalendar
from calendar import Calendar
from datetime import datetime

bp = Blueprint("ttt",__name__,)

@bp.route("/ttt",methods=("GET","POST"))
def ttt():
    d = datetime.now()
    m = Calendar()
    a = []
    for i in range(len(m.monthdatescalendar(d.year,d.month))):
        for j in range(len(m.monthdatescalendar(d.year,d.month).pop(0))):
            a.append(m.monthdatescalendar(d.year,d.month).pop(i).pop(j).day)
#    print(a)
    count = range(len(a))
#    print(count)

    if request.method =="POST":
        print("POST!!")
        days = request.form.getlist("day")
        print(days)
        print(len(days))
        
        return render_template("ttt.html",a = a,count = count,days = days)
    

    return render_template("ttt.html",a = a,count = count)

