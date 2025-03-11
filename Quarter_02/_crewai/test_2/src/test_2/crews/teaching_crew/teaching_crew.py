from crewai import Crew, Task, Agent
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class TeachingCrew:

    agent_config = "config/teaching_crew.yaml"
    task_config = "config/teaching_crew.yaml" 
    # 1. Agent
    @agent
    def principle(self) -> Agent:
        """
        The principle agent is a school teacher who is responsible for overseeing the crew's operations and ensuring that all tasks are aligned with the crew's objectives.
        It ensures that all tasks are aligned with the crew's objectives and that the crew is functioning effectively.
        """
        return Agent(
            role="principle",
            description="The principle agent is a school teacher who is responsible for overseeing the crew's operations and ensuring that all tasks are aligned with the crew's objectives.",
            backstory="""You are a school teacher who is responsible for overseeing the crew's operations and ensuring that all tasks are aligned with the crew's objectives. You have a deep understanding of the educational system and are committed to providing the best possible learning experience for your students. You are also responsible for managing the crew's budget and resources, and ensuring that all tasks are completed on time and within budget.""",
        )
    # 2. Task

    # 3. Crew   

    # 4. Run

