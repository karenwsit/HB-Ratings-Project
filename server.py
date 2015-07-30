"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")

@app.route('/login', methods=["GET", "POST"])
def site_login():
    """Handles submission of login form and add user id to session. Redirect to homepage with flash message"""
    
    if  request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # add user to database
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()

        # get id of new user from database and put in session
        user_ob = User.query.filter_by(email=email).first()

        if 'login' not in session:
            session['login'] = user_ob.user_id

        flash('Thank you SO much for logging in! Now go rate some movies.')

        return redirect('/')

    else:
        return render_template("login.html")

@app.route('/logout')
def site_logout():
    """Logs users out by deleting userid from session & redirect to homepage with flash message"""

    # delete user from session
    del session['login']

    # redirect to homepage with a flash message

    flash("You're logged out, loser. Thanks for nothing.")

    return redirect('/')


@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)


@app.route("/users/<int:id>")
def show_user(id):
    """Return page showing details of a given user."""


    # CONTINUE HERE - SQL ALCHEMY RELATIONSHIPS

    # rating_ob = Rating.query.filter_by(user_id=id).all()
    # movie_id = rating_ob.movie_id

    # movies_reviewed_by_user = Movie.query.filter_by(movie_id=movie_id).all()


    return render_template("user_details.html", users)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run()