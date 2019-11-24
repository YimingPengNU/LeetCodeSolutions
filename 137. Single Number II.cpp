class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> map;
        for (auto num : nums) {
            if (map.find(num) != map.end())
                map[num]++;
            map.insert({num, 1});
        }
        for (auto it = map.begin(); it != map.end(); it++) {
            if (it->second == 1)
                return it->first;
        }
        return 0;
    }
};
