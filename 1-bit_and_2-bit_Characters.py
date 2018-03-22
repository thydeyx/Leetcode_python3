# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2018-03-22 19时44分45秒
# Last modified : 2018-03-22 19时49分45秒
#     File Name : 1-bit_and_2-bit_Characters.py
#          Desc :

class Solution:
    def isOneBitCharacter(self, bits):
        n = len(bits)
        flag = [True for i in range(n)]
        i = 0
        while i < n - 1:
            if bits[i] == 1:
                i += 1
                flag[i] = False
            i += 1
        return flag[n-1]

if __name__ == "__main__":
    s = Solution()
    print(s.isOneBitCharacter([1,1,1,0]))

