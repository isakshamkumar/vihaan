import os
import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/execute-python-script', methods=['POST'])
def execute_python_script():
    script_path = request.json.get('script_path')
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    return jsonify({'output': result.stdout})

@app.route('/handle_user_input', methods=['POST'])
def handle_user_input():
    print("called")
    data = request.json.get('user_input')
    file_name = os.path.join(os.path.dirname(__file__), 'script.py')
    try:
        with open(file_name, 'w') as f:
            f.write(data)
        return jsonify({'message': 'Python script created successfully', 'file_path': file_name})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
