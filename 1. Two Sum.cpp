class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        vector<int> res;
        for (auto i = 0; i < nums.size(); ++i) {
            auto found = hash.find(target - nums[i]);
            if (found != hash.end()) {
                res.push_back(found->second);
                res.push_back(i);
            }          
            hash.insert({nums[i], i});
        }
        return res;
    }
};
