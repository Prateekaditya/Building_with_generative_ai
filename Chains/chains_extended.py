from dotenv import load_dotenv
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatMistralAI(model="mistral-large-latest")

message=[
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]
prompt_template=ChatPromptTemplate.from_messages(message)

upper_cases=RunnableLambda(lambda x:x.upper())
count_words=RunnableLambda(lambda x:f"Word count:{len(x.split())}\n{x}")
justSomething=RunnableLambda(lambda x:f"just checking how it formats\n\n{x}")

chain=prompt_template | model |StrOutputParser() |upper_cases |count_words |justSomething

res=chain.invoke({
    "topic":"school",
    "joke_count":3
})

print(res.encode("ascii", "ignore").decode())