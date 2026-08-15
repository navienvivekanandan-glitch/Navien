#Task 4
import sqlite3
from flask import *
#Task 4.1

conn = sqlite3.connect('LIBRARY.db')

conn.execute('''CREATE TABLE IF NOT EXISTS "Book" (
	"BookID"	INTEGER NOT NULL,
	"Title"	TEXT NOT NULL,
	"Genre"	TEXT NOT NULL,
	PRIMARY KEY("BookID")
);''')

conn.execute('''CREATE TABLE IF NOT EXISTS "Member" (
	"MemberNumber"	INTEGER NOT NULL,
	"FamilyName"	TEXT NOT NULL,
	"GivenName"	TEXT NOT NULL,
	PRIMARY KEY("MemberNumber")
);''')

conn.execute('''CREATE TABLE IF NOT EXISTS "Loan" (
	"LoanID"	INTEGER NOT NULL,
	"MemberNumber"	INTEGER NOT NULL,
	"BookID"	INTEGER NOT NULL,
	"DateLoaned"	TEXT NOT NULL,
	"Returned"	REAL NOT NULL,
	PRIMARY KEY("LoanID"),
	FOREIGN KEY("BookID") REFERENCES "Book"("BookID"),
	FOREIGN KEY("MemberNumber") REFERENCES "Member"("MemberNumber")
);''')

conn.commit()
conn.close()


#Task 4.2
def file():
    conn = sqlite3.connect('LIBRARY.db')

    file = open('BOOK.txt','r')
    for line in file:
        line = line.strip()
        line = line.split(',')
        BookID,Title,Genre = line[0],line[1],line[2]
        conn.execute('''INSERT INTO Book(BookID,Title,Genre)
        VALUES (?,?,?)''',(BookID,Title,Genre))

    conn.commit()
    file.close()

    file = open('MEMBER.txt','r')
    for line in file:
        line = line.strip()
        line = line.split(',')
        MemberNumber,FamilyName,GivenName = line[0],line[1],line[2]
        conn.execute('''INSERT INTO Member(MemberNumber,FamilyName,GivenName)
        VALUES (?,?,?)''',(MemberNumber,FamilyName,GivenName))

    conn.commit()
    file.close()

    file = open('LOAN.txt','r')
    for line in file:
        line = line.strip()
        line = line.split(',')
        LoanID,MemberNumber,BookID,DateLoaned,Returned = line[0],line[1],line[2],line[3],line[4]
        conn.execute('''INSERT INTO Loan(LoanID,MemberNumber,BookID,DateLoaned,Returned)
        VALUES (?,?,?,?,?)''',(LoanID,MemberNumber,BookID,DateLoaned,Returned))

    conn.commit()
    file.close()

    conn.close()

#Task 4.3

member_number = int(input("Enter the member number: "))

conn = sqlite3.connect('LIBRARY.db')

result = conn.execute('''SELECT Book.Title, Loan.Returned FROM Book,Member,Loan
    Where Member.MemberNumber = Loan.MemberNumber
    AND Member.MemberNumber = ?
    AND Book.BookID = Loan.BookID;''',(member_number,)).fetchall()

conn.close()

print(f'{"Title":<32}',f'{"Returned"}')
      
for line in result:
    title = line[0]
    returned = line[1]
    print(f'{title:32}',f'{returned}')

#Task 4.4

conn = sqlite3.connect('LIBRARY.db')

results = conn.execute('''SELECT Member.FamilyName,Member.GivenName,Book.Title FROM Book,Member,Loan
    WHERE Loan.Returned = 'FALSE'
    AND Loan.MemberNumber = Member.MemberNumber
    AND Loan.BookID = Book.BookID''').fetchall()


app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html',results = results)

app.run()
