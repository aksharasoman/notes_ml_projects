
Here is a list of some errors that occurred during the implementation of the project. If you encounter them during your own implementation, please refer to the solutions or workarounds I used below.

-  Warning Message from Gemini model when we incorporate a system instruction to the model initialization. 
	-> The warnings disappeared when I installed the following package: `grpcio==1.60.1`
-  VSCode Shortcuts Triggered When Typing on TextInput: When I type letter 'a' in the textinput (panel library element), Jupyter notebook creates new code cell.
	-> As a temporary solution, we can I disable "Jupyter Keymap" (Search for "keymap" in extensions and disable it) or edit problematic keymappings and assign another one.
- Choosing a virtual environment outside your current directory (workspace) in vscode: Cmd+Shift+P -> Select Python Interpreter -> Type in the location of the python in your virtual env. (eg: '~/2.Projects/.venv/bin/python3.12) 
