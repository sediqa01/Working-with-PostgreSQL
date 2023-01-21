from sqlalchemy import (
    create_engine, Column, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base(db)

# create class base module for doctor


class Doctor(base):
    __tablename__ = "Doctor"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    feild = Column(String)


Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)

ahmad = Doctor(
    first_name="Ahmad",
    last_name="Talibi",
    feild="Patalogy"
)

session.add(ahmad)
session.commit()

doctors = session.query(Doctor)
for doctor in doctors:
    print(
        doctor.id,
        doctor.first_name + " " + doctor.last_name,
        doctor.feild,
        sep=" | "
    )