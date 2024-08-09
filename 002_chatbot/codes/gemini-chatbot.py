# %% [markdown]
# # Building a Chatbot using Gemini API

# %% [markdown]
# #### Task 0: Configure API key
# 
# The Python SDK for the Gemini API is contained in the google-generativeai package. 
#
# Install dependency using:
# !pip install google-generativeai
# 
# Do not check an API key into your version control system but assign it as an environment variable instead:
# export API_KEY=<YOUR_API_KEY>

# %% [markdown]
# #### Task 1: Initialize the model


import google.generativeai as genai

with open('gemini_api_key.txt','r') as file:
    API_KEY = file.read()
genai.configure(api_key=API_KEY)

# %% [markdown]
# Use system instructions to steer the behavior of a model

with open('pizzabot_system_instruction.txt', 'r') as file:
    sys_instr = file.read()

model=genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  system_instruction=sys_instr)

##### 2.1 Initialize the chat
chat = model.start_chat(history=[])

# %% 
# #### Task 2: Receive Prompts and Save Context and Generate chat responses

# **ChatSession** class of gemini enables us to have freeform conversation over multiple turns. We dont have to store conversation history as a separate list.
# Example: [Build an interactive chat](https://ai.google.dev/gemini-api/docs/text-generation?lang=python#chat)  
# The **ChatSession.send_message** method returns the same *GenerateContentResponse* type as **GenerativeModel.generate_content**. It also appends your message and the response to the chat history

def run_chat(value):
    response = chat.send_message(value)
    return f"Assitant: {response.text}"

# %%
#### Task 3: Build GUI 
import panel as pn
pn.extension() #initialization

chat_area_input = pn.chat.ChatAreaInput(value="Hi",placeholder="Type something, and press Enter to submit!") # intial value is a must, else 
output_markdown = pn.bind(run_chat, chat_area_input.param.value)
pn.Column(chat_area_input, output_markdown)

# %% [markdown]
# ### GEMINI Challenges
# 1. Making mistakes in mathematical calculations. When we ask it to re-check the calculation, it may give you a different total than the one it said earlier. 
# 2. Compared to openai api, I had to add more instructions for the chatbot to make it perform satisfactorily.
#    1. eg: While calculating the total bill of the customer, calculate the sum of price of all items ordered by the customer.
#    2. Please do not suggest dishes not in the menu mentioned below.
# 3. The instructions specify that the chatbot should always ask for toppings after a pizza order is placed. However, chatbot has missed it in some instances.

# %%



