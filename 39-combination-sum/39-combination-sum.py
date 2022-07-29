class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
    
        def dfs( nums, path, res,ind):
            if sum(path)>target:
                return
            if sum(path)==target:
                res.append(path[::])
                return
            for i in range(ind,len(nums)):
                dfs(nums,path+[nums[i]],res,i)
            return res
        dfs(candidates, [], res,0)
        return res