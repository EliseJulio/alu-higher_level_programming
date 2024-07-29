#!/usr/bin/python3
"""script that deletes all State objects with a
name containing the letter a from the database
hbtn_0e_6_usa
"""
import sys
from model_state import Base, State  
from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker  
  
def delete_states_with_a(username, password, db_name):  
   engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{db_name}")  
   Base.metadata.bind = engine  
   Session = sessionmaker(bind=engine)  
   session = Session()  
  
   states_to_delete = session.query(State).filter(State.name.like("%a%")).all()  
   for state in states_to_delete:  
      session.delete(state)  
   session.commit()  
   session.close()  
  
if __name__ == "__main__":  
   import sys  
   if len(sys.argv)!= 4:  
      print("Usage: {}  ".format(sys.argv))  
      sys.exit(1)  
   delete_states_with_a(sys.argv, sys.argv, sys.argv)
