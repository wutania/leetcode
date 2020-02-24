"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.
"""
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = ''
        a_count = 0
        
        for i in range(len(s)):
            print("l: ", l)
            print("a_count: ", a_count)
            if ((a_count > 1) or (len(l) > 2)):
                return False
            if s[i] == 'A':
                a_count += 1
                l = ''
            elif s[i] == 'P':
                l = ''
            elif s[i] == 'L':
                l = l + 'L'
        if ((a_count > 1) or (len(l) > 2)):
            return False
        return True
