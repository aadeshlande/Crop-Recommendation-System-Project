from django.shortcuts import render
import os
import pickle
import pandas as pd

def home(request):
    return render(request,'index.html')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, 'backend', 'CropModel.sav')
le_path = os.path.join(BASE_DIR, 'backend', 'label_CropModel.sav')

model = pickle.load(open(model_path,'rb'))
le = pickle.load(open(le_path,'rb'))

def recommend_crop(N, P, K, temperature, humidity, ph, rainfall):
    df = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                      columns=['N','P','K','temperature','humidity','ph','rainfall'])
    pred_label = model.predict(df)[0]
    predicted_crop = le.inverse_transform([pred_label])[0]
    return predicted_crop.capitalize()

def predict(request):
    if request.method == 'POST':
        N = float(request.POST['N'])
        P = float(request.POST['P'])
        K = float(request.POST['K'])
        temperature = float(request.POST['temperature'])
        humidity = float(request.POST['humidity'])
        ph = float(request.POST['ph'])
        rainfall = float(request.POST['rainfall'])

        prediction_text = recommend_crop(N, P, K, temperature, humidity, ph, rainfall)

        return render(request, 'index.html', {'prediction_text': prediction_text})
    else:
        return render(request, 'index.html')

