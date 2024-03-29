from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = StringField(label='Password', validators=[DataRequired()])
    name = StringField(label='Name', validators=[DataRequired()])
    submit = SubmitField(label="Sign Up!")


# TODO: Create a LoginForm to login existing users

class LogInForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = StringField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment_body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField(label='Submit Comment')
