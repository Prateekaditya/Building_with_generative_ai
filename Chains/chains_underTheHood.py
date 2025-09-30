from langchain_core.runnables import RunnableSequence,RunnableLambda
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai.chat_models import ChatMistralAI

load_dotenv()


model=ChatMistralAI(model="mistral-large-latest")

message=[
    ("system","You are a college student you to tell joke on {topic}"),
    ("human","Tell me {count} jokes.")
]
prompt_template=ChatPromptTemplate.from_messages(message)

format_promt=RunnableLambda(lambda x:prompt_template.format_prompt(**x))
invoke_model=RunnableLambda(lambda x:model.invoke(x.to_messages()))
output_parser=RunnableLambda(lambda x:x.content)

chain=RunnableSequence(first=format_promt ,middle=[invoke_model],last=output_parser)

res=chain.invoke({"topic":"Lab","count":3})

print(res)
