from flask import Flask, request, render_template
import joblib

# Load model and vectorizers
model = joblib.load('model.pkl')
vectorizer = joblib.load('vector.pkl')
tfidf = joblib.load('tf.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    data = [message]

    # Transform the input text
    vect = vectorizer.transform(data)
    tfidf_data = tfidf.transform(vect)

    # Get prediction and confidence
    prediction = model.predict(tfidf_data)[0]
    #probabilities = model.predict_proba(tfidf_data)[0]
    #confidence = round(max(probabilities) * 100, 2)

    # Identify important words
    feature_names = vectorizer.get_feature_names_out()
    word_weights = tfidf_data.toarray()[0]
    top_indices = word_weights.argsort()[-5:][::-1]   # top 5 words
    top_words = [(feature_names[i], round(word_weights[i], 4)) for i in top_indices if word_weights[i] > 0]

    # Format output
    if prediction == 1:
        result = f"🚫 Spam Email "
        
    else:
        result = f"✅ Legitimate (Ham) "

    return render_template('index.html', prediction=result, top_words=top_words)

if __name__ == '__main__':
    app.run(debug=True)
