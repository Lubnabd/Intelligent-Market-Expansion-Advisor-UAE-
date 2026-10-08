from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.tools.websearch import WebSearchTools

load_dotenv()

def get_restaurant_profile():
    """
    Returns information about the Jordanian restaurant.
    """
    print(">>> RESTAURANT PROFILE TOOL WAS CALLED")

    with open("data/restaurant_profile.md", "r") as file:
        return file.read()

def log_tool_call(function_name, func, args):
    print(f"\n>>> TOOL CALLED: {function_name}")
    print(f">>> ARGS: {args}\n")
    return func(**args)

advisor = Agent(
    model=OpenAIResponses(id="gpt-5-mini"),
    tools=[get_restaurant_profile,
    WebSearchTools()],

    tool_hooks=[log_tool_call],

    instructions=[
        "You are a UAE restaurant expansion advisor",
        # "The resturant is a Jordanian local resturant expanding into the UAE",
        # "The target market are Abu Dhabi and Dubai",
        # "The restaurant specializes in meaty pizza and kebab sandwiches",
        # "Separate factual information from assumptions",
        # "Explain trade-offs instead of simply giving an answer",
        # "Never invent precise statistics, rental prices, "
        # "competitors, regulations, or fees",
        # "When information is uncertain, clearly say so",
        # "Finish recommendations with practical next actions",
        "Use the restaurant profile tool for information about our restaurant.",
        "Use web search when the question requires current or external information.",
        "Do not invent exact rents, regulations, prices, or statistics.",
        "Prefer reliable and official sources.",
        ],
    )

# advisor.print_response(
#     "Should we choose Dubai or Abu Dhabi?"
# )
advisor.print_response(
    # "According to our restaurant profile, what products do we specialize in?"
    "Who are the current pizza and kebab competitors in Dubai?"
)