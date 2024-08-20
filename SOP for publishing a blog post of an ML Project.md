####  Deploy github repo for codes
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
7. Create `index.qmd` file with required yaml header (copy from a published index file)
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
	3. Main sections in index.qmd (article main page )
		1. Introduction ← github repo readme
		2. Major implementation aspects
		3. Problem Statement/Objective
		4. Tasks
		5. Code (provide github repo link)
		6. Results (snapshot)
		7. Key takeaways
		8. Challenges Encountered
		9. Skills Acquired (display in an eye-catching way: create using canva etc.)
1. Run: git-publish “commit-message” to upload the blog post.
2. Add blog link to Github Readme
3. Remove temp files and images that are not required anymore from project folder,Desktop and Downloads.
4. Do final round of ‘git push’ in codes & blog folders.

> [!caution] File-naming 
> To include any qmd file other than index.qmd to the listing page, start the file name with in_ eg: ‘in_concepts.qmd’

##### Tips
1. The way obsidian notes are organized during the project implementation: 
	1. *A home file* that contains links to all other notes within the folder. → It becomes easier to have an overview of all aspects of this project in one place, eliminating the need to go through each file in the folder while preparing the article.  Eg: [[(ML Project) Build your own chatbot]]
	2. [[Folder Structure for ML Project]]

