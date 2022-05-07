from flask import Flask, render_template
import calendar

app = Flask(__name__)

@app.route('/leap')

def year():
    leap = []
    enter_year = range(1900, 2101)
    for x in enter_years:
        if calendar.isleap(x):
            leap.append(x)
    return render_template('index.html', list=leap)


app.run()

