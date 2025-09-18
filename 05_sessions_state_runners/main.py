from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from uuid import uuid4
from google.genai.types import Content, Part
from qa_agent.agent import root_agent as qa_agent
from dotenv import load_dotenv
import asyncio

load_dotenv()

APP_NAME = "05_sessions_state_runners"
USER_ID = "user_123"
SESSION_ID = str(uuid4())

session_service = InMemorySessionService()

initial_state = {
    "user_name": "Muhamamd Saad",
    "user_preferences": """
        - I love working with AI and Agents.
        - My favorite sports is Cricket.
        - I am a CS undergrad student.
        - I love to travel and explore new places.
        - My favorite TV show is Game of Thrones.
        - My favorite anime movie is Your Name.
    """
}


async def main():
    print("Creating a stateful session")
    print(f"Session ID: {SESSION_ID}")

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state
    )

    runner = Runner(
        agent=qa_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    while (True):
        print("\nWaiting for user input...")

        input_text = input("Enter your question (or 'exit' to quit): ")

        if input_text.lower() == 'exit':
            print("Exiting...")
            break

        new_message = Content(
            parts=[Part(text=input_text)],
            role="user"
        )

        for event in runner.run(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=new_message
        ):
            if event.is_final_response() and event.content and event.content.parts:
                print("AI:", event.content.parts[0].text)

    print("\nUpdating session state with new information.")

    session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    # Log final Session state
    print("=== Final Session State ===")
    for event in session.events:
        print(f"{event.timestamp}: {event.content.parts[0].text}")

asyncio.run(main())
