from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatMistralAI(model="mistral-large-latest")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert product reviewer."),
        ("human", "List the main features of the product {product_name}."),
    ]
)

pros_prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            (
                "human",
                "Given these features: {features}, list the pros of these features.",
            ),
        ]
    )

cons_prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            (
                "human",
                "Given these features: {features}, list the cons of these features.",
            ),
        ]
    )

def combine_pros_cons(pros, cons):
    return f"Pros:\n{pros}\n\nCons:\n{cons}"

# Now use RunnableLambda to pass features to the prompt, then to model
pros_branch_chain = (
    RunnableLambda(lambda features: {"features": features}) |
    pros_prompt_template |
    model | 
    StrOutputParser()
)

cons_branch_chain = (
    RunnableLambda(lambda features: {"features": features}) |
    cons_prompt_template |
    model |
    StrOutputParser()
)

chain = (
    prompt_template | 
    model | 
    StrOutputParser() |
    RunnableParallel(branches={"pros": pros_branch_chain, "cons": cons_branch_chain}) |
    RunnableLambda(lambda x: combine_pros_cons(x["branches"]["pros"], x["branches"]["cons"]))
)

res = chain.invoke({"product_name": "Redmi_Note_12"})

print(res)
