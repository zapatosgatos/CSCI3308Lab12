import parts


# The Computer class is a Facade class which will simplify the computer part classes.
# You should implement this class
# This class should be able to be called by the running part
class Computer:
    def __init__(self):
        self.cpu=parts.CPU()
        self.mem=parts.Memory()
        self.hd=parts.HardDisk()
    # implement the class below this line    








# The running part
# Don't modify the following code!
com=Computer()
com.startComputer()
com.printCPUInfo()
com.printMemInfo()
com.printHDInfo()
