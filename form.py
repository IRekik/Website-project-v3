import csv
import smtplib
from wsgiref.validate import validator
import os
from flask import Flask, render_template, redirect, url_for, request
from wtforms import StringField, TextAreaField, form
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email
from flask_wtf import FlaskForm

@app.route('/register_form', methods=["POST","GET"])
def Register_Store():
    if request.method == "POST":
        form=username_form()
        if form.is_submitted():
            with open('Data/log_in.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(request.form["username"])
                writer.writerow(request.form["password"])
    email = request.form.get("email")
    message = "Congratulations!\nYou are now a new member of the website Dofustus! Thank you for choosing to create an account in our website! We hope that you find what you are searching for and keep learning more about our game.\n\nSee you soon!"
    email_server.login("isrekik.2000@gmail.com", "kiker0002")
    email_server.sendmail("isrekik.2000@gmail.com", email, message)
    return redirect("/")

@app.route('/login_form', methods=["POST"])
def Log_In():
    x=""
    bool1=False
    bool2=False
    if request.method == "POST":
        form = username_form()
        if form.is_submitted():
            y=request.form["username"]
            z=request.form["password"]
            w=""
            with open('../untitled2/Data/log_in.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    for k in row:
                        x += str(k)
                    if x == y:
                        bool1=True
                        w=x
                        print("Username found")
                    if z == x and z != w:
                        bool2=True
                        print("Password found")
                    x=""
            if bool1 and bool2:
                return redirect("/Forum")
            else:
                return redirect("WrongPassword")
    else:
        return redirect("")


@app.route('/contact_support', methods=["POST"])
def receive_support():
    x = ""
    counter=0
    if request.method == "POST":
        with open('../untitled2/Data/contact.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(request.form["support_message"])
        with open('../untitled2/Data/contact.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                for k in row:
                    x += str(k)

        message.append(x)
        f = open("../untitled2/Data/contact.csv", "w+")
        f.close()
        x=""
        print(message)
        counter += 1
    return render_template("Contact support.html",list=message)
