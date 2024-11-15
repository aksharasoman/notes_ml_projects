## Deliverables
1. Code repository with the demo (Build function on Sieve)
2. A Google Doc of a blog post (*A tutorial post*- break down how you did it and why it’s useful.)

## Project Tasks & Sieve Functions
- downloads a YouTube video
	- 
- summarizes it into a conversational style
- converts the summary into conversation speech between two people
- bonus: [make a talking avatar](https://www.sievedata.com/blog/portrait-avatar-talking-head-video-api-hedra-infinity) or a set of talking avatars speaking that speech

## Steps
1. Sieve [Sign up](https://www.sievedata.com/dashboard) and get your [API key](https://www.sievedata.com/dashboard/settings) (source: [Getting Started](https://docs.sievedata.com/guide/intro#getting-started))
2. Create Project Folder (/Users/aksharas/2.Projects/codes_ml_projects/004_sieveChallenge)
3. Create a new Python environment named ‘sieve’
	1. python -m venv sieve 
	2. source sieve/bin/activate
	3. In VS code, Cmd"+Shift+P - Select Python Interpreter - choose new env py from list
4. Install the Sieve Python client
	`pip install sievedata`
5. Login with your API key
	 `sieve login`
	 If you face [[“SSL CERTIFICATE_VERIFY_FAILED” error]]
6. 