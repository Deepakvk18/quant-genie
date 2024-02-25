# LLM
from langchain.chat_models import ChatOpenAI
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor
from langchain.schema.runnable import RunnablePassthrough
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.tools.render import format_tool_to_openai_function
from langchain.output_parsers import PydanticOutputParser
from pydantic.v1 import Field, BaseModel
from typing import List

from llm.tools.technical_analysis import technical_tools
from llm.tools.fundamental_analysis import fundamental_tools
from llm.prompts import SYSTEM_TEMPLATE



tools = []
tools.extend(technical_tools)
tools.extend(fundamental_tools)

functions = [format_tool_to_openai_function(tool) for tool in tools]

class OutputSchema(BaseModel):
    text: str = Field(description='output in text'),
    images: List[str] = Field(description='List of image urls', type=List[str])

gpt = ChatOpenAI(
    model='gpt-3.5-turbo-16k',
    streaming=True,
    temperature=0,
    ).bind(functions=functions)

gemini = ChatGoogleGenerativeAI(
            model='gemini-pro', 
            temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_TEMPLATE),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
],)

chain = RunnablePassthrough.assign(
    agent_scratchpad = lambda x: format_to_openai_functions(x["intermediate_steps"])
) | prompt | gpt | OpenAIFunctionsAgentOutputParser()

agent_executor = AgentExecutor(
                    agent=chain, 
                    tools=tools, 
                    verbose=True, 
                    max_iterations=5,
                    return_intermediate_steps=False,
                    handle_parsing_errors=True)