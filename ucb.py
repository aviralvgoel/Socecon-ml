# defining 5 arms using gaussian classes
import random
import math

class Arm:
    def __init__(self,average,standard_deviation):
        self.average = average
        self.sd=standard_deviation
        self.nt=0 #number of pulls of a particular arm
        self.rt = 0 # average till then


    def pull_arm(self):
        self.nt +=1
        self.deltat = math.sqrt(8*(math.log(N))/self.nt)
        self.pull = random.gauss(self.average,self.sd)
        self.rt= (self.pull)/self.nt
        return self.pull

    # def ucb(self):
    #     self.ucb = self.rt+self.deltat
    #     return self.ucb


arm1 = Arm(0.2,0.000001)
arm2 = Arm(0.3,0.000001)
arm3 = Arm(0.6,0.000001)
N=3 # total number of pulls of all arms
pull1 = arm1.pull_arm()
pull2 = arm2.pull_arm()
pull3 = arm3.pull_arm()
T= 1000
i=0
arm1.ucb = arm1.deltat+ arm1.rt
arm2.ucb = arm1.deltat + arm2.rt
arm3.ucb = arm3.deltat + arm3.rt
while (i<T):
    if max(arm1.ucb,arm2.ucb,arm3.ucb)==arm1.ucb:
        N+=1
        arm1.pull_arm()
        arm1.ucb = arm1.deltat + arm1.rt
        arm2.ucb = arm1.deltat + arm2.rt
        arm3.ucb = arm3.deltat + arm3.rt
        print(f"we played arm 1 and arm1ucb= {arm1.ucb} arm2ucb = {arm2.ucb} arm3ucb = {arm3.ucb}")
        i+=1

    if max(arm1.ucb,arm2.ucb,arm3.ucb)==arm2.ucb:
        N+=1
        arm2.pull_arm()
        arm2.ucb = arm2.deltat + arm2.rt
        arm2.ucb = arm1.deltat + arm2.rt
        arm3.ucb = arm3.deltat + arm3.rt
        print(f"we played arm 2 and arm1ucb= {arm1.ucb} arm2ucb = {arm2.ucb} arm3ucb = {arm3.ucb}")
        i+=1

    if max(arm1.ucb,arm2.ucb,arm3.ucb)==arm3.ucb:
        N+=1
        arm3.pull_arm()
        arm3.ucb = arm3.deltat + arm3.rt
        arm2.ucb = arm1.deltat + arm2.rt
        arm3.ucb = arm3.deltat + arm3.rt
        print(f"we played arm 3 and arm1ucb= {arm1.ucb} arm2ucb = {arm2.ucb} arm3ucb = {arm3.ucb}")
        i+=1




