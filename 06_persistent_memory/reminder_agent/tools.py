from google.adk.tools import ToolContext


async def add_reminder(reminder: str, tool_context: ToolContext) -> dict[str, str]:
    """Add a reminder to the user's list of reminders.
    Args:
        reminder (str): The reminder text to add.
        tool_context (ToolContext): The tool context containing session information.

    Returns:
        dict[str, str]: A confirmation message.

    """
    print(f"--- Tool: add_reminder called with reminder: {reminder} ---")
    existing_reminders = tool_context.state.get("reminders", [])

    existing_reminders.append(reminder)

    tool_context.state["reminders"] = existing_reminders

    return {"action": "add_reminder", "reminder": reminder, "message": "Reminder added successfully."}


async def list_reminders(tool_context: ToolContext) -> dict[str, list[str] | str]:
    """List all reminders for the user.
    Args:
        tool_context (ToolContext): The tool context containing session information.

    Returns:
        dict[str, list[str]]: A list of all reminders.

    """
    print(f"--- Tool: list_reminders called ---")
    reminders = tool_context.state.get("reminders", [])
    if not reminders or len(reminders) == 0:
        return {"action": "list_reminders", "reminders": "No reminders found."}

    return {"action": "list_reminders", "reminders": reminders}


async def update_user_name(new_name: str, tool_context: ToolContext) -> dict[str, str]:
    """Update the user's name in the session state.
    Args:
        new_name (str): The new name for the user.
        tool_context (ToolContext): The tool context containing session information.

    Returns:
        dict[str, str]: A confirmation message.

    """
    print(f"--- Tool: update_user_name called with new_name: {new_name} ---")
    tool_context.state["user_name"] = new_name

    return {"action": "update_user_name", "new_name": new_name, "message": "User name updated successfully."}


async def delete_reminder(index: int, tool_context: ToolContext) -> dict[str, str]:
    """Delete a reminder from the user's list of reminders.
    Args:
        index (int): The index of the reminder to delete.
        tool_context (ToolContext): The tool context containing session information.

    Returns:
        dict[str, str]: A confirmation message.

    """
    print(f"--- Tool: delete_reminder called with index: {index} ---")
    reminders = tool_context.state.get("reminders", [])
    if index < 0 or index >= len(reminders):
        return {"action": "delete_reminder", "message": "Invalid reminder index."}

    deleted_reminder = reminders.pop(index)
    tool_context.state["reminders"] = reminders

    return {"action": "delete_reminder", "reminder": deleted_reminder, "message": "Reminder deleted successfully."}


async def update_reminder(index: int, new_text: str, tool_context: ToolContext) -> dict[str, str]:
    """Update a reminder in the user's list of reminders.
    Args:
        index (int): The index of the reminder to update.
        new_text (str): The new text for the reminder.
        tool_context (ToolContext): The tool context containing session information.

    Returns:
        dict[str, str]: A confirmation message.

    """
    print(
        f"--- Tool: update_reminder called with index: {index}, new_text: {new_text} ---")
    reminders = tool_context.state.get("reminders", [])
    if index < 0 or index >= len(reminders):
        return {"action": "update_reminder", "message": "Invalid reminder index."}

    reminders[index] = new_text
    tool_context.state["reminders"] = reminders

    return {"action": "update_reminder", "reminder": new_text, "message": "Reminder updated successfully."}


async def clear_reminders(tool_context: ToolContext) -> dict[str, str]:
    """Clear all reminders from the user's list of reminders.
    Args:
        tool_context (ToolContext): The tool context containing session information.

    Returns:
        dict[str, str]: A confirmation message.

    """
    print(f"--- Tool: clear_reminders called ---")
    tool_context.state["reminders"] = []

    return {"action": "clear_reminders", "message": "All reminders cleared successfully."}
