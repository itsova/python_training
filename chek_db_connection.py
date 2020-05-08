from fixture.orm import ORMFixture
from fixture.db import DbFixture
from model.group import Group
from model.contact import Contact


db = ORMFixture(host="localhost", name="addressbook", user="root", password="")

# total_amount_contacts = len(db.get_contact_list())
# group_list = db.get_group_list()
# for group in group_list:
#      print(group.id)
#      contacts_in_group = len(db.get_contacts_in_group(Group(id=group.id)))
#      print('****' + str(contacts_in_group) + ' ' + str(group.id))
#      if contacts_in_group < total_amount_contacts:
#          pass

group_list = db.get_group_not_in_contact(Contact(id='465'))
for it in group_list:
    print(it)

# def test_add_contact_in_group(app):
#     global id, g
#     db = ORMFixture(host="localhost", name="addressbook", user="root", password="")
#     group_list = db.get_group_list()
#     contact_list = db.get_contact_list()
#     if len(group_list) == 0:
#         app.group.create(Group(name="Test"))
#     if len(contact_list) == 0:
#         app.contact.create(Contact(firstname="Test"))
#     for contact in contact_list:
#         group_wo_contact = db.get_group_not_in_contact(Contact(id=contact.id))
#         if len(group_wo_contact) > 0:
#             id = contact.id
#             g = group_wo_contact[0].id
#             break
#         else:
#             pass
#     app.contact.add_contact_in_group_by_id(id, g)










