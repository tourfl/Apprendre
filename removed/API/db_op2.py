from db_op import Session, Hand


def list_to_db(set, session):
    """" Simple List to DataBase entry """

    if type(set) is list and len(set) > 1:

        my_hand = Hand(keyword=set[0], yekword=set[1])
        session.add(my_hand)

        return True

    return False


def l2_to_db(s2, session):
    """ Square List to DataBase entries """
    
    if type(s2) is list:
        for item in s2:
            if not list_to_db(item, session):
                return False

        return True

    return False      


def test(session):
    set1 = ['hand', 'main']

    print(Hand(3)) # False

    print(Hand(set1)) # True

    # faire une requête provoque un flush
    my_set = session.query(Hand).filter_by(words='hand').first()

    print(my_set.id) # 1


def test2(session):
    full_list = [['hand', 'main'], ['foot', 'pied'], ['shoulder', 'épaule']]
    wrong_list = [2, 3, 4]
    w_list = [['hand', 'main'], ['pied']]

    print(list_to_db(full_list[0], session)) # True
    print(l2_to_db(full_list, session)) # True
    print(l2_to_db(wrong_list, session)) # False
    print(l2_to_db(w_list, session)) # False

    my_set = session.query(Hand).filter_by(keyword='foot').first()

    print(my_set.id) # 3


if __name__ == '__main__':
    session = Session()

    test(session)
