![[images/Pasted image 20240826143245.png|400]]

![[images/Pasted image 20241112102607.png]]

- contextualize query prompt : modify the prompt to incorporate both current human input and chat history.
	- in the following order: [system message, chat_history, human message]
	- prompt template:
```
	q_prompt = ChatPromptTemplate.from_messages(
		[ ("system",system_prompt),
		 MessagesPlaceholder("chat_history"),
		 ("human","{input}") ])
```
- Chain:
```
history_aware_retreiver =      create_history_aware_retriever(llm, retriever, q_prompt)
```

#### Where do we keep chat_history in our application?
Use LangGraph which has builtin memory

