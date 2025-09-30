from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_mistralai.chat_models import ChatMistralAI

load_dotenv()
 
model=ChatMistralAI(model="mistral-large-latest")

message=[
    ("system","You are a helpful friend in my {place}"),
    ("human","what new skills should i learn for {role}.")
]

prompt_template=ChatPromptTemplate.from_messages(message)

chain=prompt_template | model | StrOutputParser()

result =chain.invoke({"place":"college","role":"SDE"})

print(result)