1. `python3 -m venv .venv` 
	1. The second argument is the location to create the virtual environment. Generally, you can just create this in your project and call it `.venv`.
2. `source .venv/bin/activate`
3. Prepare pip: 
`python3 -m pip install --upgrade pip`
`python3 -m pip --version`
4. Prepare a 'requirements.txt' file 
`python3 -m pip install -r requirements.txt` 
OR 
5. Install packages individually (pip install <>) & generate a list of required packages at the end of the project:
```
pip-chill --no-chill -v > requirements.txt
```
- `--no-chill` : does not include `pip-chill` itself in the output
- `-v` : outputs the indirect dependencies as well, but commented. Therefore it is easy to keep track of them.
- nb: pip install pip-chill

Which will output a list of package specifiers as 'Requirements Files' that can re-create the exact versions of all packages installed in an environment.