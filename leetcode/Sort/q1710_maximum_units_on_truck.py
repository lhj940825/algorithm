'''
 * User: Hojun Lim
 * Date: 2021-01-07
'''

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key= lambda x:x[1], reverse=True)

        output = 0
        for (num_box, unit) in boxTypes:
            if num_box <= truckSize:
                output += num_box * unit
                truckSize -= num_box

            else:
                output += truckSize * unit
                break

        return output



