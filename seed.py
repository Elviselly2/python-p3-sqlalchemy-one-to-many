#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Review, Base
from faker import Faker

# Initialize database connection
DATABASE_URL = "sqlite:///one_to_many.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables if they don't exist
Base.metadata.create_all(engine)

# Initialize Faker
fake = Faker()

# Clear existing data
session.query(Game).delete()
session.query(Review).delete()
session.commit()

# Seed Games
games = [
    Game(title="Breath of the Wild", genre="Action-adventure", platform="Switch", price=60),
    Game(title="Elden Ring", genre="RPG", platform="PC", price=50),
    Game(title="Minecraft", genre="Sandbox", platform="Multi-platform", price=30),
]

session.add_all(games)
session.commit()

# Seed Reviews
for game in games:
    for _ in range(3):  # Create 3 reviews per game
        review = Review(
            score=fake.random_int(min=1, max=10),
            comment=fake.sentence(),
            game_id=game.id
        )
        session.add(review)

session.commit()

print("Database seeded successfully!")
