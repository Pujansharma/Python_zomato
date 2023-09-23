from flask_wtf import FlaskForm
from wtforms import  IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, NumberRange, Length

class OrderForm(FlaskForm):
    dish_id = SelectField('Dish', coerce=int, validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    # You can add more fields as needed for the order form

class ReviewForm(FlaskForm):
    rating = SelectField('Rating', coerce=int, validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[Length(max=255)])
    # You can add more fields as needed for the review form
