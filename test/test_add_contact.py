# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="ffghfgh", middlename="ghgfhfg", lastname="hgfhfg", nickname="fghfghfg"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname=""))
