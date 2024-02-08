from flask import Flask ,redirect,url_for,render_template,request


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login',methods=['GET'])
def login():
    username=request.args.get("username")
    if username=="Rakesh":
        return "Welcome"
    else:
        return "invalid"
 

 

if __name__ == '__main__':
    app.run(debug=True,port=5001)


 