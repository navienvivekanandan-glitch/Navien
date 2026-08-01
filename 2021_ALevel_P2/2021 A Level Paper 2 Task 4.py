#Task 4

#Task 4.1
from flask import *
import sqlite3


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

#Task 4.2
@app.route('/Round 1/')
def round_1():
    conn = sqlite3.connect('Task4.db')
    results = conn.execute('''SELECT competitor.name,scores.score FROM scores,competitor
        WHERE scores.round = 1 AND scores.id = competitor.id
        ORDER BY scores.score DESC;''')
    return render_template('round1.html',results=results)

@app.route('/Round 2/')
def round_2():
    conn = sqlite3.connect('Task4.db')
    results = conn.execute('''SELECT competitor.name,scores.score FROM scores,competitor
        WHERE scores.round = 2 AND scores.id = competitor.id
        ORDER BY scores.score DESC;''')
    return render_template('round2.html',results=results)

@app.route('/Round 3/')
def round_3():
    conn = sqlite3.connect('Task4.db')
    results = conn.execute('''SELECT competitor.name,scores.score FROM scores,competitor
        WHERE scores.round = 3 AND scores.id = competitor.id
        ORDER BY scores.score DESC;''')
    return render_template('round3.html',results=results)


#Task 4.3
@app.route('/Mean Scores/')
def mean_scores():
    conn = sqlite3.connect('Task4.db')
    cursor = conn.execute('''SELECT competitor.name,scores.score FROM competitor,scores
    WHERE competitor.id = scores.id
    ORDER BY competitor.name ASC;''').fetchall()
    results = []
    total = 0
    count = 0
    i = 0
    while i <= len(cursor)-1:
        if i == 0:
            total = total + int(cursor[i][1])
            count += 1
            i += 1
        if i > 0:
            if str(cursor[i][0]) == str(cursor[i-1][0]):
                total = total + int(cursor[i][1])
                count += 1
                i += 1
            else:
                avg = round(total / count,2)
                results.append((cursor[i-1][0],avg))
                total = 0 + int(cursor[i][1])
                count = 0 + 1
                i += 1
    avg = round(total / count,2)
    results.append((cursor[i-1][0],avg))
                
    return render_template('mean_scores.html',results = results)

#Task 4.4
  
@app.route('/Qualifiers/')
def qualifiers():
    conn = sqlite3.connect('Task4.db')
    cursor = conn.execute('''SELECT competitor.name,scores.score FROM competitor,scores
    WHERE competitor.id = scores.id
    ORDER BY competitor.name ASC;''').fetchall()
    results = []
    total = 0
    i = 0
    while i <= len(cursor)-1:
        if i == 0:
            total = total + int(cursor[i][1])
            i += 1
        if i > 0:
            if str(cursor[i][0]) == str(cursor[i-1][0]):
                total = total + int(cursor[i][1])
                i += 1
            else:
                if total > 250:
                    results.append((cursor[i-1][0],total,'Qualified'))
                else:
                    results.append((cursor[i-1][0],total,'Not Qualified'))
                total = 0 + int(cursor[i][1])
                i += 1
                
    if total > 250:
        results.append((cursor[i-1][0],total,'Qualified'))
    else:
        results.append((cursor[i-1][0],total,'Not Qualified'))
                
    return render_template('qualified.html',results = results)
    

app.run()
