import os
from mistralai import Mistral
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_mistralai.chat_models import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model=ChatMistralAI(model="mistral-large-latest")
chat_history=[]
# res=model.invoke("What is the capital of USA?")

# print(res.content)
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)
# message=[
#     SystemMessage(content="Solve the following math problem?"),
#     HumanMessage(content="What is the square of 8?"),
#     AIMessage(content="The square of a number means multiplying the number by itself.So, the square of 8 is:8 × 8 = 64"),
#     HumanMessage(content="The square of 24 is?")
# ]

# res=model.invoke(message)

# # print(res)

# print(f"The Ai response is :{res.content}")
# storing the chat history
while True:
    query=input("You:")
    if query.lower()=="exit":
        break
    chat_history.append(HumanMessage(content=query))
    res=model.invoke(chat_history)
    chat_history.append(AIMessage(res.content))
    respone=res.content

    print(f"AI:{respone}")
print("---- Message History ----")
print(chat_history)
