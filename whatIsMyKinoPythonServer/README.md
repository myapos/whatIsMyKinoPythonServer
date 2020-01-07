### In order to run python server give the following commands

First you have to activate python environment with command `source python/bin/activate` command from root folder. To deactivate you can use `deactivate` command from root folder.

- `cd python` to visit python folder which contains python server
- `export FLASK_APP=server.py` to setup FLASK_APP environment variable
- `flask run` to run the python server

If you want to add permanently the environment variables you could add the command `export FLASK_APP=server.py` to the `~/.profile` file
