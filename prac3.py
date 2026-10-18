class Two_sum:
    def __init__(self,num:list[int],target:int):
        self.nums = nums
        self.target = target

    def return_index(self):

        seen = {}

        for i,n in enumerate(self.nums):

            complement = self.target - n

            if complement in seen:
                return [seen[complement],i]

            seen[n] = i

        return []


tae = Two_sum([5,10,4,6], 16)

print(tae.returnIndex())

