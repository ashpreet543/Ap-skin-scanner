import os
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def analyze_and_treat(image_path, water_intake):
    # REAL ANALYSIS - Photo nu sach ch padhna
    try:
        img = Image.open(image_path).convert('RGB')
        img = img.resize((100, 100)) # chota karke fast analysis
        img_array = np.array(img)
        
        # 1. Brightness -> Glow
        brightness = np.mean(img_array) # 0-255
        # 0-255 nu 30-85 ch convert
        base_score = int((brightness / 255) * 55) + 30

        # 2. Water intake da asar
        if water_intake == "3-4L":
            base_score += 15
        elif water_intake == "1-2L":
            base_score -= 12
        
        glow_score = min(95, max(15, base_score))

        # 3. Hydration - sirf paani te
        if water_intake == "3-4L":
            hydration = "Excellent"
        elif water_intake == "2-3L":
            hydration = "Good"
        else:
            hydration = "Low"

        # 4. Acne - Photo di texture (std dev) naal
        # Jey photo ch zyada dark/light farak hai, ta acne/texture zyada
        std_dev = np.std(img_array)
        if std_dev > 55:
            acne = "High - Texture visible"
        elif std_dev > 35:
            acne = "Medium"
        else:
            acne = "Low - Clear Skin"

        # 5. Diet plan
        if glow_score < 60:
            diet_plan = "Paani 3-4L, Vitamin C (Santra), 8 ghante neend"
        elif glow_score < 80:
            diet_plan = "Maintain karo, haldi wala doodh + paani"
        else:
            diet_plan = "Perfect! Same diet continue rakho"

        return {
            "glow": glow_score,
            "hydration": hydration,
            "acne": acne,
            "diet_plan": diet_plan,
            "challenge": "7 din lagataar photo pao - Result dekho!"
        }
    except Exception as e:
        return {
            "glow": 50,
            "hydration": "Good",
            "acne": "Low",
            "diet_plan": "Error: " + str(e),
            "challenge": "Dobara try karo"
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
