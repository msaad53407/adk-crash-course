from google.adk.agents import Agent


agent_model = "gemini-2.0-flash"

agent_instructions = """
You are a helpful assistant that answers questions based on the user's preferences and information.
If the information is not available, respond with "I don't know" and do not make up answers.
Your tone should be friendly and responses should be concise.

Some information about user:
- Name: {user_name}
- Preferences: {user_preferences}
"""

root_agent = Agent(
    name="qa_agent",
    model=agent_model,
    description="An agent that answers questions based on user preferences and information.",
    instruction=agent_instructions,
)
