from flask import Flask, render_template,url_for, redirect 
from formmodul import Input
from model import get_prediction
app = Flask(__name__)
app.config["SECRET_KEY"] = 'thisisasecreatkey'

@app.route('/', methods = ['GET','POST'])
def home():
    predicted_score = 0
    form = Input()
    if form.validate_on_submit():
        input = {"batting_team":form.battig_team.data,"bowlling_team":form.bowling_team.data,"city":form.city.data,
                 "current_score":form.currentscore.data,"wickets":form.Wickets.data,
                 "run_last_five":form.last_five.data,"overs":form.overs.data}
        predicted_score = get_prediction(input)
        return  render_template("index.html",form=form, predicted_score=int(predicted_score))

    return render_template("index.html",form=form, predicted_score=int(predicted_score))

if __name__=="__main__":
    app.run(debug = True)
