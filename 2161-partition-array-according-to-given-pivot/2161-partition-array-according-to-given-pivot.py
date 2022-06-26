class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pos, l, cnt = 0, list(), 0
        for i in range(len(nums)):
            if nums[i]<pivot:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos+=1
            else:
                if nums[i] == pivot:
                    cnt+=1
                else:
                    l.append(nums[i])
        nums[pos:pos+cnt] = [pivot]*cnt
        pos+=cnt
        nums[pos::] = l
        return nums