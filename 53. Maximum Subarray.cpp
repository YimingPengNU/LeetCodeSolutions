#include <cmath>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int S = 0;
        int maxSub = nums[0];
        int minS = 0;
        for (int num : nums) {
            S += num;
            maxSub = max(maxSub, S - minS);
            minS = min(minS, S);
        }
        return maxSub;
    }
};
