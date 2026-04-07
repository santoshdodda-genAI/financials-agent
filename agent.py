from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from config import MODEL

# Agent
financial_agent = Agent(
    model=MODEL,
    name="market_summarizer",
    description="Classifies and summarizes financial text.",
    instruction="""
    You are an expert financial analyst.

    1. Classify sentiment: Bullish, Bearish, Neutral.
    2. Provide exactly 2 sentences summary.

    Format:
    Sentiment: <value>
    Summary: <2 sentences>
    """
)

# Runner
runner = Runner(
    app_name="financial-insights",
    agent=financial_agent,
    session_service=InMemorySessionService()
)

async def run_analysis(text_input: str) -> str:
    result = ""

    # Create session properly
    session = await runner.session_service.create_session(
        app_name="financial-insights",
        user_id="api_user"
    )

    content = Content(
        role="user",
        parts=[Part(text=text_input)]
    )

    async for event in runner.run_async(
        user_id="api_user",
        session_id=session.id,
        new_message=content
    ):
        if hasattr(event, "is_final_response") and event.is_final_response():
            if event.content and event.content.parts:
                result = event.content.parts[0].text
                break

    return result