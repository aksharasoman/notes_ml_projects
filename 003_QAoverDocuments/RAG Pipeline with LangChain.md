
![1000](images/(ML%20Project)%20Question%20Answering%20Over%20Documents%2022Aug24_07-41.excalidraw)


### Different Retrieval Methods
![1000](images/RAG%20Pipeline%20with%20LangChain%2023Aug24_07-14.excalidraw)

#### Maximum Marginal Relevance (MMR) 
![800](images/RAG%20Pipeline%20with%20LangChain%2023Aug24_07-34.excalidraw)

qa_chain_mr = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever(),
    chain_type="map_reduce"
)

Map-reduce: Each retrieved document is send individually to the LLM and obtain a response. Then these responses are combined and send to the LLM as a final prompt.
- [c]  involves many more calls to the LLM => slower
- [p] can operate over many documents.
- [ ]
### What if the retrieved document splits exceed the LLM’s context window?
Self-note: I do not understand what each does. (no explanation in the course video)
![[images/Pasted image 20240826113747.png]]