import os
from crewai import Agent, LLM
from crewai_tools import FileWriterTool


# LLM configurations - Agent specific config
model = os.getenv("WRITER_AGENT_LLM")
if model is None:
    raise ValueError("Environment variable 'RESEARCH_AGENT_LLM' must be set to a valid model name.")

temperature_str = temperature_str = os.getenv("RESEARCH_AGENT_TEMPERATURE", "0.7")
temperature = float(temperature_str)


llm = LLM(
    model=model,
    temperature=temperature
)

content_writer_agent = Agent(
    role="Content Writer",
    goal="Create comprehensive, well-structured reports and summaries",
    backstory = (
                "You are a professional content writer with expertise in creating "
                "clear, engaging, and well-structured documents. You can transform complex "
                "information into accessible and compelling content."
            ),
    llm=llm,
    tools=[FileWriterTool()],
    verbose=True,
)