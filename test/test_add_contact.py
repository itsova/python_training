# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="ffghfgh", middlename="ghgfhfg", lastname="hgfhfg", nickname="fghfghfg",
                               title="hfhfghgf", company="ghfghfgh", address="fghfghf",
                               home="fghfgdhf", mobile="gfhfghfgh", email="fghfghfg"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                                   title="", company="", address="",
                                   home="", mobile="", email=""))
    app.session.logout()