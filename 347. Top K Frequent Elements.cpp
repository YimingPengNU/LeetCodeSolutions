class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        if (nums.size() == 1 && k == 1)
            return nums;
        sort(nums.begin(), nums.end());
        vector<int> nums_copy(nums.size(), 0);
        copy(nums.begin(), nums.end(), nums_copy.begin());
        auto it = unique(nums_copy.begin(), nums_copy.end());
        nums_copy.resize(distance(nums_copy.begin(), it));
        unordered_map<int, int> hash;
        for (it = nums_copy.begin(); it != nums_copy.end(); ++it) {
             hash.insert({*it, count(nums.begin(), nums.end(), *it)});
        }
        auto comp =  [&] (int& i, int& j) {
            return hash.at(i) < hash.at(j);
        };
        priority_queue<int, vector<int>, decltype(comp)> heap(comp);
        for (it = nums_copy.begin(); it != nums_copy.end(); ++it) {
             heap.push(*it);
        }
        vector<int> res;
        for (int i = 0; i < k; ++i) {
            res.push_back(heap.top());
            heap.pop();
        }
        return res;
    }
};
