from flask import Flask, jsonify,json,request
import pyodbc
#from flask import Flask
from flask import jsonify, request, Response
#from flask_mysqldb import MySQL




api = Flask(__name__)
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-7DL0DAA\SQLEXPRESS;"
    "Database=attendancedb;"
    "UID=zoraiz;"
    "PWD=123456;"
    "Trusted_Connection=yes;"
)






@api.route('/AllStudent', methods=['GET','POST'])
def getAllStudent():
    cursor = conn.cursor()
    l={}
    cursor.execute("select * from EMPMTR")
    for row in cursor:
       l['Reg']=row[0]
       l['First Name']=row[1]

    for row in cursor:
        print(row)

    return jsonify(l)


if __name__ == '_main_':
    api.run(debug=True)