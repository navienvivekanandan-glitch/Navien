#Task 4.3
import flask,sqlite3

app = flask.Flask(__name__)

file = open('people.txt','r')
person_type_lst =[]
for line in file:
    line = line.strip().split(',')
    name,DOB,person_type = line[0],line[1],line[2]
    person_type_lst.append(person_type)

file.close()
    
conn = sqlite3.connect('school.db')
results = conn.execute('''SELECT People.FullName, People.ScreenName FROM People;''').fetchall()

@app.route('/')
def home():
    display = []
    for i in range(len(person_type_lst)):
        display.append((results[i][0],results[i][1],person_type_lst[i]))
    return flask.render_template('home.html',display=display)

app.run()
