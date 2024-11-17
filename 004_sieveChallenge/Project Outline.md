##### Provided Content:
## Deliverables
1. Code repository with the demo (Build function on Sieve)
2. A Google Doc of a blog post (*A tutorial post*- break down how you did it and why it’s useful.)

## Project Tasks & Sieve Functions
- downloads a YouTube video
	- [sieve/youtube_to_mp4](https://www.sievedata.com/functions/sieve/youtube_to_mp4)
- summarizes it into a conversational style
	- [sieve/visual-qa](https://www.sievedata.com/functions/sieve/visual-qa) (1 use case is Video Summarization)
		- as ‘visual-qa’ to “generate summary in conversational style” (prompt)
	- *Other Summary Generation Options (not using)*
		- [sieve/transcript-analysis](https://www.sievedata.com/functions/sieve/transcript-analysis) : Given a video or audio, generate a title, chapters, summary, tags, and highlights. (if `generate_summary` is True)
		- [sieve/describe](https://www.sievedata.com/functions/sieve/describe) : Generate audio-visual descriptions of videos with timestamp references. (Spoken Context: This option dictates the usage of the speech in the video to influence the final summary. If set to `False`, the summary will be generated based on only the visuals seen across the video.)
- converts the summary into conversation speech between two people (text to speech)
	- [sieve/tts](https://www.sievedata.com/functions/sieve/tts)
- bonus: [make a talking avatar](https://www.sievedata.com/blog/portrait-avatar-talking-head-video-api-hedra-infinity) or a set of talking avatars speaking that speech
	- [sieve/portrait-avatar](https://www.sievedata.com/functions/sieve/portrait-avatar)

---
## Solution 
### Title
How to Convert a YouTube Video as a Conversation Between Two Talking Avatars?
Convert a YouTube Video into a Conversational Exchange Between Two Talking Avatars
### Pipeline

| Step | Task                                                                                                                                                           | Process                                                                            | Remarks                                                        | Compare                                                       |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------- |
| 1    | downloads a YouTube video                                                                                                                                      | [sieve/youtube_to_mp4](https://www.sievedata.com/functions/sieve/youtube_to_mp4)   |                                                                |                                                               |
| 2    | summarizes it into a conversational style                                                                                                                      | [sieve/visual-qa](https://www.sievedata.com/functions/sieve/visual-qa)             | Prompt: Summarize the video as a conversation between 2 people | 1. flash and pro models<br>2. Prompt without the word “video” |
| 3    | converts the summary into conversation speech between two people                                                                                               | [sieve/tts](https://www.sievedata.com/functions/sieve/tts)                         |                                                                |                                                               |
| 4    | [make a talking avatar](https://www.sievedata.com/blog/portrait-avatar-talking-head-video-api-hedra-infinity) or a set of talking avatars speaking that speech | [sieve/portrait-avatar](https://www.sievedata.com/functions/sieve/portrait-avatar) |                                                                |                                                               |
| 5    | Join generated videos                                                                                                                                          | ffmpeg concat                                                                      |                                                                |                                                               |

---
##### Content in Progress:
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
- What is fps (The framerate to use when processing a video file) in sieve/visual-qa function?
	- Let's set the `fps` param to be 1 since there aren't instant changes in between the frames.
	- When i set the input videos frame rate (=30), func threw error. 

---
## Extensions Possible?
- Can I parallelize processing - tts and avatar generation of individual turns ?
	- ref: [Example: Parallelized Face Detection - Sieve](https://docs.sievedata.com/guide/examples/parallelized-face-detection)
	- NOT SURE if push inside a sieve function works - not sure how to make code to wait for all parallel processing results to arrive.
- chatTTS
- conversational talking-listening heads: check challenge
## Challenges
- Multiple-speaker support!
	- text to speech : retaining 2 conversational style with 2 people (tts doesnt take 2 people conversations -dialogues) : tts works only for monologues?
		- For multi-speaker support, you might need to:
		1. Use different reference audio files for each speaker.
		2. Run the TTS function multiple times with different settings for each speaker.
		3. Combine the resulting audio files as needed for your application.
	- sieve/portrait avatar  documentation says
		- Ensure there is only a single primary speaker in the audio.
	-  currently *dubbing* is only api seen with multiple speaker support (doubtful)
		- The `edit_segments` parameter allows you to selectively dub or edit specific portions of the media. useful for adding custom translations for specific segments
	**Solution:** 
	- Use  ‘*sieve/visual-qa*’ to “generate summary as a conversation between 2 people” (prompt) → output in text format (conv_summary_text)
	- feed each turn of output (conv_summary_text) to *sieve/tts* with either speaker1 or speaker2 voice iteratively → generate audio1, audio2, audio3, .., (Odd number files belong to speaker1 and even numbered files belong to speaker2).
	- For each audio file, use *sieve/portrait-avatar* generate a video file. Use avatar1 for speaker1’s audio files(odd numbered) and avatar2 for speaker2’s audio files (even numbered). 
	- Join the generated video files in sequential order to form a single video file using ffmpeg; Ref: [[Merge multiple video files using ffmpeg]]
- Video and audio asynchronous while merging videos 
	- To verify if all input videos have the same codec, resolution, and frame rate,
	`ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate -of csv=p=0 input_video.mp4`
	- Issue: different frame rates of videos generated by sieve/portrait-avatar)
	- *Solution*: Use FFmpeg to re-encode the videos to a uniform frame rate.
	`ffmpeg -loglevel warning -i video4.mp4 -r 30 -c:v libx264 -preset fast -crf 23 -c:a aac encoded_video4.mp4`
	- now, to merge the videos:
	`ffmpeg -f concat -safe 0 -i file_list.txt -loglevel warning -c copy merged_output.mp4
-



	






	
	