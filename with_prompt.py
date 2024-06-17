##integrate our code OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI 

from langchain import PromptTemplate
from langchain.chains import LLMChain


# to store the conversation in memory --- conversation buffer memory


from langchain.memory import ConversationBufferMemory 


import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

## streamlit framework

st.title('Celebrity Search Result')
st.title ('Langchain Demo with OpenAI APT')
input_text=st.text_input("Search the topic you want")

# Prompt Templates

first_input_prompt = PromptTemplate(
    input_variables = ['name'],
    template = "Tell me about {name}"

)

## OpenAI LLMS

llm = OpenAI(temperature = 0.8)
chain = LLMChain(llm=llm,prompt = first_input_prompt,verbose = True)




if input_text:
    st.write(chain.run(input_text))
