from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
cors=CORS(app)
model=pickle.load(open('LinearRegressionModel.pkl','rb'))
car=pd.read_csv("Cars24_Cleaned.csv")

@app.route('/')
def index():
    city=sorted(car['City'].unique())
    year=sorted(car['Year'].unique(), reverse=True)
    companies=sorted(car['Brand'].unique())
    car_models=sorted(car['Car Name'].unique())
    car_trans=car['Car model'].unique()
    owner=sorted(car['Owner'].unique())
    car_type=car['Car Type'].unique()
    city.insert(0,"Select City")
    year.insert(0, "Select Year ")
    companies.insert(0, "Select Brand ")



    return render_template('index.html', city=city, years=year, companies=companies,car_models=car_models, car_trans=car_trans, owner=owner, car_type=car_type)


@app.route('/predict', methods=['POST'])
def predict():

    City=request.form.get('city')
    Year=request.form.get('year')
    Brand=request.form.get('company')
    Car_Name=request.form.get('car_models')
    Car_Model =request.form.get('car_tran')
    Car_km=request.form.get('kilo_driven')
    Owner =request.form.get('owner')
    Car_Type = request.form.get('car_type')

    print(City,Year,Brand,Car_Name,Car_Model,Car_km,Owner,Car_Type)

    prediction=model.predict(pd.DataFrame([[City,Year,Brand,Car_Name,Car_Model,Car_km,Owner,Car_Type]],columns=['City','Year','Brand','Car Name','Car model','Car km','Owner','Car Type']))
    print(prediction)

    return str(np.round(prediction[0],2))
if __name__=="__main__":
    app.run()


