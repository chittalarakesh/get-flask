from flask import Flask ,redirect ,url_for

app=Flask(__name__)


 
def admin():
    return "this is admin"
 
def employe():
    return "this is the employee"


app.add_url_rule('/admin', 'admins' ,admin)




if __name__ == '__main__':
    app.run(debug=True)


 