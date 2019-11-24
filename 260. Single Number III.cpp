class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int> res;
        unordered_map<int, int> map;
        for (auto num : nums) {
            if (map.find(num) != map.end())
                map[num]++;
            map.insert({num, 1});
        }
        for (auto it = map.begin(); it != map.end(); it++) {
            if (it->second == 1)
                res.push_back(it->first);
        }
        return res;
    }
};
