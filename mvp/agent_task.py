from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, CSVSearchTool
from langchain_openai import ChatOpenAI
import os

# Get the full path to the CSV file
csv_file_path = os.path.abspath('crew/atlanta_neighborhoods_with_coordinates.csv')

# Define the tools
serper_tool = SerperDevTool()
website_search_tool = ScrapeWebsiteTool()
atlanta_ga_rent_csv = CSVSearchTool(csv=csv_file_path)

task_validator = (
    "As the Validator, your primary task is to determine if the user's question regarding rent prices can be answered based on the available data in the CSV.\n"
    "You should identify the key components of the question and decide if the data is available or if a search is necessary.\n"
    "Here's the question: {question}"
)

task_analyst = (
    "As the Data Analyst, your responsibility is to create or update the visualization of rent prices based on the provided data and the user's requirements.\n"
    "You should handle tasks such as adjusting rent prices for inflation and generating the appropriate visualizations.\n"
    "If the question involves projecting future prices, use the given inflation rate and update the data accordingly.\n"
    "Here's the question: {question}"
)

task_researcher = (
    "As the Research Agent, your responsibility is to search the internet for information if the user's question cannot be answered with the available data.\n"
    "Use available tools to gather relevant information and ensure it is specific to the user's query about rent prices.\n"
    "Here's the question: {question}"
)

def create_agent_workflow(question):
    validator_agent = Agent(
        role='Validator',
        goal='Determine if the user\'s question can be answered with available data.',
        backstory="""
Expert in assessing if a query can be answered based on available data or if further research is required.
""",
        tools=[atlanta_ga_rent_csv],
        verbose=True,
        cache=True,
        allow_delegation=True,
    )

    analyst_agent = Agent(
        role='Data Analyst',
        goal='Create and update visualizations based on the provided data and user requirements.',
        backstory="""
Specialist in generating and updating visualizations based on data, handling tasks such as adjusting for inflation and future projections.
""",
        tools=[atlanta_ga_rent_csv],
        verbose=True,
        cache=True,
        allow_delegation=True
    )

    researcher_agent = Agent(
        role='Researcher',
        goal="Conduct internet searches for additional information if needed.",
        backstory="""
Expert in finding additional information online when the available data is insufficient to answer the user's question.
""",
        tools=[atlanta_ga_rent_csv],
        verbose=True,
        cache=True,
        allow_delegation=True
    )

    validation_task = Task(
        description=task_validator.format(question=question),
        expected_output='A determination if the question can be answered with available data or needs external research.',
        agent=validator_agent,
    )

    analysis_task = Task(
        description=task_analyst.format(question=question),
        expected_output='Updated data and visualizations based on the user\'s requirements.',
        agent=analyst_agent,
        context=[validation_task]
    )

    research_task = Task(
        description=task_researcher.format(question=question),
        expected_output='Additional information gathered from the internet if needed.',
        agent=researcher_agent,
        context=[validation_task]
    )

    crew = Crew(
        agents=[validator_agent, analyst_agent, researcher_agent],
        process=Process.linear,
        manager_llm=ChatOpenAI(temperature=0, model="gpt-4"),
        memory=True,
        tasks=[validation_task, analysis_task, research_task]
    )

    result = crew.kickoff(inputs={"topic": question})
    return result

# Example usage
question = "What will the rent prices in Atlanta, GA be in 3 years with an average US inflation rate of 3%?"
result = create_agent_workflow(question)
print(result)
