from cs50 import SQL
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import os

app = Flask(__name__)
 
# Connect to database

db = SQL("sqlite:///users.db")

# Check if email exists in database
@app.route('/check_email', methods=['POST'])
def check_email():
    email = request.form['email']
    cur = g.db.cursor()
    cur.execute("SELECT * FROM users WHERE email=?", (email,))
    if cur.fetchone() is not None:
        # Email exists, redirect to original.html
        return redirect('/original.html')
    else:
        # Email does not exist, display error message
        return "Email not found"

# Close database connection
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

if __name__ == '__main__':
    app.run()