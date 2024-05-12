import autogen
import difflib

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

# Define the agents for different sections
class DataRetrievalAgent(autogen.UserProxyAgent):
    def __init__(self, name, data):
        super().__init__(name=name)
        self.data = data

    def retrieve_data(self):
        return self.data

# Define data for each section
introduction_data = "This is the introduction section."
literature_data = "This is the literature section."
methodology_data = "This is the methodology section."
results_data = "These are the results."

# Create agents for each section with their corresponding data
introduction_agent = DataRetrievalAgent(name="introduction_agent", data=introduction_data)
literature_agent = DataRetrievalAgent(name="literature_agent", data=literature_data)
methodology_agent = DataRetrievalAgent(name="methodology_agent", data=methodology_data)
results_agent = DataRetrievalAgent(name="results_agent", data=results_data)

# Define a dictionary mapping user requests to agents
request_to_agent = {
    "introduction": introduction_agent,
    "literature": literature_agent,
    "methodology": methodology_agent,
    "results": results_agent,
}

# Define the TaskAwareGroupChat class
class TaskAwareGroupChat(autogen.GroupChat):
    def choose_next_speaker(self, conversation_history):
        user_input = conversation_history[-1]["message"].lower()  # Convert input to lowercase

        # Analyze user input to determine the task
        matches = difflib.get_close_matches(user_input, request_to_agent.keys(), n=1, cutoff=0.5)  # Use difflib to find close matches
        if matches:
            return request_to_agent[matches[0]]  # Return the closest match
        else:
            # Handle cases where no matching agent is found
            return None

# Initialize the user proxy agent
user_proxy_agent = autogen.UserProxyAgent(name="user_proxy_agent")

# Initialize the group chat with the user proxy agent
group_chat = TaskAwareGroupChat(
    agents=[user_proxy_agent],
    messages=[],
    max_round=1, 
)

# Initialize the group chat manager
group_chat_manager = autogen.GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config
)

# User input to select which section they want 
user_request = input("Enter the section you want (introduction, literature, methodology, results): ")

# Process user input through the group chat manager
selected_agent = group_chat.choose_next_speaker([{"message": user_request}])

# Retrieve data from the selected agent
if selected_agent:
    retrieved_data = selected_agent.retrieve_data()
    print("Retrieved data for", user_request, ":", retrieved_data)
else:
    print("Invalid section requested.")
