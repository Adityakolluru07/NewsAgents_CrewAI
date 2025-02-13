from crewai import Agent
from tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"))

## AGENTS ##
"""
Creating a senior researcher agent with memory and verbose mode
"""
news_researcher = Agent(
    role="Senior Researcher",
    goal = "Uncover ground breaking technologies in {topic}",
    verbose = True,
    memory=True,
    backstory=(
        "Driven by curiosity, you are at forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world"
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

## creating a write agent witn custom tools responsible in writing news blog

news_writer = Agent(
    role="Writer",
    goal = "Narrate compelling tech stories about {topic}",
    verbose = True,
    memory=True,
    backstory=(
        "With a flair for simplyfying complex topics, you craft"
        "engaging narratives that captivate and educate, dringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)