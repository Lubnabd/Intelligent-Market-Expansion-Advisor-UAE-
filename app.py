from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIResponses

load_dotenv()

advisor = Agent(
    model=OpenAIResponses(id="gpt-5-mini"),
    instructions=[
        "You are a UAE restaurant expansion advisor",
        "The resturant is a Jordanian local resturant expanding into the UAE",
        "The target market are Abu Dhabi and Dubai",
        "The restaurant specializes in meaty pizza and kebab sandwiches", ],
    )

advisor.print_response(
    "Should we choose Dubai or Abu Dhabi?"
)