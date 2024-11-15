## Deliverables
1. Code repository with the demo (Build function on Sieve)
2. A Google Doc of a blog post (*A tutorial post*- break down how you did it and why it’s useful.)

## Project Tasks & Sieve Functions
- downloads a YouTube video
	- [sieve/youtube_to_mp4](https://www.sievedata.com/functions/sieve/youtube_to_mp4)
- summarizes it into a conversational style
	- [sieve/visual-qa](https://www.sievedata.com/functions/sieve/visual-qa) (1 use case is Video Summarization)
	- [sieve/transcript-analysis](https://www.sievedata.com/functions/sieve/transcript-analysis) : Given a video or audio, generate a title, chapters, summary, tags, and highlights.
	- [sieve/describe](https://www.sievedata.com/functions/sieve/describe) : Generate audio-visual descriptions of videos with timestamp references.
- converts the summary into conversation speech between two people
	- 
- bonus: [make a talking avatar](https://www.sievedata.com/blog/portrait-avatar-talking-head-video-api-hedra-infinity) or a set of talking avatars speaking that speech

## Detailed Steps
- Sieve [Sign up](https://www.sievedata.com/dashboard) and get your [API key](https://www.sievedata.com/dashboard/settings) (source: [Getting Started](https://docs.sievedata.com/guide/intro#getting-started))
- Create Project Folder (/Users/aksharas/2.Projects/codes_ml_projects/004_sieveChallenge)
- Create a new Python environment named ‘sieve’
	- python -m venv sieve 
	- source sieve/bin/activate
	- In VS code, Cmd"+Shift+P - Select Python Interpreter - choose new env py from list
- Install the Sieve Python client
	- `pip install sievedata`
- Login with your API key
	 - `sieve login`
	 - If you face [[“SSL CERTIFICATE_VERIFY_FAILED” error]]
- input video: [2-Minute Debate: Is Smart Tech Making Us Dumb? - YouTube](https://youtu.be/mh8AfvllYwA) 

## Questions
- I could not find “sieve/describe” function listed in explore page ([Explore | Sieve](https://www.sievedata.com/explore)). I got to know about it from discord channel. Where do I find such functions listed?