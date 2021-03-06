### Useful commands

- `python3 -m venv venv`
- `. venv/bin/activate`
- `pip3 install Flask`
- `pip3 freeze > requirements.txt`
- `pip install -r requirements.txt --no-index --find-links file:///tmp/packages` --> install all requirements

First you have to activate python environment with command `source python/bin/activate` command from root folder. To deactivate you can use `deactivate` or `conda deactivate` command from root folder.

### Running server

- `export FLASK_APP=server.py` to setup FLASK_APP environment variable
- `export FLASK_ENV=development` to enable development mode and reloading of server
- `flask run` to run the python server

If you want to add permanently the environment variables you could add the command `export FLASK_APP=server.py` to the `~/.profile` file

### Deploy to heroku

Commit your changes and then run CLI command

- `git push origin master && git push heroku master`

### Links

- `https://flask.palletsprojects.com/en/1.1.x/installation/#installation`
