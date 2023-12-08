from flask import Flask, jsonify, request
from user_services import UserService

app = Flask(__name__)
user_service = UserService()

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_service.create_user(user_data)
    return jsonify({"message": "User created successfully"}), 201

@app.route('/getuser/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_json())
    return jsonify({"message": "User not found"}), 404

@app.route('/getusers', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify([user.to_json() for user in users])

@app.route('/deleteuser/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service.delete_user(user_id)
    return jsonify({"message": "User deleted successfully"}), 200

@app.route('/updateuser/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    user_data['id'] = user_id
    user_service.update_user(user_data)
    return jsonify({"message": "User updated successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

