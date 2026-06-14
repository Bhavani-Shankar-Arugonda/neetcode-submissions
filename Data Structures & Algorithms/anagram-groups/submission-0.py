class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1 = [0]*len(strs)
        list2 = []
        for i in range (len(strs)):
            if(list1[i]!=-1):
                list1[i]=-1
                new_list = []
                new_list.append(strs[i])
                for j in range(i+1,len(strs)):
                    if(list1[j]!=-1):
                        if(sorted(strs[i])==sorted(strs[j])):
                            list1[j]=-1
                            new_list.append(strs[j])
                list2.append(new_list)
        
        return list2




