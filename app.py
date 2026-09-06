import os
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Demo hataya - hun real calculation
def analyze_and_treat(image_path, water_intake):
    # 1. Yaha pe tusi apna AI model lagaaoge
    # Filhal main sample logic de reha:
    base_score = 50
    if water_intake == "3-4L":
        base_score += 15
    elif water_intake == "1-2L":
        base_score -= 10
    
    # Image da size / brightness check karke score (demo logic di jagah)
    file_size = os.path.getsize(image_path)
    glow_score = min(95, base_score + (file_size % 20))
    
    return {
        "glow": glow_score,
        "hydration": "Low" if water_intake == "1-2L" else "Good",
        "acne": "High" if glow_score < 65 else "Low",
        "diet_plan": "Paani vadhao + Vitamin C" if glow_score < 70 else "Maintain karo",
        "challenge": "7 din lagataar photo pao"
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'before' not in request.files:
        return jsonify({"error": "Before photo nahi mili"}), 400
    
    file = request.files['before']
    water = request.form.get('water', '1-2L')
    
    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)
    
    result = analyze_and_treat(path, water)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
