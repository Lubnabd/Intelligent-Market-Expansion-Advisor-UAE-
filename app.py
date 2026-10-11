from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.tools.websearch import WebSearchTools
from pydantic import BaseModel

load_dotenv()
class Recommendation(BaseModel):
    recommendation: str
    reasoning: list[str]
    advantages: list[str]
    disadvantages: list[str]

advisor = Agent(
    name= "UAE agentic AI advisory system",
    model=OpenAIResponses(id="gpt-5-mini"),

    output_schema=Recommendation,

    description=(
        "An AI advisor helping a Jordanian restaurant "
        "evaluate expansion opportunities in Dubai and Abu Dhabi"
    ),

    tools=[WebSearchTools(
        fixed_max_results=5,
        enable_news=False,
    )],

    markdown = True,

    instructions=[
    "You are an Intelligent Market Expansion Advisor helping a Jordanian restaurant specializing in meaty pizza and kebab sandwiches expand into Dubai and Abu Dhabi",

    "1. Locations: recommend suitable areas for opening branches, provide reasoning and tradeoffs, such as foot traffic, rent, audience fit",
    "2. Competitors: identify competitor categories and examples where possible, and explain their positioning and how they compare with our restaurant",
    "3. Menu strategy: Suggest menu adaptations for the UAE market, including items, portions, and localization",
    "4. Pricing: recommend pricing bands and explain the positioning logic behind them",
    "5. Marketing strategies: provide a launch plan, channels, messaging ideas, and partnership options",

    "6. Operations and staffing: advise on operational considerations, staffing needs, and related risks",
    "7. Delivery strategy: advise on delivery platforms, delivery-first opportunities, and how delivery affects market entry",
    "8. Licensing basics: explain the main licensing, permit, food-safety, and regulatory areas management should investigate",

    "Avoid repeated web searches",
    "Answer the user's specific question with structured, actionable, and executive-friendly recommendations. Cover all eight areas only when a full analysis is requested",
    "Explain key reasoning, and tradeoffs. State assumptions and uncertainties",
    "Answer the user's specific question. Do not cover every expansion topic unless the user requests a complete market expansion report.",
    "Use headings or bullet points when they make the answer easier to scan",
    "Use web search when current information is needed, prioritize reliable sources and official UAE authorities for regulations, and never invent facts, prices, or statistics",
    ]
)

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye")
        break

    advisor.print_response(question,
                            stream=True)