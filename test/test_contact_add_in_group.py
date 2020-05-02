from model.contact import Contact
from model.group import Group
import random

def test_add_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    old_bind = db.get_address_in_groups()
    app.contact.add_contact_in_group_by_id(contact.id)
    new_bind = db.get_address_in_groups()
    assert len(old_bind) + 1 == len(new_bind)
