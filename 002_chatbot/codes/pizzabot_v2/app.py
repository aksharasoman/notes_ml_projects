# %% [markdown]
# # Building a Chatbot using Gemini API

# %% [markdown]
# #### Task 0: Configure API key
# 
# The Python SDK for the Gemini API is contained in the google-generativeai package. 
# 
# Install dependency using:
# *pip install -q -U google-generativeai
# *
# 
# Do not check an API key into your version control system but assign it as an environment variable instead:
# export API_KEY=<YOUR_API_KEY>

# %% [markdown]
# #### Task 1: Initialize the model

# %%
# !pip install google-generativeai
import google.generativeai as genai

with open('gemini_api_key.txt','r') as file:
    API_KEY = file.read()
genai.configure(api_key=API_KEY)

# %% [markdown]
# Use system instructions to steer the behavior of a model

# %%
# Using a context manager to open the file
with open('pizzabot_system_instruction.txt', 'r') as file:
    sys_instr = file.read()

# %%
model=genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  system_instruction=sys_instr)

##### 2.1 Initialize the chat
chat = model.start_chat(history=[])

# %% [markdown]
# #### Task 2: Receive Prompts and Save Context and Generate chat responses
# *I searched for gemini api help docs.* 
# 
# **ChatSession** class of gemini enables us to have freeform conversation over multiple turns. We dont have to store conversation history as a list.
# 
# Example: [Build an interactive chat](https://ai.google.dev/gemini-api/docs/text-generation?lang=python#chat)  

# %% [markdown]
# The **ChatSession.send_message** method returns the same *GenerateContentResponse* type as **GenerativeModel.generate_content**. It also appends your message and the response to the chat history

# %%
import panel as pn
def run_chat(value,user,instance):
    response = chat.send_message(value)
    # return f"{response.text}"
    return pn.chat.ChatMessage(response.text, user="Pizza Bot", avatar="🐼")

# %% [markdown]
# #### Task 3: Build GUI 

# %%


pn.extension("perspective")#initialization

chat_bot = pn.chat.ChatInterface(help_text="Welcome to Pizza Paradise! What would like to order?",callback=run_chat,
                                 max_height=500,show_rerun=False,show_clear=False,
                                 )


# %% [markdown]
# #### GEMINI Challenges
# 1. Making mistakes in mathematical calculations. When we ask it to re-check the calculation, it may give you a different total than the one it said earlier. 
# 2. Compared to openai api, I had to add more instructions for the chatbot to make it perform satisfactorily.
#    1. eg: While calculating the total bill of the customer, calculate the sum of price of all items ordered by the customer.
#    2. Please do not suggest dishes not in the menu mentioned below.
# 3. The instructions specify that the chatbot should always ask for toppings after a pizza order is placed. However, chatbot has missed it in some instances.

# %% [markdown]
# #### Task 4: Serving the Notebook

# %% [markdown]
# We’ll organize our components in a nicely styled template (MaterialTemplate) and mark it .servable() to add it to our served app

# %%
pn.template.MaterialTemplate(
    site="Panel",
    title="Order bot of Pizza Paradise!",
    main=[chat_bot],
).servable(); # The ; is needed in the notebook to not display the template. Its not needed in a script

# %% [markdown]
# serve the app with:
# 
# panel serve gemini-pizza-chatbot_v2.ipynb --autoreload



