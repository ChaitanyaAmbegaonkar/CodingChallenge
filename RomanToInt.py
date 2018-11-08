class Solution(object):
    def getVal(self,i):
        if i == 'X':
            return 10
        elif i == 'I':
            return 1
        elif i == 'V':
            return 5
        elif i == 'L':
            return 50
        elif i == 'C':
            return 100
        elif i == 'D':
            return 500
        elif i == 'M':
            return 1000

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = Solution()
        count = 0
        prev = ''
        for i in s:
            temp = a.getVal(i)
            if prev == i:
                count += temp
                if prev == '':
                    prev = i
            else:

                if prev == 'X' and i == 'L':
                    count += 30
                elif prev == 'X' and i == 'C':
                    count += 80
                elif prev == 'I' and i == 'V':
                    count += 3
                elif prev == 'I' and i == 'X':
                    count += 8
                elif prev == 'C' and i == 'D':
                    count += 300
                elif prev == 'C' and i == 'M':
                    count += 800
                else:
                    count += temp
                prev = i

        print count


s = "MCMXCIV"
sol = Solution()
sol.romanToInt(s)