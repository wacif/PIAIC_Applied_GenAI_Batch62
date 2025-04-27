from crewai.flow.flow import Flow, listen, start

class TestFlow(Flow):
    @start()
    def first_method(self):
        return "Output from first_method"

    @listen(first_method)
    def second_method(self, first_output):
        return f"Second method received: {first_output}"


def main():
    flow = TestFlow()
    final_output = flow.kickoff()

    print("---- Final Output ----")
    print(final_output)