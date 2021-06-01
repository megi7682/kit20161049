from flask import Flask, request, render_template, session, redirect
from func import ck_idpw # 내가만든 ip pw 체크 함수
import db

app = Flask(__name__)
app.secret_key = b'aaa!111/'

@app.route('/')
def joro():
    return render_template("html.html")

@app.route('/form')
def asd():
    return render_template("form.html")

@app.route('/coin')
def coin():
    if 'user' in session:
        return '여기는 코인 거래소 !'
    else :
        return redirect('/login')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/join_action', methods=['GET', 'POST'])
def join_action():
    if request.method == 'GET':
        return "로그인 중입니다 ... 잠시만 기다려 주세요"
    else:
        userid = request.form['userid']
        pwd = request.form['pwd']
        name = request.form['name']
        phone = request.form['phone']
        print(userid, pwd, name, phone)
        db.insert_user(userid, pwd , name, phone)
        return '회원가입 성공!@'

@app.route('/login' ,methods =['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else :
        id = request.form['userid']
        pw = request.form['pwd']
        print(id, pw) 
        ret = db.get_idpw(id,pw)
        if ret != None:
            session['user'] = ret[3]
        return ck_idpw(ret)


@app.route('/join2')
def join2():
    return render_template('join2.html')

if __name__ == '__main__':
    app.run() 