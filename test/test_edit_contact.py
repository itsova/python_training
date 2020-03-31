# -*- coding: utf-8 -*-

from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="1", middlename="2", lastname="3", nickname="4"))
    app.session.logout()