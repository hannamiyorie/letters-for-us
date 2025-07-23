from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Message
import os
from dotenv import load_dotenv

print("mencoba memuat file .env...")
load_dotenv()

print("isi DATABASE_URL:", os.environ.get('DATABASE_URL'))

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/api/messages', methods=['GET', 'POST'])
def handle_messages():
    if request.method == 'POST':
        data = request.get_json()
        if not data or not data.get('name') or not data.get('content'):
            return jsonify({"error": "Nama dan pesan tidak boleh kosong"}), 400

        new_message = Message(
            name=data.get('name'),
            content=data.get('content')
        )
        db.session.add(new_message)
        db.session.commit()
        return jsonify(new_message.to_dict()), 201

    else:
        messages = Message.query.order_by(Message.created_at.desc()).all()
        messages_list = [message.to_dict() for message in messages]
        return jsonify(messages_list)
    
    new_message = Message(
        name=data.get('name'),
        content=data.get('content')
    )
    db.session.add(new_message)
    db.session.commit()
    
    return jsonify(new_message.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)