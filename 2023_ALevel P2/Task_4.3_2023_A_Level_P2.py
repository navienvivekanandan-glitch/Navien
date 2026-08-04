#Task 4.3
from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    result = ''
    file = open('decompressedimage.txt','r')
    lst = []
    for line in file:
        line = line.strip()
        lst.append(line)
    file.close()

    decompressed_string = lst[0]
    decompressed_lst = []
    string = ''
    for i in range(len(decompressed_string)):
        if len(string) != 3:
            string += decompressed_string[i]
        else:
            decompressed_lst.append(string)
            string = ''
            string += decompressed_string[i]
    decompressed_lst.append(string)

    colour_lst = []

    for i in range(len(decompressed_lst)):
        if decompressed_lst[i] == '000':
            colour_lst.append(['red','000'])
        if decompressed_lst[i] == '001':
            colour_lst.append(['white','001'])
        if decompressed_lst[i] == '010':
            colour_lst.append(['yellow','010'])
        if decompressed_lst[i] == '011':
            colour_lst.append(['blue','011'])
        if decompressed_lst[i] == '100':
            colour_lst.append(['black','100'])
        if decompressed_lst[i] == '110':
            colour_lst.append(['green','110'])
        
    image = []

    count = 0
    for i in range(9):
        row = []
        for j in range(9):
            row.append(colour_lst[count])
            count += 1
        image.append(row)
    

    return render_template('home.html',image=image)

app.run()
