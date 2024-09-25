public class Solution
{
    public int PivotIndex(int[] nums)
    {
        int sum = nums.Sum();
        int left = 0;
        int right = sum;
        for (int i = 0; i < nums.Length; i++)
        {
            right -= nums[i];
            if (left == right) return i;
            left += nums[i];
        }

        return -1;
    }
}