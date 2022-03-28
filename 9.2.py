from flask import Flask, render_template
import calendar

app = Flask(__name__)

@app.route('/keliamieji')

def metai():
    keliamieji = []
    metus = range(1900, 2101)
    for x in metus:
        if calendar.isleap(x):
            keliamieji.append(x)
    return render_template('index.html', sarasas=keliamieji)


app.run()

