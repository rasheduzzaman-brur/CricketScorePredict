import pickle
import pandas as pd
import xgboost
from xgboost import XGBRegressor

model = pickle.load(open('model/model.pkl','rb'))

def get_prediction(input):
    balls_left = 120 - (input["overs"]*6)
    wickets_left = 10 -input["wickets"]
    crr = input["current_score"]/input["overs"]

    input_df = pd.DataFrame(
     {'batting_team': [input["batting_team"]], 'bowling_team': [input["bowlling_team"]],'city':input["city"], 
      'current_score': [input["current_score"]],'balls_left': [balls_left], 'wickets_left': [wickets_left], 'crr': [crr], 'last_five': [input["run_last_five"]]})
    result = model.predict(input_df)
    return result[0]