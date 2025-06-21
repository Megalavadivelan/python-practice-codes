s_username="EMC"
s_password="123"
uname=input("uname:")
password=input("password:")
def validate():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False
validate()
print(validate())
