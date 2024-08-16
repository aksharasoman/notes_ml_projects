### Key Aspects of Building a Chatbot
- **Training**: LLMs have 2 phases of training.
	- Pre-training: a model is trained to predict the next word
	- Fine-tuning: tunes a model to a particular task.
		- For chat models: task is *Conversational*
- **Memory**
	- To remember turns of a conversation, we can add memory *(See LangChain course by [[deeplearning.ai Courses for developing a chatbot|dl.ai]]) 
		- LLM does not have memory on its own.
- **Production**
	- Needs to be monitored to ensure safe and non-toxic conversations *(See lecture "Moderation" in course 3 in the list given here:*  [deeplearning.ai Courses for developing a chatbot](deeplearning.ai%20Courses%20for%20developing%20a%20chatbot.md) )

Resource: [[deeplearning.ai Courses for developing a chatbot]]

---
## ARTICLE WRITE-UP

Building an effective chatbot involves understanding various key aspects, including the training of Large Language Models(LLMs), incorporating memory, and production considerations.

#### Training
Language models (LLMs) undergo two main phases of training:

1. **Pre-training**: In this phase, the model learns to predict the next word in a sentence using large-scale datasets. This helps the model acquire general understanding of language.
    
2. **Fine-tuning**: This phase adapts the model to specific tasks. For chat models, the fine-tuning task is typically **Conversational**, where the model learns to engage in dialogues effectively.

#### Memory
LLMs do not inherently possess memory, meaning they cannot remember previous interactions or conversations. Developers can incorporate memory features to maintain context throughout the interaction.

For more insights, see the [LangChain course by deeplearning.ai](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/)on developing chatbots.

#### Production
When deploying a chatbot to production, it's essential to ensure that it provides safe and non-toxic responses.

For more details on setting up effective moderation practices, refer to the ‘Moderation’ chapter in the [Building Systems with ChatGPT](https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/) course by deeplearning.ai.


For more details: [[deeplearning.ai Courses on developing a chatbot]]