# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New firstname")
    index = randrange(len(old_contacts))
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()


def test_modify_contact_midlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(middlename="New middlename")
    index = randrange(len(old_contacts))
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
