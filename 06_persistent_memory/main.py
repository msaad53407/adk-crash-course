import asyncio
from google.adk.sessions import DatabaseSessionService
from google.adk.runners import Runner
from dotenv import load_dotenv
from utils import call_agent_async
from reminder_agent.agent import root_agent as reminder_agent

load_dotenv()

DB_URL = "postgresql://postgres:postgres123@localhost:5432/reminders-agent"

# Step 1: Initialize the session service
session_service = DatabaseSessionService(
    db_url=DB_URL
)

# Step 2: Define Initial state

initial_state = {
    "user_name": "Muhammad Saad",
    "reminders": []
}

APP_NAME = "reminder_agent"
USER_ID = "user_123"


async def main():

    # Step 3: Create or retrieve a session
    sessions = await session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID
    )

    if sessions and len(sessions.sessions) > 0:
        SESSION_ID = sessions.sessions[0].id
        print(f"Resuming existing session with ID: {SESSION_ID}")
    else:
        new_session = await session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state
        )
        SESSION_ID = new_session.id
        print(f"Created new session with ID: {SESSION_ID}")

    # Step 4: Setup Runner
    runner = Runner(
        agent=reminder_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    # ===== PART 5: Interactive Conversation Loop =====
    print("\nWelcome to Memory Agent Chat!")
    print("Your reminders will be remembered across conversations.")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        # Get user input
        user_input = input("You: ")

        # Check if user wants to exit
        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Your data has been saved to the database.")
            break

        # Process the user query through the agent
        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)

if __name__ == "__main__":
    asyncio.run(main())
