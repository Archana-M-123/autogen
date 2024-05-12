import autogen

# Define configuration settings for the language model
config_list=[
    {
        'base_url': "http://localhost:1234/v1",
        'api_key' : "sk-111111111111111",
        "model": "TheBloke/zephyr-7B-beta-GGUF",

    }
]

# Configuration settings for the language model
llm_config ={
    "config_list": config_list,
}

# Define the agents using appropriate subclasses
adder_agent = autogen.UserProxyAgent(name="adder_agent")
multiplier_agent = autogen.UserProxyAgent(name="multiplier_agent")
subtracter_agent = autogen.UserProxyAgent(name="subtracter_agent")
divider_agent = autogen.UserProxyAgent(name="divider_agent")
number_agent = autogen.UserProxyAgent(name="number_agent")

# Set descriptions for the agents
adder_agent.description = "Add 1 to each input number."
multiplier_agent.description = "Multiply each input number by 2."
subtracter_agent.description = "Subtract 1 from each input number."
divider_agent.description = "Divide each input number by 2."
number_agent.description = "Return the numbers given."

# Define a group chat with the agents
group_chat = autogen.GroupChat(
    agents=[adder_agent, multiplier_agent, subtracter_agent, divider_agent, number_agent],
    messages=[],
    max_round=2,
)

# Initialize the group chat manager
group_chat_manager = autogen.GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config
)

# Initiate a chat with one of the agents
chat_result = number_agent.initiate_chat(
    group_chat_manager,
    message="My number is 3, I want to turn it into 13.",
    summary_method="reflection_with_llm",
)

# Print the chat result summary
print("hahahhah",chat_result.summary)
