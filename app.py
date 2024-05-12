import autogen

print(dir(autogen))

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

# Initialize the assistant agent
assistant = autogen.AssistantAgent(
    name="assistant",
    system_message="You are a code specializing in python",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction. otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task="""write a python method to output numbers 1 to 100
"""

# Initiate the chat between the user proxy agent and the assistant
user_proxy.initiate_chat(
    assistant,
    message=task
)
