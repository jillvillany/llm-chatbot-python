from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import Tool
from llm import openai_llm, watsonx_llm
from langchain.chains.conversation.memory import ConversationBufferWindowMemory


# NOTE: return_direct=False and handle_parsing_errors=True needed so don't get type validation error for memory
tools = [
    Tool.from_function(
        name="General Chat",
        description="For general chat not covered by other tools",
        func=watsonx_llm.invoke,
        return_direct=False, # (!)
        handle_parsing_errors=True # (!)
    )
]

memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True,
)

agent_prompt = hub.pull("hwchase17/react-chat")
agent = create_react_agent(watsonx_llm, tools, agent_prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True
    )


def generate_response(prompt):
    """
    Create a handler that calls the Conversational agent
    and returns a response to be rendered in the UI
    """
    print(f"PROMPT: {prompt}")

    response = agent_executor.invoke({"input": prompt})

    return response['output']