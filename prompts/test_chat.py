from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai.chat_models import ChatMistralAI
from mistralai import Mistral
load_dotenv()

model=ChatMistralAI(model="mistral-large-latest")

print("##--Prompt from template--##")
# template="Tell me a joke about {topic}"
# prompt_template=ChatPromptTemplate.from_template(template)

# prompt=prompt_template.invoke({"topic":"law"})

# res=model.invoke(prompt)

message=[
    ('system','You are a compic tell me joke on {topic}'),
    ('human','Tell me {count} joke.'),
]
prompt_template=ChatPromptTemplate.from_messages(message)
prompt=prompt_template.invoke({"topic":"school","count":"3"})
res=model.invoke(prompt)

print(res.content.encode("ascii", "ignore").decode()) # done this because of the emoji problem
