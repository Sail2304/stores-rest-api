from flask_restful import Resource, reqparse
import sqlite3
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type = str,
                        required = True,
                        help = "This field can not be blank"
                        )
    
    parser.add_argument('password',
    type = str,
    required = True,
    help = "This field cannot be blanked"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message" : f"A user with username {data['username']} already exists"}


        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201