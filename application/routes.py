from flask import render_template, request, redirect
from datetime import datetime
from application import app, db


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post")
def post():
    return render_template("posts/post1.html")


@app.route("/post1")
def post1():
    return render_template("posts/post1.html")


@app.route("/post2")
def post2():
    return render_template("posts/post2.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        """ Add entry to DB """
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        try:
            db.blogContacts.insert_one({
                "date": datetime.now(),
                "name": name,
                "email": email,
                "phone": phone,
                "message": message
            })
        except:
            return render_template("error_page.html")

    return render_template("contact.html")


@app.get('/<name>/delete/')
# OR
# @app.route('/<name>/delete/', methods=['POST'])
def delete(name):
    db.blogContacts.delete_many({"name": name})
    return redirect('/', code=302)
