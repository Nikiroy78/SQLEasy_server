# SQLEasy server
It is documentation from SQLEasy server...
## Configuration
SQLEasy server must been configurated from correct work in your server.
### SQLEasy server GUI
this is GUI version of SQLEasy server, after start, you can edit custom settings and write your data: host, port, etc.
// Here pictures :)
### SQLEasy server lite
Lite version (console version) configure in command panel (terminal from Linux version and console from win32 version):
```bash
Enter login from command panel: Admin
Enter password from command panel: *****
You use httpS protocol? (Y/n): n
Enter host: http://localhost
Enter port (default: 8080): 8080
Want you save server errors in error logs? (Y/n): Y
Want you show detalis server errors in resonse (may be usefull from your projects, what no see error logs in server)? (Y/n): Y
Make directory "error logs"...
Creating database....
Creating config.cfg...
Starting server http://localhost:8080...
=====================================
```
Ps: in first step you can choose language
```bash
===============
CHOOSE LANGUAGE
===============
1. [EN] English/English
2. [RU] Russian/Русский
3. [PL] Polen/Polski
===============
Enter code: 1
```
You can choose language later.
## Administration
From administrating your server, you can use tools in http://localhost:8080/panel. Here located panel from administration server. 
Use your login and password:
// Pin photos...
You locating in command panel! Greatings!
// Pin photos...
You can choose language...
// Pin photo...
## API
You must use POST requests from using SQLEasy server API.
Requests you must send in next adress: **http://hostport:8080/api/method**
Ps. hostport it's your domain (localhost, 127.0.0.1, mysite.org, etc.)
From works you need **token**. Token can give in **http://hostport:8080/panel/tokens**. Token must been configurated from your protect.
### Errors in API
Codes:
100 - SQL Error, errors in SQL script
**Example: **
```json
{
	"error": {
		"code": 100,
		"description": "syntax error"
	}
}
```
2** - API errors
200 - Syntax error, bad request.
**Example:**
```json
{
	"unparse_value": "blablabla, invalid value!"
}
```
```json
{
	"error": {
		"code": 200,
		"description": "Invalid request"	
	}
}
```
210 - Token is null or not founded in request.
**Example:**
```json
{
	"key": null
}
```
```json
{
	"error": {
		"code": 210,
		"description": "Token is null or not founded in request"	
	}
}
```
211 - Invalid token
**Example:**
```json
{
	"key": "Invalid token :)"
}
```
```json
{
	"error": {
		"code": 211,
		"description": "Invalid token"	
	}
}
```
212 - Access denied
**Example:**
```json
{
	"key": "9883bc5f0da8e41f",
	"Request": "SELECT * FROM passwords"
}
```
```json
{
	"error": {
		"code": 212,
		"description": "Access denied"	
	}
}
```
213 - Time of access is ended
**Example:**
```json
{
	"key": "9883bc5f0da8e41f",
	"Request": "SELECT * FROM tables"
}
```
```json
{
	"error": {
		"code": 213,
		"description": "Time of access is ended"	
	}
}
```
214 - Token has been removed
Ps. If token has been removed 14 days ago (You can recovery this token).
**Example:**
```json
{
	"key": "9883bc5f0da8e41f",
	"Request": "SELECT * FROM tables"
}
```
```json
{
	"error": {
		"code": 214,
		"description": "Token has been removed"
	}
}
```
220 - Only for read.
**Example:**
```json
{
	"key": "9883bc5f0da8e41f",
	"Request": "INSERT table (ID, name) WHERE (2, \"Rzekow\")"
}
```
```json
{
	"error": {
		"code": 220,
		"description": "Only for read"
	}
}
```
300 - Unknown error
Ps. errors in server, information about this errors sends in **/path/to/projectFolder/error logs/12_12_2021 12_12_00GMT.log**
**Example:**
```json
{
	"key": "9883bc5f0da8e41f",
	"Request": "INSERT table (ID, name) WHERE (2, \"Rzekow\")"
}
```
```json
{
	"error": {
		"code": 300,
		"description": "Unknown error",
		"detalis": "Traceback:\nblablabla python error"
	}
}
```
### Execute
Example of server url: **http://mywebsite.org/api/Response**
This method execute your SQL code in your server.
request body:
```json
{
	"key": "mykey",
	"Request": "SELECT * FROM table"
}
```
Request:
```json
{
	"response": [
		{
			"ID": 0, 
			"name": "Grzegorz"
		},
		{
			"ID": 1, 
			"name": "Hanz"
		}
	]
}
```
### fileExecute
Example of server url: **http://mywebsite.org/api/fileExecute**
This method execute your SQL code from file in your server.
request example:
```python
import requests, getpass
response = requests.post(
	'http://mywebsite.org/api/Response', 
	data={"key": getpass.getpass('Enter your API key: ')},
	file=open('/path/to/file.file', 'rb')
)
print(response.json())
```
output.log
```python
{
	'response': [
		{
			'ID': 0, 
			'name': 'Grzegorz'
		},
		{
			'ID': 1, 
			'name': 'Hanz'
		}
	]
}
```