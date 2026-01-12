from flask import *
from public import public
from admin import admin
from api import api


app=Flask(__name__)

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(api)


app.run(debug=True,host="0.0.0.0")