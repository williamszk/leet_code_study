# One of the challenges in Hacker Rank is this challenge
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hold1 = [0]*26
        for letter in s:
            idx = ord(letter)-ord("a")
            hold1[idx] += 1

        hold2 = [0]*26
        for letter in t:
            idx = ord(letter)-ord("a")
            hold2[idx] += 1

        sum_now = sum([abs(x-y) for x,y in zip(hold1, hold2)]) // 2

        return sum_now


def main():
    s = "bab"
    t = "aba"
    output = 1
    sol = Solution()
    assert sol.minSteps(s, t) == output

    s = "leetcode"
    t = "practice"
    output = 5
    sol = Solution()
    assert sol.minSteps(s, t) == output

    s = "anagram"
    t = "mangaar"
    output = 0
    sol = Solution()
    assert sol.minSteps(s, t) == output


if __name__ == "__main__":
    main()
