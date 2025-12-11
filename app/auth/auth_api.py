from flask import jsonify, request
from app.auth import auth
from app.models import User

@auth.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing email or password'}), 400
    
    user = User.query.filter_by(email=data.get('email')).first()
    if user and user.check_password(data.get('password')):
        return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
        # In a real API, return a JWT token here
    
    return jsonify({'message': 'Invalid credentials'}), 401

@auth.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing data'}), 400
        
    if User.query.filter_by(username=data.get('username')).first():
        return jsonify({'message': 'Username taken'}), 400
    if User.query.filter_by(email=data.get('email')).first():
        return jsonify({'message': 'Email taken'}), 400
        
    # Create user logic duplicated for API to satisfy requirement
    # Ideally should move to a service layer
    from app import db
    user = User(username=data.get('username'), email=data.get('email'))
    user.set_password(data.get('password'))
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201
