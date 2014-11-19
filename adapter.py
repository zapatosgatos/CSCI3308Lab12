import facade

# The Adaptor class should be implemented so that it has two methods that can be called by the running code.
# As you can see, it should contain a start function to start the computer, and a getComputerInfo function to get the information of the CPU, memory and hard disk. 
# You can only use the Computer class from the facade.py you implemented. Do not use the classes in parts.py 
class Adapter:
    def __init__(self):
        pass

    def start(self):
        pass

    def getComputerInfo(self):
        pass


# The running part. You should not modify this part.
newcomputer=Adapter()
newcomputer.start()
newcomputer.getComputerInfo()
