from flask import Flask, render_template, redirect, request
import sqlite3
import mysql.connector

def get_connection():
    return sqlite3.connect("HOTDOGS.db")

app = Flask(__name__)

@app.route('/')
def read():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            f"select * from DOGGIES")
        doggies = cursor.fetchall()
    except mysql.connector.Error as error:
        print(error)
    connection.commit()
    connection.close()
    if doggies:
        return render_template('index.html', doggies=doggies, l=len(doggies))
    else:
        return render_template("no_doggies.html")
    
@app.route('/create', methods=['POST', "GET"])
def create_hotdog():
    if request.method == 'POST':
        name = request.form['name']
        meat = request.form['meat']
        mustard = request.form['mustard']
        ketchup = request.form['ketchup']
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                f"insert into DOGGIES (name, meat, mustard, ketchup) values ('{name}','{meat}','{mustard}', '{ketchup}')")
        except mysql.connector.Error as error:
            print(error)
        connection.commit()
        connection.close()
        return read()
    else:
        return render_template('create.html')

@app.route('/update', methods=['POST', 'GET'])
def update_hotdog():
    if request.method == 'POST':
        old = request.form['old']
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                f"SELECT * FROM DOGGIES WHERE ID = {old}")
            dog = cursor.fetchone()

            buns = ['simple', 'gluten-free', 'with-poppy-seeds', 'wholemeal']
            meats = ['beef', 'veal', 'pork', 'vegan']
            mustards = ['Yes', 'No']
            ketchups = ['Yes', 'No']
            lst = [buns, meats, mustards, ketchups]

            for i, l in enumerate(lst):
                l = l.remove(dog[i+1])

            mustard_prime = "hidden"
            mustard_secondary = "checkbox"
            if dog[3] == 'Yes':
                mustard_prime, mustard_secondary = mustard_secondary, mustard_prime

            ketchup_prime = "hidden"
            ketchup_secondary = "checkbox"
            if dog[4] == 'Yes':
                ketchup_prime, ketchup_secondary = ketchup_secondary, ketchup_prime
                
        except mysql.connector.Error as error:
            print(error)
        connection.commit()
        connection.close()
        return render_template("update.html", dog=dog, buns=buns, meats=meats, mustards=mustards, mustard_prime=mustard_prime, mustard_secondary=mustard_secondary, ketchups=ketchups, ketchup_prime=ketchup_prime, ketchup_secondary=ketchup_secondary)
    else:
        return "oops"

@app.route('/updated', methods=['PoST'])
def updated():
    if request.method == 'POST':
        newname = request.form['name']
        newmeat = request.form['meat']
        newmustard = request.form['mustard']
        newketchup = request.form['ketchup']
        id = request.form['id']
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                f"UPDATE DOGGIES SET name = '{newname}', meat = '{newmeat}', mustard = '{newmustard}', ketchup = '{newketchup}' WHERE ID = {id}")
        except mysql.connector.Error as error:
            print(error)
        connection.commit()
        connection.close()
        return read()

@app.route('/delete', methods=['POST'])
def delete_hotdog():
    if request.method == 'POST':
        delete = request.form['trash']
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                f"DELETE FROM DOGGIES WHERE ID = {delete}")
        except mysql.connector.Error as error:
            print(error)
        connection.commit()
        connection.close()
        return read()
    else:
        return "oops"

if __name__ == '__main__':
    app.run()
