from mongoengine import *

connect('turtledb', host='192.168.2.100', port=27017)

class Npi(Document):
    npi = StringField(max_length=100, required=True)
    first_name = StringField(max_length=50, required=True)
    middle_initial = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)

npi_list = Npi()

npi_list.npi = '001'
npi_list.first_name = "foo"
npi_list.middle_initial = ""
npi_list.last_name = "bar"

npi_list.save()

