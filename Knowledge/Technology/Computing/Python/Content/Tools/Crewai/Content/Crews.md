## Concepts

A crew in crewAI represents a collaborative group of agents working together to achieve a set of tasks. Each crew defines the strategy for task execution, agent collaboration, and the overall workflow.

## Usage

### Creating a Crew

```bash
from crewai import Crew, Agent, Task, Process
from langchain_communicty.tools import DuckDuckGoSearchRun
from crewai_tools import tool

@tool('DuckDuckGoSearch')
def search(search_query: str):
	"""Search the web for information on a given topic"""
	return DuckDuckGoSearchRun().run(search_query)
# Define
```

#technology #computing #python #crewai 