from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import logging


from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

logging.basicConfig(level=logging.INFO)

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
        try:
            data=CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )
            
            pred_df=data.get_data_as_data_frame()
            application.logger.info("Prediction input DataFrame created successfully.")

            predict_pipeline=PredictPipeline()
            results=predict_pipeline.predict(pred_df)
            application.logger.info(f"Prediction successful. Result: {results[0]}")
            
            return render_template('home.html',results=results[0])

        except Exception as e:
            application.logger.error("An error occurred during prediction: %s", e, exc_info=True)
            return render_template('home.html', error="An error occurred. Please check the logs.")


if __name__=="__main__":       
    application.run(host='0.0.0.0', port=8000)    
