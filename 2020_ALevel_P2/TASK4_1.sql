import sqlite3
conn = sqlite3.connect('school.db')

conn.execute('''CREATE TABLE IF NOT EXISTS`People` (
	`PersonID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`FullName`	TEXT NOT NULL,
	`DateOfBirth`	TEXT NOT NULL,
	`ScreenName`	TEXT NOT NULL,
	`IsAdult`	INTEGER NOT NULL
)''';)
conn.commit()
conn.close()
	