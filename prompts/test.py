from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage


# # PART 1: Create a ChatPromptTemplate using a template string
# template="Tell me a joke {topic}."
# prompt_template=ChatPromptTemplate.from_template(template)

# print("#############--PromptTempleate---##############")
# prompt=prompt_template.invoke({"topic":"cats"})
# print(prompt)

# # PART 2: Prompt with Multiple Placeholders
# template_multiple=""" You are helpful assitant.
# Human:Tell me a {number} joke on {joke} .
# Assitant: """
# prompt_multiple=ChatPromptTemplate.from_template(template_multiple)

# prompt=prompt_multiple.invoke({"number":"3","joke":"bear"})
# print("\n----- Prompt with Multiple Placeholders -----\n")
# print(prompt)
# print(prompt.to_string()) # for only content

# PART 3: Prompt with System and Human Messages (Using Tuples)
# message=[
#     ("system","You are a combedian who tell jokes about {topic}."),
#     ("human","tell me {count} jokes."),
# ]

# prompt_template=ChatPromptTemplate.from_messages(message)
# prompt=prompt_template.invoke({"topic":"Robot","count":"3"})
# print(prompt.to_string())

# # Extra Informoation about Part 3.
# # This does work:
# messages = [
#     ("system", "You are a comedian who tells jokes about {topic}."),
#     HumanMessage(content="Tell me 3 jokes."),
# ]
# prompt_template = ChatPromptTemplate.from_messages(messages)
# prompt = prompt_template.invoke({"topic": "lawyers"})
# print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
# print(prompt)


# This does NOT work:
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    HumanMessage(content="Tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
print(prompt)