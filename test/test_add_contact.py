# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_number(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=firstname, lastname=lastname, address=address, homephone=homephone, workphone=workphone,
            email=email, email2=email2, email3=email3, mobilephone=mobilephone, secondaryphone=secondaryphone)
    for firstname in ["", random_string("firstname", 10)]
    for lastname in ["", random_string("lastname", 10)]
    for address in ["", random_string("address", 20)]
    for email in ["", random_string("emailr", 15)]
    for email2 in ["", random_string("email2", 15)]
    for email3 in ["", random_string("email3", 15)]
    for homephone in ["", random_string_number("+7", 15)]
    for mobilephone in ["", random_string_number("+7", 25)]
    for workphone in ["", random_string_number("+7", 20)]
    for secondaryphone in ["", random_string_number("+7", 20)]
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) +1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




