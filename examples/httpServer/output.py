from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://admin:pass@localhost/test?sslmode=disable'
db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))

# Start HTTP server on a specified port
@app.route('/api/create', methods=['POST'])
def create_user():
    # Ensure username and password are valid
    username = request.form['username']
    password = request.form['password']
    if not username or not password:
        return 'Invalid input', 400

    # Insert new user record into PostgreSQL
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    # Return 200 OK if created or error if not
    return 'User created', 200

@app.route('/api/password_change', methods=['PUT'])
def change_password():
    username = request.form['username']
    new_password = request.form['newpassword']
    user = User.query.get(username)
    if user:
        user.password = new_password
        db.session.commit()
        return 'Password changed', 200
    else:
        return 'User not found', 404

@app.route('/api/retrieve', methods=['GET'])
def retrieve_user():
    username = request.args.get('username')
    user = User.query.get(username)
    if user:
        return 'User found', 200
    else:
        return 'User not found', 404

@app.route('/api/remove', methods=['DELETE'])
def remove_user():
    username = request.args.get('username')
    user = User.query.get(username)
    if user:
        db.session.delete(user)
        db.session.commit()
        return 'User removed', 200
    else:
        return 'User not found', 404

if __name__ == '__main__':
    app.run(port=8080)
