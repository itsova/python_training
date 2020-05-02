from model.contact import Contact
from model.group import Group
import random

def test_dell_contact_in_group(app, db):
    if len(db.get_address_in_groups()) == 0:
        app.contact.create(Contact(firstname="Test"))
        app.group.create(Group(name="Test"))
        contact = random.choice(db.get_contact_list())
        app.contact.add_contact_in_group_by_id(contact.id)
    old_bind = db.get_address_in_groups()
    bind = random.choice(old_bind)
    app.contact.dell_contact_in_group_by_id(bind[1])
    new_bind = db.get_address_in_groups()
    assert len(old_bind)-1 == len(new_bind)

