# limesurveyrc2parser
Parser for the LimeSurvey Remote Control API version 2.0


## What Is It?
This library parses the LimeSurvey RC2 API PHP source code and extracts
the method names, arguments, argument types, docstrings and such to generate 
a Python wrapper client. Magical! :tada:

The template for generating Python methods and overall structure is based on 
another client, [LimeSurveyRC2API](https://github.com/lindsay-stevens/limesurveyrc2api). 
In comparison, the advantages of the generated client are that it'll have 
methods for available API endpoints, and by generating them it makes it easy to 
keep up to date with changes in the API. Disadvantages are that it won't have 
the error message detection stuff or integration tests - but maybe these could 
be new features of this library! (Open a PR! :thumbsup:).


## Usage
After installation, just run
* `lsrc2download` (download the PHP source code to 
   the current dir)
* `lsrc2generatepy` (reads the downloaded PHP source code
   and generates a `lsrc2client.py` file)

Or if you're using the repo without an install: `python script.py --download --generate`

Now, you are ready to go:
```
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
>>> import lsrc2client
>>> client = lsrc2client.LimeSurveyClient(url="https://myserver.org/ls/index.php/admin/remotecontrol")
>>> client.get_session_key("admin", "secretpassword")
'5km5r9eabuns6bst5jp4kdmrnif35hcz'
>>> session_key = '5km5r9eabuns6bst5jp4kdmrnif35hcz'
>>> client.list_surveys(session_key)
{'status': 'No surveys found'}
```


## Credentials
The template for generating the python client code is based on the LS RC2 API 
client by Lindsay Stevens [https://github.com/lindsay-stevens/limesurveyrc2api](https://github.com/lindsay-stevens/limesurveyrc2api)