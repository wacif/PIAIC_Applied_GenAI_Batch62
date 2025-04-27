from crewai.flow.flow import Flow, listen, start, or_, and_
from datetime import datetime


class StateExampleFlow(Flow):
    first_timestamp: str = None
    second_timestamp: str = None

    @start()
    def first_start_method(self):
        self.first_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Output from first_start_method at {self.first_timestamp}"
    
    @start()
    def second_start_method(self):
        self.second_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Output from second_start_method at {self.second_timestamp}"

    @listen(or_(first_start_method, second_start_method))
    def second_method(self):
        return f"Output with or_. First completed at {self.first_timestamp}, Second completed at {self.second_timestamp}"

    # @listen(and_(first_start_method, second_start_method))
    # def second_method(self):
    #     return f"Output with and_. First completed at {self.first_timestamp}, Second completed at {self.second_timestamp}"

def main():
    flow = StateExampleFlow()
    final_output = flow.kickoff()
    print(f"Final Output: {final_output}")
    print("Final State:")
    print(flow.state)
