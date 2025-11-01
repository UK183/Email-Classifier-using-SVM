# 📧 Email Classification using SVM & Flask

An **end-to-end Machine Learning web application** that classifies emails as **Spam** or **Legitimate (Ham)** using a **Support Vector Machine (SVM)** model trained on real-world email data.  
Deployed via **Flask**, this project demonstrates the complete ML lifecycle — from text preprocessing and feature engineering to web-based deployment — delivering an interactive, explainable, and production-ready application.

---
<div align="center">
  <img src="images/Spam output1.PNG" width="70%"/>

</div>

## 🎯 Project Outcomes

- ✅ Achieved **over 98% accuracy** in classifying spam and legitimate emails.  
- ✅ Deployed an **interactive Flask web app** enabling real-time email spam detection.  
- ✅ Implemented **TF-IDF feature extraction** and **SVM optimization** for high-precision classification.  
- ✅ Designed an explainable interface showing **influential words and weights** driving predictions.  
- ✅ Enhanced user experience with a **“Get Detail”** feature and search filter to explore model insights.  

This project reflects skills in **data preprocessing, feature engineering, model evaluation, and Flask deployment**, aligning directly with Data Science and Machine Learning engineering roles.

---

## 🧠 Technical Stack

- **Programming Language:** Python  
- **Frameworks:** Flask, Scikit-learn  
- **ML Algorithm:** Support Vector Machine (SVM)  
- **Feature Extraction:** TF-IDF Vectorizer  
- **Libraries:** NumPy, Pandas, Joblib  
- **Frontend:** HTML, CSS, JavaScript  

---

## 📊 Project Workflow

1. **Data Preprocessing**  
   - Cleaned and normalized email text (lowercasing, punctuation & digit removal).  
   - Converted textual data into numerical vectors using **TF-IDF**.  

2. **Model Building**  
   - Trained an **SVM classifier** for binary text classification.  
   - Tuned parameters using **GridSearchCV** for optimal accuracy.  

3. **Model Evaluation**  
   - Evaluated using confusion matrix, precision, recall, F1-score, and accuracy metrics.  
   - Ensured balanced performance across both spam and ham categories.  

4. **Deployment**  
   - Integrated the trained model with a **Flask web interface**.  
   - Enabled real-time predictions and model interpretability features.

---

## 💡 Real-World Application

This solution can be extended to:
- 📬 Enterprise email security systems  
- 🔎 Phishing or fraud detection platforms  
- 💬 Chat moderation and text classification tools
  
---

## 📊 Project Flow

**Data Importing →** Load dataset (`spam.csv`) and clean unnecessary columns  
**Preprocessing →** Apply label encoding, remove duplicates, and perform basic text cleaning (lowercase, punctuation removal)  
**EDA →** Visualize spam vs ham distribution and analyze message length patterns  
**Vectorization →** Convert text data into numerical features using **CountVectorizer**  
**TF-IDF Transformation →** Reweight words based on their importance and frequency  
**SVM Model →** Train a **Support Vector Machine** classifier for spam detection  
**Evaluation →** Measure model performance using accuracy, confusion matrix, and classification report  
**Prediction →** Test the model on new email examples through an interactive **Flask web app**

---


## 🧩 Folder Structure
Email_Classifier_SVM/

│

├── app.py

├── model.pkl

├── vector.pkl

├── tf.pkl

├──index.html

├── style.css

└── requirements.txt



---

## ⚙️ How to Run

```bash
git clone https://github.com/<your-username>/Email-Classifier-using-SVM.git
cd Email-Classifier-using-SVM

python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
python app.py
```
Then open your browser at 👉 http://127.0.0.1:5000

## 📈 Example Predictions

| 📧 **Input Email** | 🧠 **Predicted Output** |
|--------------------|------------------------|
| "Congratulations! You’ve won a free iPhone. Click here to claim now!" | 🚫 **Spam Email** |
| "Team meeting scheduled at 10 AM tomorrow." | ✅ **Legitimate (Ham)** |
| "Get 50% off on all products! Limited time offer." | 🚫 **Spam Email** |
| "Your invoice for the last month is attached below." | ✅ **Legitimate (Ham)** |
| "Win cash rewards by completing this short survey!" | 🚫 **Spam Email** |



## 🏆 Key Achievements & Skills Demonstrated
- End-to-End ML Pipeline: Data preprocessing → model training → deployment 
- Text Analytics:Text Preprocessing & Feature extraction via CountVectorizer & TF-IDF  
- Model Optimization: Hyperparameter tuning with GridSearchCV
- Web Deployment: Flask integration and UI development
- Explainable AI (XAI): Display of top influential words for transparency
- Full-Stack ML Project Execution: From dataset to live application











