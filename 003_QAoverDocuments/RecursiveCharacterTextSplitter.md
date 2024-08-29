from langchain.text_splitter

- **Recursive Splitting**: The `RecursiveCharacterTextSplitter` works by recursively breaking down text based on specified characters or tokens, starting with larger units (e.g., paragraphs) and then moving to smaller units (e.g., sentences or words) until the chunks meet a specified size constraint.
- **Breakpoints**: The splitter tries to split the text at natural breakpoints, such as paragraph breaks or sentence boundaries, to ensure that the chunks make sense contextually and don't cut off in awkward places.

‘copied from chatgpt’