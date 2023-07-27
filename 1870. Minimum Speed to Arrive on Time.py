import math

class Solution(object):
    def minSpeedOnTime(self, dist, hour):

        if (len(dist) - 1 >= hour):
            print("not possible")
            return -1

        maxSpeed = 10000000

        minSpeed = 1
        while(minSpeed <= maxSpeed):
            midSpeed = int((minSpeed + maxSpeed) / 2)

            totalTime = float(0)
            for x, distance in enumerate(dist):
                #print(x)
                time = 1 /float(1)
                time = float(distance) / float(midSpeed)
                if (x+1 != len(dist)):
                    time = math.ceil(time)
                totalTime = totalTime + time
            print("time: " + str(totalTime) + " for speed: " + str(midSpeed))
            if (totalTime == hour):
                print("Solution: " + str(midSpeed))
                return midSpeed
            if (totalTime > hour):
                minSpeed = midSpeed +1 
            if (minSpeed == midSpeed or maxSpeed == midSpeed):
                var= [minSpeed, midSpeed, maxSpeed]
                print("pointer gleich " +  str(var))
                print("Solution: " + str(midSpeed))
                return minSpeed
            if (totalTime < hour):
                maxSpeed = midSpeed
        return maxSpeed


