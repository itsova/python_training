# -*- coding: utf-8 -*-

from model.contact import Contact


def test_delete_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()

