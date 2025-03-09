from crewai.flow import Flow, start, listen
import time


class SimpleFlow(Flow):
    
    @start()
    def fuction_1(self):
        print("This step 1,")
        time.sleep(4)

    @listen(fuction_1)
    def function_2(self):
        print("This step 2,")
        time.sleep(4)

    @listen(function_2)
    def function_3(self):
        print("This step 3,")
        time.sleep(4)



# def kickoff():
#     print("This is a test")
#     return "Test completed"

def kickoff():
    obj = SimpleFlow()
    obj.kickoff()