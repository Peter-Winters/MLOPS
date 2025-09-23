from flask import Flask, request, render_template
import numpy as np
import pickle
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

application = Flask(__name__)

## route for homepage
@application.route('/')
def index():
    return render_template('index.html')

@application.route('/predict', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            # Retrieving form data
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),  
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )
            
            # convert to dataframe
            pred_df = data.get_data_as_dataframe()
            print(pred_df)

            # prediction
            predict_pipeline = PredictPipeline(
                model_path='artifacts/model.pkl',
                preprocessor_path='artifacts/preprocessor.pkl')
            results = predict_pipeline.predict(pred_df)

            return render_template('home.html', results=results[0])

        except Exception as e:
            print(e)
            return render_template('home.html', error=str(e))
    else:
        return render_template('home.html')
    

if __name__ == "__main__":
    application.run(host='0.0.0.0')