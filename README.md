# Car Price Prediction End-to-End-Machine-Learning-Project Using Cars24 Web-Scarpped data

### Project Link:- https://ml-carpriceprediction-api.herokuapp.com/
(Link might not work because Heroku is not free anymore)
## Introduction:-

This project is based on cars data from [Cars24](https://www.cars24.com/) which is a place for buyers and sellers for cars across India. Do you ever think to sell your car but you are unsure about the prices.? It might me any city or any brand of car. So we have got a solution for you, by using the technique of **Machine Learning** we can predict best price for your Car.

As the title suggests this is an end-to-end project, let me explain how and which are those stages ?

![image](https://user-images.githubusercontent.com/99324199/177263229-4b66b842-3d7f-4f63-a525-99123f934373.png)

## Lifecycle Of Project:-

### 1:- Collecting Data:-

This involves the process of collecting data from different sources such as any car selling website such as [Cars24](https://www.cars24.com/) , which has records of various cars available. For this I've used Web Scrapping i.e I have extracted car's data from the website. Once you write the code you can use it repeatedly after specific intervals for updated data, it makes the the data collection part hassle free. The tools I've used are **Beautiful Soup** & **Selenium**. You can find The code and data for the same here [Web Scrapping of Cars24](https://github.com/MalharJ21/Car_Price_Prediction/tree/main/Web%20Scrapping%20of%20Cars24)

### 2:- EDA & Modeling:-

This phase involves data cleaning, performing analysis on this dataset and plotting different visualizations. In data cleaning, What I've done is dropped the null values, extracted valuable information from car's data, converting values from different units to same unit & put all these cleaned data into a separate csv file for serving as a source for next stage i.e Modeling [Cars24 Cleaned-CSV](https://github.com/MalharJ21/Car_Price_Prediction/blob/main/Cars24_Cleaned.csv). And I have also performed EDA on analysis on this dataset and plotted different visualizations, For example, If you have a question how many cars are on Manual Transmission and Automatic Transmission we can get pie chart with number of percentage for respective transmission present. After comes building ML models which trains on this dataset and helps us predict prices of properties which it has not seen before [EDA & Modeling](https://github.com/MalharJ21/Car_Price_Prediction/blob/main/EDA_%26_Modeling_Cars24.ipynb).
  
  ### 3:- Creating a Web Frame-work using Flask  

This phase involves creating a web frame-work using flask [application.py](https://github.com/MalharJ21/Car_Price_Prediction/blob/main/application.py) here you can find the code for the same. I have created a simple UI where user can easily access and make predictions.

### 4:- Deployment
The final stage of the project includes deploying the project live on the internet, which others can use whenever and wherever they want. For hosting my project I've used Heroku as the platform and designed a simple UI with the help of HTML & CSS and Flask as the backend framework. I would love if you try and play around with this making some predictions. Here is the link [Car Price Prediction](https://ml-carpriceprediction-api.herokuapp.com/).



Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/malhar-jadhav-b2a421213/) for any feedback you have.
