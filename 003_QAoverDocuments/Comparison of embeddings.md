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

###### questions: 
1. What are the unsupervised algorithms discussed?
2. Who are the TAs of the course?
3. Who is the instructor of the course?
4. Who is the TA specialized in neuroscience?

**With Google Embedding:** *Faster* (5.5s for load_db function); *Concise answers*
1. The lecture discusses two examples of unsupervised learning algorithms. One example is used to group genes into clusters based on their responses to different experiments, and the other example is used to group pixels in images together.
2. The TAs of the course are Paul Baumstarck, Catie Chang, Tom Do, Zico Kolter, and Daniel Ramage. 
3. The instructor of the course is Andrew Ng. 
4. Catie Chang is the TA specialized in neuroscience. She applies machine learning algorithms to understand the human brain. 


**With Huggingface Embedding:** *BETTER* 
1. The text discusses two unsupervised algorithms: clustering and independent component analysis. Clustering is used to find structure in data by partitioning it into groups, while independent component analysis is used to separate mixed signals into their original sources.
2. The TAs for the course are Paul Baumstarck, Catie Chang, Tom Do, Zico Kolter, and Daniel Ramage. Each TA specializes in a different area of machine learning, such as computer vision, neuroscience, computational biology, robotics, and natural language processing. 
3. The instructor of the course is Andrew Ng. He is also referred to as the "Instructor" in the provided text.
4. Catie Chang is the TA specialized in neuroscience. She applies machine learning algorithms to understand the human brain. 

