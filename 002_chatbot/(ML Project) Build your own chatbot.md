---
tags:
  - mlproject
  - gen-ai
title: Build a chatbot for <?>
author: Akshara Soman
---

It is fun to build.

### Background
[[Key Aspects of Building a Chatbot.md]]
[[Master Chatbot Development with DeepLearning.AI Courses]]
[[Quick Guide on using Gemini for Conversational Tasks]]
[[Miscellaneous Coding Issues]]
[[Learnings from this project]]

### Implementation - Aspects to Consider
1. OpenAI API key used in deeplearning.ai course is not free. Hence, instead of openai, use a free LLM API - 
	1. [[Gemini LLM API key]] : free-tier option available
	2. Another option: [Llama API](https://docs.llama-api.com/quickstart) free in its beta version (now: jul 2024)::  [Obtaining an API Token - Llama API](https://docs.llama-api.com/api-token) 
3. Using [panel](https://panel.holoviz.org/index.html) python library to build chat GUI 


Egs: [barista bot](https://aistudio.google.com/app/prompts/barista-bot)

### Objective
Build a chatbot for a pizzeria for taking orders using Gemini 1.5 Flash model and build GUI using "Panel" library
#### Tasks:
1. import necessary LLM libraries and api key
2. configuration
3. function to receive a list of prompts & pass to LLM & return response
4. function to collect context 
5. build chat interface 
6. host it in server: [[Deploy an App built using Panel using Ploomber]]
	1. Another option: [Deploy a Python Visualization Panel App to Google Cloud Run](https://towardsdatascience.com/deploy-a-python-visualization-panel-app-to-google-cloud-ii-416e487b44eb) - didn’t  do it because of the cost involved. It can be deployed only for a limited duration of time.
	2. [Panel — Ploomber Docs](https://docs.cloud.ploomber.io/en/latest/apps/panel.html)

	
	Pizzabot deployed:[Order bot of Pizza Paradise!](https://broken-wildflower-4698.ploomberapp.io/app)

###### Follow-up queries:
1. Llama model vs gemini - performance comparison for conversational tasks
2. Any other chatbot application related to my life : book suggestion bot?? (tough)


### Reference: 
[Your Guide to Generative AI Courses - DeepLearning.AI](https://www.deeplearning.ai/resources/generative-ai-courses-guide/): outlines courses by DL.ai on chatbots.


