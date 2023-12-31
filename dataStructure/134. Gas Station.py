from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        start_index = 0
        car_gas = gas[0]

        left = 0

        while left < len(gas):
            if car_gas < cost[left]:
                left += 1
                car_gas = gas[left]
            else:
                start_index = left
                cycle_index = left
                while car_gas >= cost[cycle_index]:
                    if cycle_index == len(gas) - 1:
                        car_gas-=cost[cycle_index]
                        cycle_index = 0
                        car_gas+=gas[cycle_index]
                    elif cycle_index==0:
                        car_gas-=cost[-1]+gas[cycle_index]
                    else:
                        car_gas = car_gas - cost[cycle_index]
                        car_gas+=gas[cycle_index+1]
                    cycle_index += 1
                    if cycle_index == start_index:
                        return True

                left+=1

        return -1

gas = [2,3,4]
cost = [3,4,3]
obj=Solution()
obj.canCompleteCircuit(gas,cost)






