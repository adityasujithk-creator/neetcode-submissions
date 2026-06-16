class Solution:
    def getConcatenation(self, n: List[int]) -> List[int]:
        nums = n;
        a = len(nums);
        ans = [0] * (2 * a);
        for i in range(0,a):
            ans[i] = n[i];
            ans[i+a] = n[i];
        return ans;