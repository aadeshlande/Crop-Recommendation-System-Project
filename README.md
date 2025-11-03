---

# 🌱 ML-Based Crop Recommendation System

A smart web application that recommends the **most suitable crop** to grow based on soil and climate conditions using **Machine Learning**. Built with **Django** for the backend and a simple, responsive **HTML/CSS frontend**.

---

## 🔹 Features

* Predicts **optimal crop** based on soil nutrients and weather.
* Takes **7 parameters** as input:

  * Nitrogen (N), Phosphorus (P), Potassium (K)
  * Temperature (°C), Humidity (%), pH, Rainfall (mm)
* **Lightweight ML model** for fast predictions.
* Fully **integrated frontend and backend**.
* Deployed on **AWS EC2**.

---

## 🛠 Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS
* **Machine Learning:** Scikit-learn, Pandas
* **Deployment:** AWS EC2

---

## 🚀 Getting Started (Run on your local machine)

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/AtharvaSagane/ML-Based-Crop-Recommendation-System.git
cd ML-Based-Crop-Recommendation-System/backend
```

### **2️⃣ Setup Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not present:

```bash
pip install django pandas scikit-learn
```

### **4️⃣ Run the Server**

```bash
python manage.py runserver
```

* Open your browser at `http://127.0.0.1:8000/` (or your server IP if on EC2).

---
<img width="1920" height="1080" alt="Screenshot (157)" src="https://github.com/user-attachments/assets/ac6c95d7-2847-431a-9d3f-77eb6a3e84fa" />

## 🧪 Example Inputs

| N  | P  | K  | Temperature | Humidity | pH  | Rainfall | Prediction |
| -- | -- | -- | ----------- | -------- | --- | -------- | ---------- |
| 90 | 42 | 43 | 20.8        | 82       | 6.5 | 200      | Rice       |
| 80 | 35 | 40 | 25.0        | 70       | 6.8 | 150      | Coffee     |
| 50 | 40 | 30 | 28.0        | 60       | 6.0 | 120      | Mango      |

---

## 📝 Project Structure

```
ML-Based-Crop-Recommendation-System/
├── backend/
│   ├── CropModel.sav           # Trained ML model
│   ├── label_CropModel.sav     # Label encoder
│   ├── manage.py
│   ├── settings.py
│   └── views.py
├── templates/
│   └── index.html
└── README.md
```

---

## 📦 Future Enhancements

* Deploy with **Gunicorn + Nginx** for production.
* Use **PostgreSQL** instead of SQLite.
* Add **user authentication** to save crop recommendations.
* Expand dataset to **support more crops and conditions**.

---

## ⚡ Author

**Atharva Sagane**

* GitHub: [github.com/AtharvaSagane](https://github.com/AtharvaSagane)
* Passionate about **ML + Web Development + Competitive Programming**.

