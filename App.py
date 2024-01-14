from flask import Flask, send_from_directory, request
from flask_mysqldb import MySQL
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/static/<path:path>')
def index(path):
    return send_from_directory('static', path)



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'firewall15'
app.config['MYSQL_DB'] = 'prueba'

mysql = MySQL(app)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO products (product_Name, isAvailable, isFeaturedProduct) VALUES (%s, %r, %r)', (data['product_Name'], data['isAvailable'], data['isFeaturedProduct']))
    mysql.connection.commit()
    return {'message': 'confirmation'}, 200

# @app.route('/edit_product')
# def edit_product():
#     return

# @app.route('/edit_product')
# def server_interface():
#     return

if __name__ == '__main__':
    app.run(port=5000, debug=True)
