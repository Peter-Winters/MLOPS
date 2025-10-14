from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import os

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

# paths
model_path = 'artifacts/model.pkl'
preprocessor_path = 'artifacts/preprocessor.pkl'

application=Flask(__name__)

## Route for a home page

@application.route('/')
def index():
    return render_template('index.html') 

@application.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            writing_score=float(request.form.get('reading_score')),
            reading_score=float(request.form.get('writing_score')))
        
        pred_df=data.get_data_as_dataframe()
        print(pred_df)
        
        predict_pipeline=PredictPipeline(model_path=model_path,preprocessor_path=preprocessor_path)
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])
    
    

if __name__=="__main__":     
    port = int(os.environ.get("PORT", 8000)) 
    application.run(host="0.0.0.0",port=port, debug=False)   