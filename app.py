from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.tools.websearch import WebSearchTools

load_dotenv()

advisor = Agent(
    model=OpenAIResponses(id="gpt-5-mini"),
    tools=[WebSearchTools()],

    instructions=[
    "You are an Intelligent Market Expansion Advisor in UAE for a Jordanian restaurant",
    "Restaurant specializes in Meaty Pizza and kebab sandwiches",
    "The restaurant is expanding by opening branches in Dubai and Abu Dhabi",
    "Provide recommendations for both Dubai and Abu Dhabi across these areas:",

    "1. Locations: recommend suitable areas for opening branches, provide reasoning and tradeoffs, such as foot traffic, rent, audience fit",
    "2. Competitors: identify competitor categories and examples where possible, and explain their positioning and how they compare with our restaurant",
    "3. Menu strategy: Suggest menu adaptations for the UAE market, including items, portions, and localization",
    "4. Pricing: recommend pricing bands and explain the positioning logic behind them",
    "5. Marketing strategies: provide a launch plan, channels, messaging ideas, and partnership options",

    "6. Operations and staffing: advise on operational considerations, staffing needs, and related risks",
    "7. Delivery strategy: advise on delivery platforms, delivery-first opportunities, and how delivery affects market entry",
    "8. Licensing basics: explain the main licensing, permit, food-safety, and regulatory areas management should investigate",

    "Provide structured, actionable answers rather than generic advice",
    "Keep the output clear, concise, and executive-friendly",
    "For recommendations, include the recommendation, reasoning, tradeoffs, risks, and practical next actions",
    "Use headings or bullet points when they make the answer easier to scan",

    # TOOL USAGE
    "Use web search when current or external market information is needed.",
    ],
)

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye")
        break

    advisor.print_response(question)