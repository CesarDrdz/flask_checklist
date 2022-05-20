from flask_app.config.mysqlconnection import connectToMySQL
<<<<<<< HEAD

=======
from pprint import pprint
>>>>>>> 40aa07b72d21909cbd8e9759fafd65e0d752c674
DATABASE = 'checklist'

class Model:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.column1 = data['column1']
        self.column2 = data['column2']
        self.column3 = data['column3']
<<<<<<< HEAD
=======
        self.user_id = data['user_id']
        if 'first_name' in data:
            self.user = data['first_name']
>>>>>>> 40aa07b72d21909cbd8e9759fafd65e0d752c674
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! CREATE
    @classmethod
    def save(cls, data:dict) -> int:
<<<<<<< HEAD
        query = "INSERT INTO models (column1,column2,column3) VALUES (%(column1)s,%(column2)s,%(column3)s);"
=======
        query = "INSERT INTO models (column1,column2,column3, user_id) VALUES (%(column1)s,%(column2)s,%(column3)s, %(user_id)s);"
>>>>>>> 40aa07b72d21909cbd8e9759fafd65e0d752c674
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    # ! READ/RETRIEVE ALL
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM models;"
        results = connectToMySQL(DATABASE).query_db(query)
        models = []
        for u in results:
            models.append( cls(u) )
        return models
<<<<<<< HEAD
=======
 
    # ! READ/RETRIEVE ALL
    @classmethod
    def get_all_with_user(cls) -> list:
        query = "SELECT * FROM users LEFT JOIN models ON users.id = models.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        models = []
        for u in results:
            models.append( cls(u) )
        return models
>>>>>>> 40aa07b72d21909cbd8e9759fafd65e0d752c674
    
    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data:dict) -> object:
        query  = "SELECT * FROM models WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    # ! UPDATE
    @classmethod
    def update(cls,data:dict) -> int:
<<<<<<< HEAD
        query = "UPDATE models SET column1=%(column1)s,column2=%(column2)s,column3=%(column3)s,updated_at=NOW() WHERE id = %(id)s;"
=======
        query = "UPDATE models SET column1=%(column1)s,column2=%(column2)s,column3=%(column3)s,user_id=%(user_id)s WHERE id = %(id)s;"
>>>>>>> 40aa07b72d21909cbd8e9759fafd65e0d752c674
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! DELETE
    @classmethod
    def destroy(cls,data:dict):
        query  = "DELETE FROM models WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)