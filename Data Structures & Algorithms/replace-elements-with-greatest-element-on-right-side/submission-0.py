class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        output = []
        number = 0


        
        while number < (len(arr) - 1):
            maxvalue = max(arr[number+1:])
            output.append(maxvalue)
            number += 1

        output.append(-1)

        return output


        