import subprocess  # Add this import statement

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/execute-python-script', methods=['POST'])
def execute_python_script():
    script_path = request.json.get('script_path')
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    return jsonify({'output': result.stdout})

if __name__ == '__main__':
    app.run(debug=True)
