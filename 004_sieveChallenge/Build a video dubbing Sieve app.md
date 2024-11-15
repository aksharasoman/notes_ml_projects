- An example app to help start.
- (tutorial post already available in sieve website)

## Problem Statement
 Create an application that automatically dubs a video of a person speaking into another language!

## Process
An input video → transcribe it → translate that text to another language → generate text-to-speech of that translated text →  have the original video lipsync to the new audio.

Input video → Transcribe → Translate to new lang → Generate Speech for translated text (TTS) → lipsync with org. video

## Sieve Functions
1. **WhisperX**: an audio transcription model (sieve/speech_transcriber)
2. **SeamlessT2T**: a text-to-text translation model (sieve/seamless_text2text)
3. **XTTS-V1**: a text-to-speech model (sieve/tts)
4. **Sieve Video Retalker**: an optimized version of video retalker for lipsyncing –> used upgraded function: ‘lipsync’ ("sieve/lipsync")

## Building the app from scratch
Source: [Example: Video Dubbing - Sieve](https://docs.sievedata.com/guide/examples/video-dubbing#building-the-app-from-scratch)

