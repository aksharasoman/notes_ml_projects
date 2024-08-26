![[images/Pasted image 20240826113747.png]]

- [c]  these chains fails to preserve conversational history (soln: add memory).

#### Map-reduce:
```
qa_chain_mr = RetrievalQA.from_chain_type(
llm,
retriever=vectordb.as_retriever(),
chain_type="map_reduce"
)
result = qa_chain_mr({"query": question})
result["result"] 
```

Each retrieved document is send individually to the LLM and obtain a response. Then these responses are combined and send to the LLM as a final prompt.
- [c]  involves many more calls to the LLM => slower
- [p] can operate over many documents.
- [i] can use langchain platform (langsmith) to understand what is happening underneath the hood.

#### refine chain
- sequential calls to the LLM
- on each call, provide new doc as context along with original question and response from the previous LLM call (corresponding to prev doc) & instruct the LLM to refine the response only if necessary using the new context given.
- `chain_type = refine`