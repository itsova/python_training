# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New firstname"))


def test_modify_contact_midlename(app):
    app.contact.modify_first_contact(Contact(middlename="New middlename"))
