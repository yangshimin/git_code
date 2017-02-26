import os
from flask import Flask, render_template, url_for, request, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_script import Manager
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'a hard guess string'
app.config['UPLOADED_IMGS_DEST'] = './upload_file'
manager = Manager(app)

imgs = UploadSet('imgs', IMAGES)
configure_uploads(app, imgs)
patch_request_class(app, 32 * 1024 * 1024)


class UploadFile(FlaskForm):
    upfile = FileField(validators=[FileRequired(u'必须选择上传文件'), FileAllowed(imgs, u'只能选择图片')])
    submit = SubmitField(u'上传')


@app.route('/', methods=['POST', 'GET'])
def index():
    form = UploadFile()
    if form.validate_on_submit():
        filelist = request.files.getlist('upfile')
        for file in filelist:
            imgs.save(file)
    return render_template('index.html', form=form)


@app.route('/managefile')
def managefile():
    imglists = os.listdir(app.config['UPLOADED_IMGS_DEST'])
    return render_template('manage.html', imglists=imglists)


@app.route('/show/<file>')
def show(file):
    file_url = imgs.url(file)
    return render_template('show.html', file_url=file_url)


@app.route('/delete/<file>')
def delete(file):
    path = imgs.path(file)
    os.remove(path)
    return redirect(url_for('managefile'))


if __name__ == '__main__':
    manager.run()
