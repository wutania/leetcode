class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if (len(a) < len(b)):
            temp = a
            a = b
            b = temp
        a = list(a)
        b = list(b)
        a.reverse()
        b.reverse()
        c = []
        carry = 0
        for i in range(len(a)):
            a1 = int(a[i])
            if (i > len(b)-1):
                b1 = 0
            else:
                b1 = int(b[i])
            k = a1 + b1 + carry
            if (k == 2 or k == 3):
                k = k -2
                carry = 1
            elif (k == 0 or k == 1):
                carry = 0
            c.append(k)
            print("c: ", c)
        if (carry != 0):
            c.append(carry)
        c.reverse()
        return "".join(map(str,c))
