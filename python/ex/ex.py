from typing import List

class YourClassName:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = input(int())
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False
