from flask import Flask, render_template, Blueprint
from models.venta import Venta
from utils.db import db
import pymysql
from controllers.ventaController import venta_bp

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.register_blueprint(venta_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/comisionesdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'SecretKeyForSessionManagement'

db.init_app(app) 

@app.route("/")
def index():
    ventas = Venta.query.all()
    return render_template("index.html", comisiones=ventas)

if __name__ == "__main__":
    app.run(debug=True)