from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/naver')
def hello():
    return render_template('naver.html')

@app.route('/')
def joro():
    return render_template("html.html")

@app.route('/naver')
def naver():
    return '안녕 나는 네이버야~'


     

if __name__ == '__main__':
    app.run()