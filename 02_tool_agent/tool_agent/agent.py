from google.adk.tools import google_search
from google.adk.agents import Agent
from datetime import datetime
import os

model = "gemini-2.0-flash"


def get_current_time() -> dict:
    """Get the current time in the format YYYY-MM-DD HH:MM:SS.

    Returns:
        The current time in dict format.
    """
    return {"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


def get_current_directory() -> dict:
    """Get the current directory where the Agent is running on the system.

    Returns:
        The current directory in dict format.
    """
    return {"current_directory": os.getcwd()}


root_agent = Agent(
    name="tool_agent",
    model=model,
    description="A tool agent that can use tools to answer questions",
    instruction="""
    You are a helpful assistant that serves users by using available tools.
    - You can use the get_current_time tool to get the current time.
    - You can use the get_current_directory tool to get the current directory.
    """,
    # tools=[google_search],
    tools=[get_current_time, get_current_directory],
)
