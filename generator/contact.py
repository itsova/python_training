import getopt
import jsonpickle
import os.path
import random
import string
import sys
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_number(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname="", lastname="", address="", homephone="", workphone="",
            email="", email2="", email3="", mobilephone="", secondaryphone="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), address=random_string("address", 20),
            homephone=random_string_number("+7", 15), workphone=random_string_number("+7", 20),
            email=random_string("email@", 15), email2=random_string("email2", 15), email3=random_string("email3", 15),
            mobilephone=random_string_number("+7", 25), secondaryphone=random_string_number("+7", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))