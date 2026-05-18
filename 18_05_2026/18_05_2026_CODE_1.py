#LC 13. Roman to Integer

#CODE: 

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I' : 1, 'V' : 5,'X': 10, 'L': 50 , 'C' : 100, 'D' : 500, 'M' : 1000}
        ptr1 = 0
        ptr2  = 1
        res = 0
        if s in dic.keys():
            return dic[s]
        while ptr1 <= ptr2 and ptr2<len(s):
            if dic[s[ptr1]] >= dic[s[ptr2]]:
                res += dic[s[ptr1]]
                ptr1+=1
                ptr2+=1
                if ptr1==len(s)-1:
                    res += dic[s[ptr1]]
            elif dic[s[ptr1]] < dic[s[ptr2]]:
                res += abs(dic[s[ptr1]]-dic[s[ptr2]])
                ptr1+=2
                ptr2+=2
                if ptr1==len(s)-1:
                    res += dic[s[ptr1]]
        return res

