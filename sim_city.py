import city
import matplotlib.pyplot as plt
import numpy as np

def runSimNoShow(PopSize,RunDuration,threshold):
    c = city.City(PopSize,threshold)
    segindex = []
    t = 0
    while t < RunDuration*PopSize:
        c.step()
        if t % PopSize == 0:
            segindex.append(c.measureSeg())
        t += 1
    return segindex

def multipleRuns(reps,PopSize,RunDuration,threshold):
    avg = np.zeros(RunDuration)
    for i in range(reps):
        print(i)
        segindex = runSimNoShow(PopSize,RunDuration,threshold)
        plt.plot(segindex,alpha=0.5)
        avg += segindex
    avg /= reps
    plt.plot(avg,'k')
    plt.title("Segregation index over time")
    plt.xlabel("Time")
    plt.ylabel("Segregation index")
    plt.show()
    return avg

def multipleRunsNoShow(reps,PopSize,RunDuration,threshold):
    avg = np.zeros(RunDuration)
    for i in range(reps):
        segindex = runSimNoShow(PopSize,RunDuration,threshold)
        avg += segindex
    avg /= reps
    return avg

def thresholds(reps,PopSize,RunDuration):
    t = 1
    final=[]
    while t <= 8:
        print(t)
        avg = multipleRunsNoShow(reps,PopSize,RunDuration,t/8.0)
        final.append(avg[-1])
        plt.plot(avg,label=str(t))
        t+=1
    plt.legend()
    plt.title("Segregation index over time")
    plt.xlabel("Time")
    plt.ylabel("Segregation index")
    plt.show()
    plt.plot(final,'o-')
    plt.title("Final Segregation Index")
    plt.xlabel("Threshold (number of kin neighbors)")
    plt.ylabel("Final segregation index")
    plt.show()

def runSimShow(PopSize,RunDuration,threshold):
    c = city.City(PopSize,threshold)
    c.show("Starting config")
    segindex = []
    t = 0
    while t < RunDuration*PopSize:
        c.step()
        if t % PopSize == 0:
            segindex.append(c.measureSeg())
        t += 1
    c.show("End config")
    plt.plot(segindex)
    plt.title("Segregation index over time")
    plt.xlabel("Time")
    plt.ylabel("Segregation index")
    #plt.set_aspect(1.0)
    plt.show()
    #return segindex

# Step 1
runSimShow(50,2000,1/2)

# Step 2
#multipleRuns(10,10,1000,1/2)

# Step 3
#thresholds(10,50,2000)
