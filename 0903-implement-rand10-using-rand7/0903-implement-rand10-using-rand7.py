# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        ran = (rand7()-1)*7 + rand7()
        #refusal sampling
        if ran <= 40:
            return ran%10 + 1
        else:
            return self.rand10()
        """
        :rtype: int
        """
        