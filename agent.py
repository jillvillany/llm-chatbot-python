from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import Tool
from langchain_core.prompts import PromptTemplate
from llm import openai_llm, watsonx_llm
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

# llm = openai_llm
llm = watsonx_llm


# NOTE: return_direct=False and handle_parsing_errors=True needed so don't get type validation error for memory
tools = [
    Tool.from_function(
        name="General Chat",
        description="For general chat not covered by other tools",
        func=llm.invoke,
        return_direct=False,
        handle_parsing_errors=True
    )
]

memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True,
)

# agent_prompt = hub.pull("hwchase17/react-chat")
# NOTE: created a custom prompt because the above prompt specifies that it's an OpenAI model
with open("agent_prompt.txt", "r") as f:
    agent_prompt_template = f.read()
agent_prompt = PromptTemplate.from_template(agent_prompt_template)

agent = create_react_agent(llm, tools, agent_prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    # tool_names=[tool.name for tool in tools],
    memory=memory,
    verbose=True,
    handle_parsing_errors=True
    )


def generate_response(prompt):
    """
    Create a handler that calls the Conversational agent
    and returns a response to be rendered in the UI
    """
    print(f"PROMPT: {prompt}")

    response = agent_executor.invoke({"input": prompt})
    print(response)

    return response['output']


if __name__ == "__main__":
    generate_response("who is the ceo of neo4j?")