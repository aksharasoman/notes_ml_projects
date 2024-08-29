*From chatgpt:*
### Understand the Document Structure:
1. Context Type (text, tables, images etc)
2. **Structure:** Identify the structural elements like headings, paragraphs, bullet points, and tables. You might want to split text at natural breaks, like paragraphs or sections.
### Types of Text Splitters:
- **By Paragraphs:** If your PDFs are well-structured with clear paragraph breaks, splitting by paragraphs is often effective. This ensures that each chunk maintains a coherent thought or idea.
- **By Sentences:** For more granular control, splitting by sentences can be useful, especially if the text is dense and each sentence carries significant meaning.
- **By Character Length:** This method splits text based on a fixed number of characters. It can be useful when paragraphs or sentences vary greatly in length, but it may result in cutting off mid-sentence or mid-paragraph.
- **By Tokens:** Splitting by tokens (e.g., words or subword units) is particularly useful if you're working with models that have token limits. This ensures that each chunk stays within the model's input capacity.
- **Custom Splitters:** For PDFs with non-standard layouts (e.g., tables, images with captions), you might need custom splitters that consider visual elements or use more sophisticated methods like layout parsing.
### Experimentation:
- **Test Different Splitters:** use evaluation metrics like retrieval accuracy or the coherence of generated text
- **Check Chunk Quality:** Ensure that the chunks make sense on their own and aren’t too fragmented or incomplete.
### Practical Tips:
- **Hybrid Approach:** Combine splitters, like splitting by paragraphs first and then refining by sentence length or tokens within each paragraph.
- **Preprocessing:** Clean the text before splitting, removing unnecessary artifacts like headers, footers, and page numbers that are common in PDFs.