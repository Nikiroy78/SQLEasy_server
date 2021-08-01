from Flask import flask
import server_tools, getpass
server_tools.init(
    server_tools.pyOut('Enter username: '),
    server_tools.pyOut('Enter password: ', 3, getpass.getpass)
)


app = flask(__name__)

@app.route('/panel')
def panel():
    return '''
'''  # Вставить код...

@app.route('/server_api/<method>')
def server_api(method):
    
