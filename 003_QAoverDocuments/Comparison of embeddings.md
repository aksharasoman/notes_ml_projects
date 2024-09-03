## google-gen ai vs hugging face
### Google Gen AI
[Google Generative AI Embeddings | 🦜️🔗 LangChain](https://python.langchain.com/v0.2/docs/integrations/text_embedding/google_generative_ai/)
```
from langchain_google_genai import GoogleGenerativeAIEmbeddings  
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001") 
```

### Huggingface:
	
```
from langchain_huggingface import HuggingFaceEmbeddings 
embeddings = HuggingFaceEmbeddings()

```

### Responses
Both with google-gen ai model as llm

###### question: "What are the unsupervised algorithms discussed?"
**With Google Embedding:**
*Response:* The lecture discusses two examples of unsupervised learning algorithms. One example is used to group genes into clusters based on their responses to different experiments, and the other example is used to group pixels in images together.
