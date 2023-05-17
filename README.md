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
The project uses the wiki_qa (https://huggingface.co/datasets/wiki_qa/viewer/default/train?row=0) dataset out of which 15000 entries have been used. The userinterface(UI) is build using the streamlit where the user needs to use the openai API key for using the text-embedding-ada-002(for text embeddings) and text-davinci-003(for translation), and should enter the search query in the fields available. The model will display the top 5 best match results. In the google collab the codes for text embeddings of the entire dataset that is given. These text embeddings are stored in the vector database in Pinecone. When the user provides a search query the model will create its embeddings and match with the already existing embeddings. Based on this the model will display the top 5 matches. I have also added the feature of translation so that searches in multiple languages is possible. It will first translate the search query in english and then embedded follows the above said procedure.
