from flask import Flask, render_template
import calendar

app = Flask(__name__)

@app.route('/year')
def year():
    leap = []
    range_of_year = range(1900, 2101)
    for x in range_of_year:
        if calendar.isleap(x):
            leap.append(x)
    return render_template('index.html', list=leap)


app.run()
