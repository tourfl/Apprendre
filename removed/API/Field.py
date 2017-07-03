from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Field(Base):
    """a Field is an up category of Topic"""
    __tablename__ = 'fields'
    id = Column(Integer, primary_key = True)
    title = Column(String)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Field(title='%s')>" % (self.title)


def test():
    field1 = Field("English")

    print(field1)

if __name__ == '__main__':
    test()