import re
from random import randrange
from model.contact import Contact


def test_all_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)


# def test_phones_on_home_page(app):
#     index = randrange(len(app.contact.get_contact_list()))
#     contact_from_home_page = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#
# def test_emails_on_home_page(app):
#     index = randrange(len(app.contact.get_contact_list()))
#     contact_from_home_page = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
#
# def test_names_and_address(app):
#     index = randrange(len(app.contact.get_contact_list()))
#     contact_from_home_page = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#     assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#     assert contact_from_home_page.address == contact_from_edit_page.address
#
#
# def clear(s):
#     return re.sub("[() -]", "", s)
#
# def merge_phones_like_on_home_page(contact):
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x: clear(x),
#                                 filter(lambda x: x is not None,
#                             [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
#
#
# def merge_emails_like_on_home_page(contact):
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x: clear(x),
#                                 filter(lambda x: x is not None,
#                                        [contact.email, contact.email2, contact.email3]))))