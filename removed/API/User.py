from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """User contains metadata for a user"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String)

    def __init__(self, login):
        self.login = login

    def __repr__(self):
        return "<User(login='%s')>" % (self.login)


def test():

    user1 = User("Raph")

    print(user1)


if __name__ == '__main__':
    test()
