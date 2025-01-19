from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 模拟用户数据
users = {
    "user1": "admin",
    "user2": "123"
}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        return redirect(url_for('success_page', username=username))
    else:
        return "登录失败，用户名或密码错误", 401

@app.route('/success/<username>')
def success_page(username):
    return render_template('success.html', username=username)

@app.route('/pag')
def pag_page():
    return render_template('pag.html')

if __name__ == '__main__':
    app.run(debug=True)


