from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

def get_entities(text):
    load_dotenv()
    model = ChatGroq(model="llama3-8b-8192")
    promt_temp = ChatPromptTemplate.from_messages([('system',"You are a helpful assistant."),
           ('human',"extract the key entities from: {text}")])
    
    chain = promt_temp | model | StrOutputParser()
    return chain.invoke({'text':text})


def summarize(text):
    load_dotenv()
    model = ChatGroq(model="llama3-8b-8192")
    promt_temp = ChatPromptTemplate.from_messages([('system',"You are a helpful assistant."),
           ('human',"summarize the following: {text}")])
    
    chain = promt_temp | model | StrOutputParser()
    return chain.invoke({'text':text})
    
