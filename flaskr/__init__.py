from pickle import NONE
from pprint import pprint

from flask import Flask
from flaskr import ttt
from calendar import TextCalendar
from calendar import HTMLCalendar
from calendar import Calendar
from datetime import datetime



def create_app(test_config=None):
    app = Flask(__name__) 

    @app.route("/")
    def hello():
        d = datetime.now()
#        pprint(TextCalendar().formatmonth(d.year,d.month),width=2) 
#        print(Calendar().monthdatescalendar(d.year,d.month).__len__()) # Week count in month
#        print(Calendar().monthdatescalendar(d.year,d.month).pop(0)) 
#        print(Calendar().monthdatescalendar(d.year,d.month).pop(0).__len__()) # Day count in a week
#        print(Calendar().monthdatescalendar(d.year,d.month).pop(0).pop(0))
#        print(Calendar().monthdatescalendar(d.year,d.month).pop(0).pop(0).day)
#        print(Calendar().monthdatescalendar(d.year,d.month).pop(0)[0].day)

        s = Calendar().monthdatescalendar(d.year,d.month)
        pprint(s.pop(0).pop(0))
        pprint(s.pop(0))
        
        m = Calendar()
        a = []
        for i in range(m.monthdatescalendar(d.year,d.month).__len__()):
            for j in range(m.monthdatescalendar(d.year,d.month).pop(0).__len__()):
                print(m.monthdatescalendar(d.year,d.month).pop(i).pop(j).day,end=",")
                a.append(m.monthdatescalendar(d.year,d.month).pop(i).pop(j).day)
            print("")
        print("")
        print(a)
        print(a[1])
        print(a.__len__())
        

        return  HTMLCalendar().formatmonth(d.year,d.month)
#        return HTMLCalendar().formatday(1,0)

    app.register_blueprint(ttt.bp)

    return app