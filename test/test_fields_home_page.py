import re
from random import randrange
from model.contact import Contact


def test_phones_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = db.get_contact_list()
    a = 0
    i = len(db.get_contact_list())
    while a < i:
        assert contact_from_home_page[a].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db[a])
        a += 1


def test_emails_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = db.get_contact_list()
    a = 0
    i = len(db.get_contact_list())
    while a < i:
        assert contact_from_home_page[a].all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db[a])
        a += 1


def test_names_and_address(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = db.get_contact_list()
    a = 0
    i = len(db.get_contact_list())
    while a < i:
        assert contact_from_home_page[a].lastname == contact_from_db[a].lastname
        assert contact_from_home_page[a].firstname == contact_from_db[a].firstname
        assert contact_from_home_page[a].address == contact_from_db[a].address
        a += 1


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                            [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))