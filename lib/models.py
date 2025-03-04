#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)

    freebies = relationship('Freebie', backref='company')

    def give_freebie(self, dev, item_name, value, session):
        new_freebie = Freebie(dev=dev, item_name=item_name, value=value)
        self.freebies.append(new_freebie)
        return new_freebie
    
    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()
    
class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    freebies = relationship('Freebie', backref='dev')

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)
    
    def give_away(self, dev, freebie, session):
        if freebie.dev == self:
            freebie.dev = dev
            session.commit()
            return True
        return False
    
    @property
    def companies(self):
        return [freebie.company for freebie in self.freebies if freebie.company]

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)
    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    def print_details(self):
        return f"{self.dev.name} got a {self.item_name} from {self.company.name}."
    
engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

