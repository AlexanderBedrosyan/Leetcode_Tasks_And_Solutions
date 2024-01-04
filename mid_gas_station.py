# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith
# station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
#
# Given two integer arrays gas and cost, return the starting gas station('s index if you can travel around the circuit '
# 'once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique)

class Solution(object):
    def checker(self, gas, cost, index):
        result = 0
        for i in range(len(gas)):
            if i == 0:
                result = gas[index]
                index += 1
                continue
            if result - cost[index] < 0:
                return False
            else:
                result = result - cost[index] + gas[index]
            index += 1
            if index > len(gas) - 1:
                index = 0
        return True


    def canCompleteCircuit(self, gas, cost):
        ind = 0
        while True:
            if self.checker(gas, cost, ind):
                return ind
            ind += 1
            if ind > len(gas) - 1:
                return -1

solve = Solution()
print(solve.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))