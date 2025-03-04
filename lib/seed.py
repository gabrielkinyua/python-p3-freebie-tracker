from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

# Create the database connection
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear old data
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

# Create companies
google = Company(name="Google", founding_year=1998)
microsoft = Company(name="Microsoft", founding_year=1975)
facebook = Company(name="Facebook", founding_year=2004)

# Create developers
alice = Dev(name="Alice")
bob = Dev(name="Bob")
charlie = Dev(name="Charlie")

# Create freebies
freebie1 = Freebie(item_name="T-shirt", value=10, dev=alice, company=google)
freebie2 = Freebie(item_name="Mug", value=5, dev=bob, company=microsoft)
freebie3 = Freebie(item_name="Sticker", value=2, dev=charlie, company=facebook)
freebie4 = Freebie(item_name="Laptop Sleeve", value=25, dev=alice, company=microsoft)

# Add and commit everything to the database
session.add_all([google, microsoft, facebook, alice, bob, charlie, freebie1, freebie2, freebie3, freebie4])
session.commit()

print("Database seeded successfully!")
