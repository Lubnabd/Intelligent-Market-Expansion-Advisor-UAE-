# Intelligent-Market-Expansion-Advisor-UAE-

This project is an Agentic AI advisory system built for a Jordanian restaurant planning to expand into Dubai and Abu Dhabi.

The system helps management ask questions about locations, competitors, menu strategy, pricing, marketing, operations, delivery, and licensing.

It is built in Python using Agno as the agent framework and OpenAI as the LLM.

The agent can decide when current external information is needed and use `WebSearchTools` to research it.

A CLI chatbot is used for fast interaction and testing.

The final responses are structured as clear, actionable, and executive-friendly recommendations.

# Documentation

## Architecture overview

Executive question
        ↓
Agno Agent receives the question, instructions, and available tools
        ↓
OpenAI LLM understands the question
        ↓
Does this require current or external information?
        ↓
if external then it will use (WebSearchTool) and if not it will use built-in knowledge
        ↓
Search tool
        ↓
Relevant evidence
        ↓
Search results are returned to OpenAI
        ↓
OpenAI analyzes evidence
        ↓
Recommendation

### Model

The used model is OpenAI gpt-5-mini. The system uses LLM-requested tool calling. The LLM decides when web search is needed, Agno executes the requested tool, and the result is returned to the LLM.

### Agent

The agent is an advisory agentic AI system using Python + Agno, that uses web search to supplement the model's built-in knowledge with current external information when necessary.

Control logic: Python control flow manages the CLI interaction, while Agno configuration and agent instructions control conversation history, tool availability, response structure, and agent behavior.

Agent harness: Rather than implementing the entire LLM execution and tool-calling layer manually, Agno acts as the agent framework/harness. It manages communication with the model, exposes tools, executes requested tool calls, maintains configured conversation state, and returns the final response.

## How to run the project locally

### 1. clone the repository

git clone <repo-ssh-url>
cd Intelligent-Market-Expansion-Advisor-UAE

### 2. Create a virtual environment and activate it

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

### 3. Create .env file and add your free API Key(private and should not be seen by anyone)

OPENAI_API_KEY=your_openai_api_key

### 5. Run the agent

python app.py

### 6. Start your question after the 'You:'

Questions like: Which areas in Dubai are most suitable for our expantion?

### 7. to exit the activated environment after you get the response:

exit

## Key design decisions

### Structured Output Schema

To keep recommendations consistent and executive-friendly, Schema structure:
- recommendation
- reasoning
- advantages
- disadvantages

### CLI interface

A command-line chatbot was used as the main interface because the assignment allows CLI interaction and it enabled faster development, testing, and debugging without the additional complexity.

### Web search ( WebSearchTools Tool Calling)

Because an LLM's built-in knowledge may not contain the latest market or regulatory information, the agent can use web search for time sensitive questions such as competitors, licensing, and pricing.

WebSearchTools was added because some expansion questions depend on current information that may not exist in the model's built-in knowledge.

The `ddgs` package was installed because it is used by Agno's web-search functionality.

### Hallucination risk

Hallucination: The system reduces hallucination risk by instructing the model to use current evidence when needed, prioritize reliable and authoritative sources, prefer official UAE sources for regulatory information, avoid inventing prices or statistics, explicitly state assumptions and uncertainty, and indicate when reliable evidence is unavailable.

Important business, legal and regulatory information should be verified with official sources.

## API Usage and Cost Control

To reduce unnecessary token usage and latency, the system:
- instructs the model to keep responses concise and answer only the user's specific question
- limits web-search results with fixed_max_results= 5
- limits conversation history with num_history_runs= 3
- uses web search only when current or external information is needed
- uses a single-agent architecture instead of unnecessary multi-agent calls
- The instructions discourage unnecessary repeated information

Shorter answers help reduce output tokens, while limiting search results and conversation history helps reduce input tokens. That's a useful distinction to mention if they ask you about cost control during the demo.

## Limitations

### No private business data

The advisor currently uses only the restaurant context included in the instructions.

It does not have access to actual:
- sales data
- financial data
- customer analytics
- supplier information

### Limited market data

The system does not currently connect to professional commercial datasets for exact rents, foot traffic or restaurant sales

# Evaluation/Testing Artifacts

### Questions:

1. "What does our restaurant specialize in?"
2. "Who are the current pizza and kebab competitors in Dubai?"
3. "What government requirements should we investigate before opening a restaurant in Dubai?"
4. "What are current restaurant trends relevant to our concept?"
5. "Which areas in Dubai fit our restaurant?"
6. "How should we adapt our menu for UAE customers?"
7. "What pricing bands should we consider in Dubai?"
8. "What staffing issues should we plan for?"
9. "What delivery strategy should we use in Dubai?"
10. "Give management a complete Abu Dhabi expansion plan"

### What worked well

The agent performed well when:
- answering questions within the restaurant expansion scope
- distinguishing between questions that required web search and questions that could be answered without it
- using `WebSearchTools` for current information such as competitors and licensing requirements
- producing structured recommendations with reasoning, advantages, and disadvantages
- following the instructions to keep answers focused on the user's specific question

### What failed or was uncertain

Some limitations were observed during testing:
- Web search occasionally returned `No results found`, especially for very specific government searches.
- When web search failed, the model could still generate a detailed answer from its built-in knowledge, which means some claims may require manual verification.
- Some responses were initially too long because the agent tried to include too many details.
- The same question may produce slightly different answers because LLM generation and web-search results are not fully deterministic.

### How I Would Improve the System

- Improve prompt instructions for more concise and focused answers.
- Add fallback search tools or more reliable data sources if the primary web search fails.
- Use direct official UAE government sources for licensing and regulatory information.
- Keep answers concise to reduce output tokens.
- Limit web-search results with `fixed_max_results`.
- Only call web search when current information is actually needed.

# AI Tool Usage Disclosure

ChatGPT was used as a development assistant throughout this project. It was mainly used for understanding concepts, reviewing design decisions, improving prompts and documentation, and helping troubleshoot issues. AI suggestions were reviewed, tested, and adapted before being included in the final project.

ChatGPT assisted with the following areas:

- **Planning the system architecture:** Helped simplify the project into a single-agent architecture using Python, Agno, OpenAI, WebSearchTools, SQLite conversation history, a structured output schema, and a CLI chatbot.

- **Writing and refining agent instructions:** Helped structure the instructions so that the agent covered the complete advisory scope required by the assessment.

- **Improving prompt quality:** Helped make the instructions more focused, executive-friendly, concise, actionable, and better aligned with the user's specific question instead of producing a complete expansion report for every request.

- **Hallucination mitigation:** Helped identify hallucination risks and add instructions that tell the model not to invent prices, statistics, regulations, competitors, or other factual information, to state assumptions and uncertainty, and to use web search when current external information is required.

- **Structured responses:** Helped introduce and refine the Pydantic `Recommendation` output schema containing recommendation, reasoning, advantages, disadvantages, risks, and next actions.

- **Testing and evaluation:** Helped design evaluation questions that test different advisory areas, including questions that should be answered using the model's existing knowledge and questions that should trigger web research.

- **Limitations and future improvements:** Helped identify realistic limitations such as unreliable web-search results, remaining hallucination risk, lack of private restaurant data, lack of professional market datasets, and the current CLI-only interface. It also helped identify possible future improvements such as stronger source verification, additional data sources, RAG for private documents, observability, and an optional graphical UI.

- **Documentation:** Helped improve the wording and organization of README sections, including architecture, local setup, design decisions, API cost control, hallucination mitigation, limitations, future improvements, evaluation, and AI tool usage disclosure.

The final implementation choices, code changes, testing, and documentation were reviewed and understood before being included in the project.

### Personally Implemented and Fully Understood

- Agno agent configuration
- OpenAI model integration
- Web search tool integration
- Agent instructions / prompt design
- Pydantic structured output/Schema
- CLI chatbot
- Cost-control and hallucination-mitigation rules
- Evaluation and testing
- Documentation decisions

AI was used as development assistance, but all final decisions and code were reviewed and understood.