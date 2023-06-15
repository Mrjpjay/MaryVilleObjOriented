from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    
    def __rep__(self):
        return f"<User(name={self.name}, email={self.email})>"
    
    def __str__(self):
        return f"User {self.id} - Name: {self.name}, Email: {self.email}"
    
#SQLite database
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#add a new user
new_user = User(name='Romero Juan', email='rj@gmail.com')
session.add(new_user)
session.commit()

#retrieve the user
users = session.query(User).all()
for user in users:
    print(user)
    
session.close()