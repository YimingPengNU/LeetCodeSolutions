class Solution {
public:
    int longestStrChain(vector<string>& words) {
        unordered_map<string, int> dp = {};
        sort(words.begin(), words.end(),
            [] (const string& s1, const string& s2) {
                return s1.size() < s2.size();
            });
        for (string word:words) {
            int val = 1;
            for (int i = 0; i < word.size(); i++) {
                string subWord = word.substr(0, i) + word.substr(i+1, word.size() - i);
                auto it = dp.find(subWord);
                if (it != dp.end() && it->second + 1 > val)
                    val = it->second + 1;
            }
            dp.insert({word, val});
        }
        return max_element(dp.begin(), dp.end(), 
                                [] (const pair<string, int>& p1, const pair<string, int>& p2) {
                                    return p1.second < p2.second;
                                })->second;
    }
};
