import random, sys

login = None
password = None


def pyOut(TEXT, border=3, out=input):
    content = out(TEXT)
    if content and len(content) >= border:
        return content
    else:
        print('invalid inputed information')
        sys.exit(0)



def init(l, p):
    global login, password
    login = l
    password = p


def genTk(length=16, dictonary='1234567890abcdef'):
    token = ''
    for _ in range(length):
        token += dictonary[random.randint(0, len(dictonary) - 1)]
    return token


class server_api:
    def oauth(login, password, **kw):
        


methods = {
    'oauth': server_api.oauth
}
