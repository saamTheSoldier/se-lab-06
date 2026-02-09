"""
RESTful API با عملیات CRUD ساده - معماری Microservice
"""
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# تنظیمات پایگاه داده مشترک (SQLite برای پایداری بدون نیاز به pull تصویر)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'sqlite:////data/microservice.db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Item(db.Model):
    """مدل ساده برای عملیات CRUD"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


@app.route('/health', methods=['GET'])
def health():
    """بررسی سلامت سرویس"""
    return jsonify({'status': 'ok', 'service': 'backend'})


@app.route('/api/items', methods=['GET'])
def get_items():
    """دریافت لیست همه آیتم‌ها"""
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])


@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """دریافت یک آیتم با شناسه"""
    item = Item.query.get_or_404(item_id)
    return jsonify(item.to_dict())


@app.route('/api/items', methods=['POST'])
def create_item():
    """ایجاد آیتم جدید"""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'name is required'}), 400
    
    item = Item(
        name=data['name'],
        description=data.get('description', '')
    )
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201


@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """بروزرسانی آیتم"""
    item = Item.query.get_or_404(item_id)
    data = request.get_json()
    
    if data.get('name'):
        item.name = data['name']
    if 'description' in data:
        item.description = data['description']
    
    db.session.commit()
    return jsonify(item.to_dict())


@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """حذف آیتم"""
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return '', 204


with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        if "already exists" not in str(e):
            raise


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
