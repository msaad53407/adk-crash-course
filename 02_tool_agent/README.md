# Notes

- Only one built-in tool is supported per agent. It means that If I am using google_search tool, I cannot another built-in tool like built-in like vertex-ai-search tool.
- We cannot mix custom function tools with built-in tools.
- We can provide multiple custom function tools in same agent. (Need to look into it whether it is working or not)

```python
root_agent = Agent(
    name="tool_agent",
    model=model,
    description="A tool agent that can use tools to answer questions",
    instruction="""
    You are a helpful assistant that serves users by using available tools.
    - You can use the google_search tool to search the web.
    """,
    tools=[google_search, get_current_time] # <- This does not work,
    tools=[vertex_ai_search, google_search] # <- This does not work either
    tools=[vertex_ai_search] # <- This works
    tools=[google_search] # <- This works
    tools=[get_current_time, get_current_directory] # <- This works
)
```

- We always have to specify a doc string for custom function tool

```python
def get_current_time() -> dict:
    """Get the current time.

    Returns:
        The current time in dict format.
        Example: {"current_time": "2023-09-01 12:00:00"}
    """
```

- Always return data in dict format, this is because when agent parses the result, dict keys can give context to agent that what data is being returned. Like in above case, agent can know that current_time is the current time.
- Default parameters for custom function tool are not supported (need to look into it whether it is true for latest version or not).

```python
def get_current_time(timezone: str = "UTC") -> dict: # <-- Not possible
    """Get the current time.

    Returns:
        The current time in dict format.
        Example: {"current_time": "2023-09-01 12:00:00"}
    """
```
