# projectSync
Creating project on github via python script and then cloning that project at the local system.
We can just run a single command with few arguments to start the process and rest will be done by the script.

Clone the repo then
Create a "creds.py" in you repo location, set below variables in that file

user = 'github-username'
pw = 'github-password'
token = 'github-token used for cloning the private repo'

Copy the function createProject from command.sh file
Paste that function in the ".bashrc" in your home location
Run command 'source .bashrc'
Now you can create a project by running below command
'createProject <project-name-in-qoutes> <project-description-in-qoutes>'

Will add visibilty arguments for the repo later on, as of now you can only make private repos.
