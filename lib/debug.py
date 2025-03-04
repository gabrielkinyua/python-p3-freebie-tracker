#!/usr/bin/env python3


from models import session, Company, Dev, Freebie

# Get a developer
alice = session.query(Dev).filter_by(name="Alice").first()
print(alice.companies) 

# Get a company
google = session.query(Company).filter_by(name="Google").first()
print(google.freebies)

# Test freebie details
freebie = session.query(Freebie).first()
print(freebie.print_details()) 

# Test if Alice received a specific freebie
print(alice.received_one("Mug")) 

freebie_to_give = session.query(Freebie).filter_by(item_name="Mug").first()

# Give away a freebie
bob = session.query(Dev).filter_by(name="Bob").first()
alice.give_away(bob, freebie_to_give, session)
print(freebie_to_give.dev.name) 



