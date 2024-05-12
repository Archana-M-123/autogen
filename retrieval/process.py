from agents import TaskAwareGroupChat, llm_config
import autogen

def process_user_request(user_request):
    # Initialize the group chat with the user proxy agent
    group_chat = TaskAwareGroupChat(
        agents=[],
        messages=[{"message": user_request}],
        max_round=1,
    )

    # Initialize the group chat manager
    group_chat_manager = autogen.GroupChatManager(
        groupchat=group_chat,
        llm_config=llm_config
    )

    # Process user input through the group chat manager
    selected_agent = group_chat.choose_next_speaker([{"message": user_request}])

    # Retrieve data from the selected agent
    if selected_agent:
        retrieved_data = selected_agent.retrieve_data()
        return retrieved_data
    else:
        return "Invalid section requested."
