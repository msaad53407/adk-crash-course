from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os
import random

model = LiteLlm(model="openrouter/deepseek/deepseek-chat-v3.1:free",
                api_key=os.getenv("OPEN_ROUTER_API_KEY"))


def get_dad_joke() -> dict:
    """
    Get a dad joke from a predefined list of jokes.

    Returns:
        A dad joke in dict format.
    """
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call cheese that isn't yours? Nacho cheese!"
    ]
    return {
        "dad_joke": random.choice(jokes)
    }


root_agent = Agent(
    name="dad_joke_agent",
    model=model,
    description="An agent that tells dad jokes",
    instruction="""
    You are a dad joke agent. Your task is to tell dad jokes in response to user queries. Keep the jokes light-hearted and fun!
    """,
    tools=[get_dad_joke],
)
