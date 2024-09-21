## Concept

Tasks are specific assignments completed  by agents. They provide all necessary details for execution, such as a description, the agent responsible, required tools, and more, facilitating a wide range of actions complexities.
## Characteristics

Tasks can have a `description`, `expected_output`, `agent` and a `context`
## Referencing Variables

It's possible to reference the agent for specific tasks from task.yaml file.

**eg.**:

**agent.yaml**

```yml
email_summarizer:
	role: >
		Email Summarizer
	goal: >
		Summarize emails into a concise and clear summary
	backstory: >
		You will create a 5 bullet point summary of the report
	llm: mixtal_llm
```

**task.yaml**

```yml
email_summarizer_task:
	description: >
		Summarize the email into a 5 bullet point summary
	expected_output: >
		A 5 bullet point summary of the email
	agent: email_summarizer
	context:
		- reporting_task
		- reserarch_task
```

## Usage

### Creating a Task

```python
from crewai import Task

task = Task(
	description='Find and summarize the latest and most relevant news on AI',
	agent=sales=agent,
	expected_output='A bullet list summary of the top 5 most important AI news
,)
```

#technology #computing #python #crewai 