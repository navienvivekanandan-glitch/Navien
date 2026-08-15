#Task 3.1
import sqlite3

conn = sqlite3.connect('DataBase.db')
conn.execute('''CREATE TABLE IF NOT EXISTS `User` (
	`Username`	TEXT NOT NULL,
	`Blocked`	INTEGER NOT NULL,
	PRIMARY KEY(`Username`)
);''')

conn.execute('''CREATE TABLE IF NOT EXISTS `Post` (
	`PostID`	TEXT NOT NULL,
	`PostText`	TEXT,
	`DateTimePosted`	TEXT NOT NULL,
	`UserName`	TEXT NOT NULL,
	FOREIGN KEY(`UserName`) REFERENCES `User`(`Username`),
	PRIMARY KEY(`PostID`)
);''')

conn.execute('''CREATE TABLE IF NOT EXISTS `Comment` (
	`CommentID`	TEXT NOT NULL,
	`PostID`	TEXT NOT NULL,
	`Username`	TEXT NOT NULL,
	`TheText`	TEXT NOT NULL,
	`DateTimeCommented`	TEXT NOT NULL,
	FOREIGN KEY(`PostID`) REFERENCES `Post`(`PostID`),
	PRIMARY KEY(`CommentID`),
	FOREIGN KEY(`Username`) REFERENCES `User`(`Username`)
);''')

conn.commit()
conn.close()

#Task 3.2
conn = sqlite3.connect('DataBase.db')

file = open('user.txt','r')
for line in file:
  line = line.strip()
  line = line.split(',')
  Username, Blocked = line[0],line[1]
  conn.execute('''INSERT INTO User(Username,Blocked)
Values(?,?)''',(Username, Blocked))

conn.commit()
file.close()

file = open('post.txt','r')
for line in file:
  line = line.strip()
  line = line.split(',')
  PostID, PostText, DateTimePosted, Username = line[0],line[1],line[2],line[3]
  conn.execute('''INSERT INTO Post(PostID, PostText, DateTimePosted, Username)
Values(?,?,?,?)''',(PostID, PostText, DateTimePosted, Username))

conn.commit()
file.close()

file = open('comment.txt','r')
for line in file:
  line = line.strip()
  line = line.split(',')
  CommentID, PostID, Username, TheText, DateTimeCommented = line[0],line[1],line[2],line[3],line[4]
  conn.execute('''INSERT INTO Comment(CommentID, PostID, Username, TheText, DateTimeCommented)
Values(?,?,?,?,?)''',(CommentID, PostID, Username, TheText, DateTimeCommented))

conn.commit()
file.close()

#Task 3.3

conn = sqlite3.connect('DataBase.db')
results = conn.execute('''SELECT User.Username,Comment.CommentID,Comment.DateTimeCommented,Comment.PostID,Comment.TheText FROM User,Comment
WHERE User.Username = Comment.Username and User.Blocked = 1;
''').fetchall()

conn.close()
for line in results:
  print(line)
