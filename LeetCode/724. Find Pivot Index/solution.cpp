class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int length = nums.size ();
        int sum = 0;
        for (int i = 0; i < length; i++) 
            sum += nums[i];
            
        int left = 0, right = sum;
        for (int i = 0; i < length; i++) {
            right -= nums[i];
            if (left == right) return i;
            left += nums[i];
        }

        return -1;
    }
};