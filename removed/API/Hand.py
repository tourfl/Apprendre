from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///:memory:', echo=False)

Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()



## TODO: recursive import
class Topic(Base):
    """Topic contains metadata for a list of words"""
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    # creator = Column(Integer, ForeignKey("user.id"), nullable=False)
    nb_use = Column(Integer)
    hand = relationship('Hand')

    def __init__(self, dic):
        self.title = dic["title"]
        self.nb_use = 0

    def __repr__(self):
        return "<Topic(title='%s', nb_use='%i')>" % (self.title, self.nb_use)


class Hand(Base):
    """a Hand contains a set of words"""
    __tablename__ = 'hands'
    id = Column(Integer, primary_key=True)
    keyword = Column(String)
    word2 = Column(String)
    topic_id = Column(Integer, ForeignKey('topics.id'))

    def __init__(self, set):
        try:
            self.keyword = set[0]
            self.word2 = set[1]
            print('ok')
        except (IndexError, TypeError):
            print('error')

    def __repr__(self):
        return "<Hand(keyword='%s', word2='%s')>" % (self.keyword, self.word2)

    def to_list(self):
        return [self.keyword, self.word2]


Base.metadata.create_all(engine)

def test():
    invhan2 = Hand([2]) # error
    valhan2 = Hand([1, 2]) # ok
    valhan3 = Hand(['hand', 'main']) # ok
    valhan4 = Hand(['avion', 'plane', 'craft']) # ok
    
    session.add(invhan2)
    session.add(valhan2)
    session.add(valhan3)
    session.add(valhan4)


def test_list():
    set1 = ['hand', 'main']

    valhand = Hand(set1)

    print(valhand.to_list() == set1) # True

if __name__ == '__main__':
    test_list()
