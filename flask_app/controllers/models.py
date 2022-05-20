<<<<<<< HEAD
from flask import render_template, request, redirect, session
=======
from flask import render_template, request, redirect
>>>>>>> 40aa07b72d21909cbd8e9759fafd65e0d752c674
from flask_app import app
from flask_app.models.model import Model

# ! ////// CREATE  //////
# TODO CREATE REQUIRES TWO ROUTES:
# TODO ONE TO DISPLAY THE FORM:
@app.route('/model/new')
def new_model():
    return render_template("new_model.html")

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/model/create',methods=['POST'])
def create_model():
    print(request.form)
    Model.save(request.form)
    return redirect('/models')

# TODO READ ALL
@app.route('/models')
def models():
<<<<<<< HEAD
    if 'user_id' not in session:
        return redirect ('/logout')
        
    return render_template("models.html",models=Model.get_all())
=======
    return render_template("models.html",models=Model.get_all_with_user())
>>>>>>> 40aa07b72d21909cbd8e9759fafd65e0d752c674

# TODO READ ONE
@app.route('/model/show/<int:id>')
def show_models(id):
    data ={ 
        "id":id
    }
    return render_template("show_model.html",model=Model.get_one(data))

# ! ///// UPDATE /////
# TODO UPDATE REQUIRES TWO ROUTES
# TODO ONE TO SHOW THE FORM
@app.route('/model/edit/<int:id>')
def edit_model(id):
    data ={ 
        "id":id
    }
    return render_template("edit_model.html",model=Model.get_one(data))

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/model/update',methods=['POST'])
def update_model():
    Model.update(request.form)
    return redirect('/models')

# ! ///// DELETE //////
@app.route('/model/destroy/<int:id>')
def destroy_model(id):
    data ={
        'id': id
    }
    Model.destroy(data)
    return redirect('/models')