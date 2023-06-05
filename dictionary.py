import mysql.connector

db = mysql.connector.connect(
    user='ardit700_student',
    password='ardit700_student',
    host='108.167.140.122',
    database='ardit700_pmldatabase'
)
cursor = db.cursor()

word = input('Enter word: ')

query = cursor.execute('SELECT * FROM Dictionary WHERE Expretion=%s'%word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print('dosen\'t exist')
    