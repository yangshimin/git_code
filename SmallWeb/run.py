from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate, MigrateCommand
import os
from flask_script import Manager
from flask_moment import Moment
from flask_bootstrap import Bootstrap

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


db = SQLAlchemy(app)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
migrate = Migrate(app, db)
moment = Moment(app)
bootstrap = Bootstrap(app)


class PostForm(Form):
    name = StringField(u'用户名:', validators=[DataRequired(message=u'用户名不能为空')])
    text = TextAreaField(u'内容:', validators=[DataRequired(message=u'内容不能为空')])
    submit = SubmitField(u'提交')


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    text = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(name=form.name.data, text=form.text.data)
        db.session.add(post)
        flash(u'留言成功')
        return redirect(url_for('index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', form=form, posts=posts)


if __name__ == '__main__':
    manager.run()
