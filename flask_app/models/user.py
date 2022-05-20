from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
<<<<<<< HEAD

=======
from pprint import pprint
from flask_app.models.model import Model
>>>>>>> 40aa07b72d21909cbd8e9759fafd65e0d752c674

DATABASE = 'checklist'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
<<<<<<< HEAD
=======
        self.models = []
>>>>>>> 40aa07b72d21909cbd8e9759fafd65e0d752c674
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    ## ! used in user validation
    @classmethod
    def get_by_email(cls,data:dict) -> object or bool:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

<<<<<<< HEAD
=======
    @classmethod
    def get_user_with_models(cls, data:dict):
        query = "SELECT * FROM users LEFT JOIN models ON users.id = models.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        pprint(results)
        user = cls(results[0])
        for result in results:
            model_dict = {
                'id': result['models.id'],
                'column1': result['column1'],
                'column2': result['column2'],
                'column3': result['column3'],
                'user_id': result['user_id'],
                'created_at': result['models.created_at'],
                'updated_at': result['models.updated_at']
            }
            user.models.append(Model(model_dict))
        return user


>>>>>>> 40aa07b72d21909cbd8e9759fafd65e0d752c674
    @staticmethod
    def validate_user(user:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(user['first_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if user['password'] != user['confirm-password']:
            flash("Passwords do not match")
            is_valid = False
<<<<<<< HEAD
=======
        if len(user['password']) < 8:
            flash("Password must be at least 8 character long.")
            is_valid = False
>>>>>>> 40aa07b72d21909cbd8e9759fafd65e0d752c674
        return is_valid