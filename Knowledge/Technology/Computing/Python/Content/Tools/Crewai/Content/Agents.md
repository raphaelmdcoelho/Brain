
## Concept

An agent is an `autonomous unit` programmed to:
* Perform tasks
* Make decisions
* Communicate with other agents

The agent can be associated like a member of a team, with specific skills and a particular job to do. Agents can have different `roles`.
## Characteristics

Agents can have a `role`, `goal` and `backstory`.

## Usage

### Creating a agent

```python
from creai import Agent

agent = Agent(
	role='Data Analyst',
	goal='Extract actionable insights'
	backstory="""You're a data analyst at a large company
	You're responsible for analyzing data and providing insights
	to the business."""
	llm=my+llm
	max_iter=15
)
```

#technology #computing #python #crewai