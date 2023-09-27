from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, SelectField, IntegerField
from wtforms.validators import InputRequired

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']
teams = ['Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka']
class Input(FlaskForm):
    battig_team = SelectField("Batting Team",validators=[InputRequired()] ,choices=[(val,val) for val in teams]) 
    bowling_team = SelectField("Bowling Team",validators=[InputRequired()] ,choices=[(val,val) for val in teams]) 
    city = SelectField("City Name", validators=[InputRequired()], choices=[(val,val) for val in cities])
    currentscore = IntegerField("Current Score", validators=[InputRequired()])
    overs = FloatField("Overs done(works for over>5)", validators=[InputRequired()])
    Wickets = IntegerField("Wickets out)", validators=[InputRequired()])
    last_five = IntegerField("Runs scored in last 5 overs)", validators=[InputRequired()])

    submit = SubmitField("Predicted Score")
    
    


