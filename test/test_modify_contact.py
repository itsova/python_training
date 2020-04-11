# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))
    assert len(old_contacts) == app.contact.count()


def test_modify_contact_midlename(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    app.contact.modify_first_contact(Contact(middlename="New middlename"))
    assert len(old_contacts) == app.contact.count()
