from flask import Flask, request, render_template
from func import ck_idpw # 내가만든 ip pw 체크 함수
app = Flask(__name__)

@app.route('/')
def joro():
    return render_template("login.html")

@app.route('/naver')
def naver():
    return '안녕 나는 네이버야~'

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
        return '회원가입 성공!@'

@app.route('/login' ,methods =['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else :
        userid = request.form['userid']
        pwd = request.form['pwd']
        print(userid, pwd) 
        return '로그인 성공!'


     

if __name__ == '__main__':
    app.run()