from py5paisa import FivePaisaClient

def login():
    try:
        client = FivePaisaClient(email="", passwd="", dob="")
        client.login()
        log= True

    except TypeError:
        client = FivePaisaClient(email="", passwd="", dob="")
        client.login()
        log = True

    finally:
        log = False
        print('Login Failed')
    return log

login()

