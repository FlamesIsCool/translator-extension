from flask import Flask, request, jsonify
from flask_cors import CORS
from deep_translator import GoogleTranslator
import os

app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get("text")
    target = data.get("target", "en")
    try:
        translated = GoogleTranslator(source='auto', target=target).translate(text)
        return jsonify({'translated': translated})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
