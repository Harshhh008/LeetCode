class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []
            
        temp = []
        sub_temp = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] == (nums[i - 1]+1):
                continue
            else:
                if nums[i - 1] != sub_temp[0]:
                    temp.append([sub_temp[0], nums[i - 1]])
                else:
                    temp.append([sub_temp[0]])
                sub_temp = [nums[i]]

        if nums[-1] != sub_temp[0]:   
            temp.append([sub_temp[0], nums[-1]])
        else:
            temp.append([sub_temp[0]])


        final_list = []
        for val in temp:
            if len(val) > 1: 
                final_list.append(f"{val[0]}->{val[len(val) - 1]}")
            else:
                final_list.append(str(val[0]))
        
        return final_list