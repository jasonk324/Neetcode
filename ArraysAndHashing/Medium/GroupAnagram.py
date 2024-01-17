class Solution:
    def groupAnagrams(self, strs):
        groupAnagramDict = {}
        groupAnagramSet = set()
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString not in groupAnagramSet:
                groupAnagramSet.add(sortedString)
                groupAnagramDict[sortedString] = []
            groupAnagramDict[sortedString].append(string)

        return list(groupAnagramDict.values())


# I guess this way is slower with checking the dictionary key values
    
class Solution:
    def groupAnagrams(self, strs):
        groupAnagramDict = dict()

        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString not in groupAnagramDict.keys():
                groupAnagramDict[sortedString] = [string]
            else:
                groupAnagramDict[sortedString].append(string)
        
        return list(groupAnagramDict.values())
