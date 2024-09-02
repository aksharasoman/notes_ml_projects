–→ [[Retrieval Augmented Generation]]
- Popular packages: LangChain, LlamaIndex
- For basics of RAG: GenAI (NG) course notes in Goodnotes
### Relevant Course
[[LangChain Course Overview]]
Tutorials:
- [Conversational RAG](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/),
- [Build a PDF ingestion and Question/Answering system | 🦜️🔗 LangChain](https://python.langchain.com/v0.2/docs/tutorials/pdf_qa/)

### Problem Statement
Build a chatbot to chat with your publications(pdf documents) - deploy it in ojus’s or my website(?) 

### Course of Action 
- [x]  Do the course to understand [[RAG Pipeline with LangChain|RAG Pipeline]]
- [ ] Adapt the pipeline for our application (note down necessary changes and details needed for each step): see ''Tasks” section below

### Tasks
1. Document Loading
	1. import pdf documents of publications 
2. Text Splitting
	- [?] [[How to decide which text splitter is suitable for a RAG application?]] : i need to do these comparisons in our work to understand better. but let’s keep that research in hold. 
	- [[RecursiveCharacterTextSplitter]]
3. Embedding 
	1. choose an llm based embedding from langchain.embeddings
	- [?] Can we use OpenAIEmbeddings even if we are using another llm model as chatbot?
2. Vectorstore - chroma
	1. Used DocArrayInMemorySearch instead: not saving the vectordb for future use 
		1. faster than Chroma 
3. Retrieval : SelfQueryRetriever 
	1. Ensure it is choosing correct paper when the paper is specified in the question.
	- [?] Do i need to use compressionRetriever (with MMR) as well? Does it have capability of understanding the meta data?
4. LLM : choose a suitable and free api chatmodel from the [langchain list](https://python.langchain.com/v0.2/docs/integrations/chat/)
	- Google-api key is free: [langchain-google-genai](https://python.langchain.com/v0.2/api_reference/google_genai/chat_models/langchain_google_genai.chat_models.ChatGoogleGenerativeAI.html) 
	- [?] Is there any better chatmodel with free api key?:  [best chat models - Google Search](https://www.google.com/search?q=which+are+the+best+chat+models&ie=UTF-8)
	- Include memory (chat history) capability
5.  Build GUI (panel based)
6. Test the chatbot

More detailed steps and personal tasks:
- [x] Copy the last part of code from chatbot lecture
- [ ] load_db()
	- [ ] embeddings = OpenAIEmbeddings() Can we use this with gemini llm
	- [ ] Use another llm chain: # create a chatbot chain. 
	qa = ConversationalRetrievalChain.from_llm(….)
- [ ] understand cbfs class- using code-explainer chatgpt
	- [ ] change _init_ laoded pdf file 
- [ ] understand chatbot creation code 

### Choosing LLM Chatmodel
- Choosing Google model since I have used it in my previous project and its api has free-tier.
> We recommend individual developers to start with Gemini API (`langchain-google-genai`) and move to Vertex AI (`langchain-google-vertexai`) when they need access to commercial support and higher rate limits. 
> by[Google | 🦜️🔗 LangChain](https://python.langchain.com/v0.2/docs/integrations/platforms/google/)

- Comparison of Google AI vs Vertex AI: [Gemini on Google AI vs Vertex AI ](https://cloud.google.com/vertex-ai/generative-ai/docs/migrate/migrate-google-ai) 
- 
### Main Python Libraries Used:
Langchain, Panel and [[Param Library]]


### Doubts
- in rag pipeline, is the query to the vector store different from the prompt to the LLM?
	- same. human question is given to vector store as query. then retrieved documents and original human question are fed to the LLM.


### Suitable titles for this project / blog post
- Conversational AI with RAG
- Conversational RAG
- RAG with memory
- Integrating Conversational History into the RAG Pipeline
- Enhancing RAG Pipeline with Conversational History

### Challenges
1. Which chatmodel (LLM)
2. Which [embedding](https://python.langchain.com/v0.2/docs/how_to/embed_text/)
	1. OpenAIEmbeddings requires open-api-key which is paid. So opting for huggingface embeddings
### Component Analysis / Follow-up Experiments
- [ ] Compare the performance of chroma vs DocArrayInMemorySearch vector db (wrt speed, ?)
- [ ] 
