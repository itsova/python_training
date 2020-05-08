from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture


def test_add_contact_in_group(app):
    global id, g
    db = ORMFixture(host="localhost", name="addressbook", user="root", password="")
    group_list = db.get_group_list()
    contact_list = db.get_contact_list()
    if len(group_list) == 0:
        app.group.create(Group(name="Test"))
        group_list = db.get_group_list()
    if len(contact_list) == 0:
        app.contact.create(Contact(firstname="Test"))
    c = 0
    for group in group_list:
        contacts_not_in_group = db.get_contacts_not_in_group(Group(id=group.id))
        if len(contacts_not_in_group) > 0:
            c += 1
            id = contacts_not_in_group[0].id
            g = group.id
            break
    if c == 0:
        app.contact.create(Contact(firstname="Test"))
        for group in group_list:
            contacts_not_in_group = db.get_contacts_not_in_group(Group(id=group.id))
            if len(contacts_not_in_group) > 0:
                id = contacts_not_in_group[0].id
                g = group.id
                break
    contacts_in_group = len(db.get_contacts_in_group(Group(id=group.id)))
    app.contact.add_contact_in_group_by_id(id, g)
    new_contacts_in_group = len(db.get_contacts_in_group(Group(id=group.id)))
    assert contacts_in_group + 1 == new_contacts_in_group



