import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_CHECK_DEFAULT'] = False
db = SQLAlchemy(app)

@app.route('/')
def status():
    
    current_conf = str(app.config['DEBUG'])
    return jsonify({'debug_status': current_conf})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
