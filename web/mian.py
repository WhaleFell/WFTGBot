from flask import Flask, request, redirect, render_template, url_for
from web import filepath
from app import CONF
from pathlib import Path
from app.utils.log import logger
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
login_manager = LoginManager()


server = Flask(__name__)
server.config['SECRET_KEY'] = CONF.Web.SECRET_KEY

login_manager.init_app(server)
login_manager.login_view = 'login'  # 设置登陆视图

logger.info("flask update path:%s" % filepath)


class User(UserMixin):
    def __init__(self, id) -> None:
        self.id = id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@server.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = None

        if CONF.Web.username == username and CONF.Web.password == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('upload_file'))
        else:
            return 'Invalid username or password'

    return render_template('login.html', conf=CONF)


@server.route('/', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(str(Path(filepath)))
            logger.success(f"文件上传成功并保存为 {filepath}")
            return f"文件上传成功并保存为 {filepath}"
    return '''
    <h1>当前管理的机器人:%s</h1>
    <h1>上传文件</h1>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="上传">
    </form>
    ''' % CONF.name
