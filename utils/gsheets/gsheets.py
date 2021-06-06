import pygsheets

def cl():
    client = pygsheets.authorize(client_secret='client_secret_401689895164-lp5dvmobse0c1s8aqq7ijle7eu6rb14n.apps.googleusercontent.com.json')
    new_sheet = client.sheet.create('test')
    sh = client.open('test1')
    print(sh)
    for i, j in new_sheet.items():
        print(i, j)


if __name__ == '__main__':
    cl()


