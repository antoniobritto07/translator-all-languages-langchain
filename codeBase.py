from dotenv import load_dotenv
import os
from langchain.schema import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# messages = [
#     SystemMessage(content="Traduza o texto a seguir para inglês"),
#     HumanMessage(content="Se inscreva no canal para aprender Python")
# ]

model = ChatOpenAI(model="gpt-4")
parser = StrOutputParser()


message_template = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para {idiom}"),
    ("user", "{text}")
])

chain = message_template | model | parser

# response = model.invoke(messages)
# realResponse = parser.invoke(response)
finalResult = chain.invoke({"idiom": "francês", "text": "Se inscreva no canal para aprender Python"})
print(finalResult)
