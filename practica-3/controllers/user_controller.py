from flask import request, jsonify, render_template

class UserController:
        def __init__(self, user_service):
            self.user_service = user_service  

        def get_user(self, user_id):
            user = self.user_service.get_user(user_id)
            if user:
                return render_template('user_view.html', user=user)
            return "User not found", 404
