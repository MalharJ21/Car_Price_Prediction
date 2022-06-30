from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)

model=pickle.load(open('LinearRegressionModel.pkl','rb'))
car=pd.read_csv("New_df.csv")

@app.route('/')
def index():
    city=sorted(car['City'].unique())
    year=sorted(car['Year'].unique(), reverse=True)
    brand=sorted(car['Brand'].unique())
    car_name=sorted(car['Car Name'].unique())
    car_model=car['Car model'].unique()
    owner=sorted(car['Owner'].unique())
    car_type=car['Car Type'].unique()
    city.insert(0,"Select City")
    year.insert(0, "Select Year ")
    brand.insert(0, "Select Brand ")



    return render_template('index.html', city=city, years=year, brand=brand, car_name=car_name, car_model=car_model, owner=owner, car_type=car_type)


@app.route('/predict', methods=['POST'])
def predict():

    City=request.form.get('city')
    Year=int(request.form.get('year'))
    Brand=request.form.get('brand')
    Car_Name=request.form.get('car_name')
    Car_Model = request.form.get('car_model')
    Car_km=int(request.form.get('kilo_driven'))
    Owner =int(request.form.get('owner'))
    Car_Type = request.form.get('car_type')

    print(City,Year,Brand,Car_Name,Car_Model,Car_km,Owner,Car_Type)

    prediction=model.predict(pd.DataFrame([[City,Year,Brand,Car_Name,Car_Model,Car_km,Owner,Car_Type]],columns=['City','Year','Brand','Car Name','Car model','Car km','Owner','Car Type']))
    print(prediction)

    return str(np.round(prediction[0],2))
if __name__=="__main__":
    app.run()


