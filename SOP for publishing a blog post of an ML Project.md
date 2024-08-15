1. Clean up codes directory of the project
	1. location:~/2.Projects/codes_ml_projects/<00x_project>|
	- keep the required files only
	- init git repo in this directory
2. Create README file for the git repo
	- Brief description of project : provide it to Chatgpt and ask to create github repo Readme
	- Files' description
	- Further information:link to blog post of this project.
3. Create a repo in github.com 
4. Link remote repo and local repo (Run this in local dir commandline)
```
git remote add origin remote-repo-url
git remote -v 
git add .
git commit -m "First Commit"
git pull origin main
git push -u origin main
```
---
#### Create blog post:
5. Create project folder in quartofiles dir.
``` 
cd ~/2.Projects/webpage_github/quartoFiles/posts
mkdir <0xx_project-name>
cd <0xx_project-name>
```
6. Open vscode: `code .`
7. Create `index.qmd` file with required yaml header (copy from another )
8. Find a suitable thumbnail image, if there is not any in the project.
9. Prepare overview content for index.qmd (see readme.md of github repo.)
	1. Keep the obsidian notes and codes folder (vs code) of the project open.
	2. Copy jupyter notebook (if any) to blog folder and add yaml header.
		```
		---
		title: Quarto Basics
		format:
		 html:
		  code-fold: true
		jupyter: python3
		---	
		```

	
		```
		quarto render hello.ipynb --to html
		quarto preview hello.ipynb
		```

3. Run: git-publish “commit-message” to upload the blog post.
Z.  Add blog link to Github Readme
