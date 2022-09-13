from socketserver import DatagramRequestHandler
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


# User Register
class UserCreateForm(FlaskForm):
    name = StringField('사용자 이름', validators=[DataRequired(), Length(min=2, max=20)])
    user_id = StringField('사용자 ID', validators=[DataRequired(), Length(min=4, max=10)])
    password = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password_confirm', '비밀번호가 일치하지 않습니다')])
    password_confirm = PasswordField('비밀번호 확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])