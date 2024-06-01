from flask import Flask, request, jsonify
from entities.user import User
from usecase.create_user import CreateUser
from usecase.find_user import FindUser
from adapter.sql_user_repository import SqlUserRepository

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def createUser():
    user =User(request.json['name'], request.json['email'],request.json['password'])

    repository = SqlUserRepository()
    user_repository = CreateUser(repository)
    user_response = user_repository.execute(user)
    return jsonify(user_response), 201


@app.route('/users-by-email', methods=['get'])
def getUsersByEmail():
    email = request.args.get('email')

    repository = SqlUserRepository()
    user_repository = FindUser(repository)
    user_response = user_repository.find(email)

    if user_response == None:
        return jsonify({"message": "User not found"}), 404
    else:
        return jsonify({
            "name": user_response.name,
            "email": user_response.email
        }), 200
    
if __name__=='__main__': 
    app.run(debug=True)