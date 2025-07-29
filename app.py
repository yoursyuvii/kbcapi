import json
from flask import Flask, jsonify
import random

# Flask app ऑब्जेक्ट बनाएं
app = Flask(__name__)

# JSON फाइल से प्रश्न लोड करें
def load_questions():
    with open('questions.json', 'r', encoding='utf-8') as f:
        return json.load(f)

questions = load_questions()

@app.route('/')
def home():
    return "<h1>KBC Questions API</h1><p>Welcome! Use /api/questions/random to get a random question.</p>"

# एक रैंडम प्रश्न पाने के लिए एंडपॉइंट
@app.route('/api/questions/random', methods=['GET'])
def get_random_question():
    random_question = random.choice(questions)
    return jsonify(random_question)

# ID के द्वारा एक प्रश्न पाने के लिए एंडपॉइंट
@app.route('/api/questions/<int:question_id>', methods=['GET'])
def get_question_by_id(question_id):
    question = next((q for q in questions if q['id'] == question_id), None)
    if question:
        return jsonify(question)
    else:
        return jsonify({"error": "Question not found"}), 404

# ऐप को चलाने के लिए मेन ब्लॉक
if __name__ == '__main__':
    app.run(debug=True)