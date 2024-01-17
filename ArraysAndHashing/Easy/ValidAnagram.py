class Solution(object):
    def isAnagram(self, s, t):
        if len(s) == len(t):
            countS = dict()
            countT = dict()

            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)

            for letter in countS: # Hey I did not know this but you can just get the keys like this
                try:
                    if countS[letter] != countT[letter]: 
                        return False
                except:
                    return False
            
            return True

        else:
            return False