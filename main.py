import numpy as np
import streamlit as st
import pandas as pd
import openai
from openai.embeddings_utils import get_embedding, cosine_similarity
import matplotlib.pyplot as plt
import plotly.express as px
from scipy import spatial
from sklearn.decomposition import PCA


# load the data
@st.cache_data
def load_data():
    data = pd.read_csv('answers_embedding.csv')  # This file contains the embeddings in csv format generated in the
    # generated in the .pynb file
    return data


def search_notebook(df, query, n, pprint=True):
    df['embedding'] = df['embedding'].apply(eval).apply(np.array)
    search_embeddings = get_embedding(query,
                                      engine="text-embedding-ada-002")
    df["similarity"] = df['embedding'].apply(lambda x: cosine_similarity(x, search_embeddings))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)
    )
    if pprint:
        print(results)
    return results


st.title("Semantic Search Engine")
user_secret = st.text_input(label=":blue[OpenAI API Key]", placeholder="Paste your API", type="password")
if user_secret:
    openai.api_key = user_secret

df = load_data()
# st.dataframe(df)
query = st.text_input(
    label=":blue[Search your query]",
    placeholder="Please, search with..."
)

search_button = st.button(label="Run", type='primary')
if query:
    if search_button:
        answer = search_notebook(df, query, 5, True)
        for index, row in answer.iterrows():
            st.write(row['similarity'], row['answer'])

