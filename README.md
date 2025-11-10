# 🏠 Simple House Price Predictor

This project is a **Simple House Price Predictor** built using **Flask** and **Machine Learning**.  
It estimates house prices in **Ethiopian Birr (ETB)** based on two main features:  
- Number of bedrooms  
- Total area

The model uses **Linear Regression** trained on **simulated housing data** to give users an approximate price estimate through a web interface.

---

## 💡 How It Works
- The app generates sample house data (with bedrooms, area and prices).  
- It trains a **Linear Regression** model from `scikit learn`.  
- When you enter the number of bedrooms and area it predicts the estimated price instantly.  
- Everything runs directly in a **Flask web app** with a minimal UI.

---

## 🧠 Tech Used
- **Python**  
- **Flask**  
- **NumPy**  
- **Scikit learn (Linear Regression)**  
- **HTML + CSS (for front end design)**

---

## 🎯 Purpose
This project was created as part of my **DevTech Internship Program** to explore how **machine learning models** can be integrated into **real-world web applications**.

---

## 🌍 Preview
Here’s what it does:
1. You enter the **number of bedrooms** and the **total area** (in sq ft).  
2. Click **Calculate Estimated Price**.  
3. It displays the predicted price in **ETB** instantly!

---

## ✨ Example
| Bedrooms | Area (sq ft) | Estimated Price (ETB) |
|-----------|---------------|------------------------|
| 3 | 2000 | 4,850,000 |
| 5 | 3500 | 7,200,000 |
| 10 | 7000 | 12,400,000 |

---

## 🙌 Acknowledgment
**DevTech Internship Program** 💻
