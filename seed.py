"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app


# def load_users():
#     """Load users from u.user into database."""

#     user_data_file = open("seed_data/u.user")
#     user_data = user_data_file.read().split("\n")
#     for line in user_data:
#         user_data_list = line.split("|")
#         if user_data_list == ['']:
#             continue
#         user_id, age, zipcode = user_data_list[0], user_data_list[1], user_data_list[4]
#         new_user = User(user_id=user_id, age=age, zipcode=zipcode)
#         db.session.add(new_user)
#         db.session.commit()

def load_movies():
    """Load movies from u.item into database."""


def load_ratings():
    """Load ratings from u.data into database."""

    ratings_file = open("seed_data/u.data")
    ratings_data = ratings_file.read().split("\n")
    for line in ratings_data:
        ratings_data_list = line.split("\t")
        if ratings_data_list == ['']:
            continue
        movie_id, user_id, score = int(ratings_data_list[0]), int(ratings_data_list[1]), int(ratings_data_list[2])
        new_rating = Rating(movie_id=movie_id, user_id=user_id, score=score)
        db.session.add(new_rating)
        db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # load_users()
    load_movies()
    load_ratings()
