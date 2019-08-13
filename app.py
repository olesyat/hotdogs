from flask import Flask, render_template, redirect, request
import sqlite3
import mysql.connector

def get_connection():
    return sqlite3.connect("HOTDOGS.db")

app = Flask(__name__)


@app.route('/')
def welcome():
        connection = get_connection()
        cursor = connection.cursor()
        return render_template('welcome.html')

@app.route('/create', methods=['POST', "GET"])
def create_hotdog():
    if request.method == 'POST':
        hot_dpg_name = request.form['nm']
        return 'You created %s' % hot_dpg_name
    else:
        return render_template('create.html')

@app.route('/read')
def read_hotdog():
    return 'Read'


@app.route('/update')
def update_hotdog():
    return 'updated'

@app.route('/delete')
def delete_hotdog():
    return 'Deleted'




if __name__ == '__main__':
    app.run(debug=True)
