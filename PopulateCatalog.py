"""This module populates item catalog database with sample data"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User_info

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

user1 = User_info(name="Clint", email="MyEmail@gmail.com")
session.add(user1)
session.commit()

category1 = Category(user_id=1,
                     name="Baseball",
                     description=("a ball game played between two teams "
                                  "on a field with a diamond-shaped "
                                  "circuit of four bases"))

session.add(category1)
session.commit()



item1 = Item(user_id=1, name="Baseball", description="a hard ball used in the game of baseball",
             category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Glove",
             description=("A thick glove worn by defenders in baseball"), category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1,
             name="Bat", description=("A smooth wooden or metal club used in baseball to hit a ball thrown by the pitcher"),
             category=category1)

session.add(item3)
session.commit()

category2 = Category(user_id=1, name="Football",
                     description=("a form of team game played in North America with an oval ball on a field marked out as a gridiron"))

session.add(category2)
session.commit()


item1 = Item(user_id=1, name="Football",
             description="An oval ball inflated with air", category=category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1,
             name="Helmet", description="A piece of protective equipment worn on the head", category=category2)

session.add(item2)
session.commit()


category1 = Category(user_id=1,
                     name="Hockey", description=("A fast contact sport on an ice rink"))

session.add(category1)
session.commit()


item1 = Item(user_id=1, name="Hockey Stick",
             description="A stick used to maneuver the puck",
             category=category1)

session.add(item1)
session.commit()

item1 = Item(user_id=1, name="Puck",
             description="A black rubber object used in Hockey",
             category=category1)

session.add(item2)
session.commit()

print("added menu items!")
