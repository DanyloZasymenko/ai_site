from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, SelectField, MultipleFileField, IntegerField, \
    PasswordField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from wtforms_sqlalchemy.fields import QuerySelectField

from ai_site.models.news import news_category_query
from ai_site.models.project import Years, Semesters


class CallbackForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone number', validators=[DataRequired(), Length(min=10, max=22)])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Leave callback')


class HistoryForm(FlaskForm):
    header = StringField('Header', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    date = DateField('Date')
    image = FileField('Choose image', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add')


class PartnerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=50)])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = FileField('Choose image', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add')


class NewsForm(FlaskForm):
    header = StringField('Header', validators=[DataRequired(), Length(min=1, max=70)])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = FileField('Choose image', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
    text = TextAreaField('Text', validators=[DataRequired()])
    category = QuerySelectField('Choose category', validators=[DataRequired()],
                                query_factory=news_category_query, allow_blank=False, get_label='name')
    submit = SubmitField('Add')


class NewsCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=30)])
    submit = SubmitField('Add')


class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=70)])
    image = FileField('Choose image', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
    description = TextAreaField('Description', validators=[DataRequired()])
    authors = TextAreaField('Authors', validators=[DataRequired(), Length(min=1, max=180)])
    url = StringField('Url', validators=[DataRequired(), Length(min=1, max=70)])
    year = SelectField('Year', choices=[(e.name, e.value) for e in Years], validators=[DataRequired()])
    semester = SelectField('Semester', choices=[(e.name, e.value) for e in Semesters], validators=[DataRequired()])
    pictures = MultipleFileField('Choose pictures')
    submit = SubmitField('Add')


class PageForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=30)])
    submit = SubmitField('Add')


class PageTextForm(FlaskForm):
    primary_text = TextAreaField('Primary Text')
    image = FileField('Choose image', validators=[FileAllowed(['jpg', 'png', 'gif'])])
    secondary_text = TextAreaField('Secondary Text')
    position = IntegerField('Position on page', validators=[NumberRange(min=0), DataRequired()])
    submit = SubmitField('Add')


class TeacherForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=70)])
    position = StringField('Position', validators=[DataRequired(), Length(min=1, max=50)])
    link = StringField('Link', validators=[Length(min=0, max=70)])
    incumbency = StringField('Incumbency', validators=[DataRequired(), Length(min=1, max=50)])
    description = TextAreaField('Description')
    interests = TextAreaField('Interests')
    research_directions = TextAreaField('Research directions')
    hobby = StringField('Hobby', validators=[Length(min=0, max=50)])
    image = FileField('Choose image', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
    scopus_id = StringField('Scopus ID', validators=[Length(min=0, max=11)])
    scholar_id = StringField('Scholar ID', validators=[Length(min=0, max=12)])
    submit = SubmitField('Add')


class CourseForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    credits = IntegerField('Credits', validators=[NumberRange(min=0), DataRequired()])
    year = SelectField('Year', choices=[(e.name, e.value) for e in Years], validators=[DataRequired()])
    semester = SelectField('Semester', choices=[(e.name, e.value) for e in Semesters], validators=[DataRequired()])
    submit = SubmitField('Add')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign Up')
