from google.adk.agents import Agent
from .sub_agents.stock_analyst.agent import stock_analyst
from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.news_analyst.agent import news_analyst
from google.adk.tools import AgentTool

from .tools.index import get_current_time

root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="A manager agent that oversees multiple specialized agents to handle complex tasks.",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - stock_analyst
    - funny_nerd

    You also have access to the following tools:
    - news_analyst
    - get_current_time
    """,
    sub_agents=[stock_analyst, funny_nerd],
    tools=[get_current_time, AgentTool(news_analyst)]
)
