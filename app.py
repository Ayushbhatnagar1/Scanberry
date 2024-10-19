from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load your trained ML model
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if 'file' not in request.files:
        return jsonify({'result': 'No file uploaded'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'result': 'No file selected'})

    # Save the uploaded image
    image_path = os.path.join('static', 'uploads', file.filename)
    file.save(image_path)

    # Use your ML model to make predictions
    # Replace the following line with your actual prediction logic
    prediction = model.predict([image_path])[0]

    return jsonify({'result': prediction, 'image_path': image_path})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

