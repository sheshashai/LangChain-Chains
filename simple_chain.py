"""
Simple Chain Example - LangChain LCEL

This script demonstrates a basic sequential chain that takes a topic as input
and generates 5 interesting facts about it using OpenAI's language model.

The chain follows this flow: Prompt Template → Language Model → String Parser
"""

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt =PromptTemplate(
    template="Genereate 5 intresting facts about {topic}",
    input_variables=["topic"],
)

model = ChatOpenAI()

parser=StrOutputParser()

chain=prompt | model | parser

result=chain.invoke({"topic":"lang graph"})

print(result)

chain.get_graph().print_ascii()