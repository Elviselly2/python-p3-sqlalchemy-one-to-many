#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Review

# Set up the database connection
DATABASE_URL = "sqlite:///one_to_many.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Fetch all games
games = session.query(Game).all()
print("\nGames in Database:")
for game in games:
    print(game)

# Fetch reviews for a specific game
game_id = 1  # Change this to test different game IDs
game = session.query(Game).filter_by(id=game_id).first()

if game:
    print(f"\nReviews for {game.title}:")
    for review in game.reviews:
        print(review)
else:
    print(f"\nNo game found with ID {game_id}")

# Open interactive debug session
import ipdb; ipdb.set_trace()
