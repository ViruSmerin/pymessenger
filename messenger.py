from fbchat import Client
from fbchat.models import *
from getpass import getpass
username = input('username::')
print ("Please select a password:: ")
passwd = getpass()
client = Client(username, passwd)
name = input('your name ::')
users = client.searchForUsers(name)
user = users[0]
print("User's ID: {}".format(user.uid))
print("User's name: {}".format(user.name))
print("User's profile picture URL: {}".format(user.photo))
print("User's main URL: {}".format(user.url))
confirm = input('are you sure??(yes/no)')

if confirm == "yes":
    message=input("Type message here::")
    ID = input("User ID here::")
    client.send(Message(text=message), thread_id=ID, thread_type=ThreadType.USER)
     
else:
    pass
