class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() < 2)
            return s.size();
        int maxLen = 1;
        int i = 0;
        int j = 0;
        unordered_set substr{s[i]};
        while (i < s.size() && j < s.size()) {
            if (substr.find(s[j+1]) == substr.end() && (j+1) < s.size()) {
                j++;
                substr.insert(s[j]);
                int len = j - i + 1;
                if (len > maxLen)
                    maxLen = len;
            }            
            else {
                substr.erase(s[i]);
                i++;    
            }                       
        }
        return maxLen;
    }
};
