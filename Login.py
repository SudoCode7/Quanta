from py5paisa import FivePaisaClient

def login():
    try:
        client = FivePaisaClient(email="jakshat101@gmail.com", passwd="$Ecurity@158", dob="20020714")
        client.login()
        log= True

    except TypeError:
        client = FivePaisaClient(email="jakshat101@gmail.com", passwd="$Ecurity@158", dob="20020714")
        client.login()
        log = True

    finally:
        log = False
        print('Login Failed')
    return log

login()
