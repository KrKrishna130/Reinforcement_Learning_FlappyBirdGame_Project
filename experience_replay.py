from collections import deque
import random
# import kr lenge collection se deque ko bad me used aayega
class ReplayMemory():
    
    #=========== create FIFO queue - experience replay===========#
    def __init__(self, maxlen, seed=None):
        # yaha hm max length,seed value isko by defalut none rakhte hai
        # jb bhi experience store kr lenge tab random value bahar nikalege wahi hm 
        # random value k liye initial value dena chahhte hai to seed value dete hai
        self.memory = deque([], maxlen=maxlen)  # memory empty add krneg inital ,maxm memory ka size kya rakhna chahte hai
# 3 method hona chahiye 1.add,2.random selection,3.lenght -->inke liye method chaiye
    def append(self, new_exp):
        self.memory.append(new_exp)

    def sample(self, sample_size):
        return random.sample(self.memory, sample_size)

    # curr buffer size
    def __len__(self):
        return len(self.memory)
