from tess import ocr
from chains.parallel_chain import summarize,get_entities 
from langchain.schema.runnable import RunnableParallel
from langchain.schema import AIMessage,SystemMessage,HumanMessage
from langchain_groq import ChatGroq

text_list = ocr()

history = []

chain = RunnableParallel(branches={'entities':get_entities, 'summarized':summarize})

sysmsg = "You are a helpful assistant. Answer the following based on the context below.\n"

for i in range(len(text_list)):
    result = chain.invoke(text_list[i])
    sysmsg+=f"\n{i+1}\n"
    sysmsg+=f"text:{text_list[i]}\n"
    sysmsg+=f"entities:{result['branches']['entities']}\n"
    sysmsg+=f"summary:{result['branches']['summarized']}\n"
history.append(SystemMessage(content=sysmsg))
#print(sysmsg)

model = ChatGroq(model='llama3-8b-8192')

while True:
    query = input()
    if query == 'exit':
        break

    history.append(HumanMessage(content=query))
    aireply = model.invoke(history).content
    print(aireply)
    history.append(AIMessage(content=aireply))

