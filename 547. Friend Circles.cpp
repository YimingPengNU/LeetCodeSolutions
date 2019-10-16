class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int count = 0;
        vector<int> visited(M.size(), 0);
        for (int i = 0; i != M.size(); ++i) {
            if (!visited[i]) {
                count++;
                dfs(M, i, visited);
            }
        }
        return count;
    }
    
    void dfs(vector<vector<int>>& M, int i, vector<int>& visited) {
        visited[i] = 1;
        for (int j = 0; j != M[i].size(); ++j) {
            if (M[i][j] && !visited[j])
                dfs(M, j, visited);
        }
    }
};
