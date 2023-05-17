# AI-Semantic-Search
Semantic Search Engine using OpenAI and streamlit

Want to have a search engine that understands you the best? AI semantic search engine definitely will do that! Here we can search any query and the search engine will give you the best possible results based on understanding of the search query and not only based on keywords.

It even includes multi language support using OpenAI translation, which makes searches possible in any language.
<h2>Technology used</h2>
<h3>Frontend</h3>

1. Streamlit (an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science)

<h3>Backend</h3>

1. OpenAI API (for text embeddings and translation)

2. Pinecone API (for storing the vector database having the embeddings)

<h2>How it works?</h2>
The project uses the wiki_qa (https://huggingface.co/datasets/wiki_qa/viewer/default/train?row=0) dataset out of which 15000 entries have been used.
