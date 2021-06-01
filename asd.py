@app.route('/form')
def fomr():
    return render_template('form.html')


@app.route('/login', methods=['GET', 'POST'])
def action_page():
    if request.method == 'GET':
        return "로그인 중입니다 ... 잠시만 기다려 주세요"
    else:
        search = request.form['search']
        return '''당신은 '{}'로 검색을 했습니다<br> 
        결과를 보여드리겠습니다. 잠시만 기다려주세요
        '''.format(search)