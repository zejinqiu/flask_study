from flask import Flask
from flask import session, escape, request, url_for, redirect

app = Flask(__name__)


# @app.route("/")
# def index():
#     return "hello world"

# 使用session
# 第一步，设置session密钥
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# 第二步，设置session
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session["username"] = request.form["username"]
        return redirect(url_for("home"))
    else:
        return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

# 第三步，获取session
@app.route("/")
def home():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

# 删除session
@app.route("/logout", methods=['GET'])
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run()
