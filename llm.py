import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_ibm import WatsonxLLM
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes


# tag::llm[]
openai_llm = ChatOpenAI(
    openai_api_key=st.secrets["OPENAI_API_KEY"],
    model=st.secrets["OPENAI_MODEL"],
)
watsonx_llm = WatsonxLLM(
    model_id=ModelTypes.FLAN_UL2.value,
    url=st.secrets["WATSONX_URL"],
    apikey=st.secrets["IBM_CLOUD_API_KEY"],
    project_id=st.secrets["WATSONX_PROJECT_ID"]
    )
# end::llm[]

# tag::embedding[]
openai_embeddings = OpenAIEmbeddings(
    openai_api_key=st.secrets["OPENAI_API_KEY"]
)
# end::embedding[]
