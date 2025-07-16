"""
Conditional Chain Example - LangChain LCEL

This script demonstrates a conditional branching chain that:
1. First classifies user feedback as positive or negative using sentiment analysis
2. Then branches to different response logic based on the classification
3. Generates appropriate responses tailored to the sentiment

The chain showcases dynamic routing and conditional logic in LangChain workflows.
Uses Pydantic for structured output parsing and RunnableBranch for conditional execution.
"""

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser 
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-1.5-flash")

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive","negative"]=Field(description="Sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=Feedback)



prompt1=PromptTemplate(
    template="Classify the following text into positive or negative : \n{feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions":parser2.get_format_instructions()}
)



classifier_chain=prompt1 | model | parser2

prompt2=PromptTemplate(
    template="Write an appropriate response to the positive feadback\n{feedback}",
    input_variables=["feedback"]
)

prompt3=PromptTemplate(
    template="Write an appropriate response to the negative feadback\n{feedback}",
    input_variables=["feedback"]
)




branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2 | model |parser),
    (lambda x:x.sentiment=='negative',prompt3| model | parser),
    RunnableLambda(lambda x:"Could not found sentiment")
)

chain=classifier_chain | branch_chain

print(chain.invoke({'feedback':'This is a terrible phone'}))