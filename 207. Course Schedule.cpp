class Solution {
public:    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // convert edge list to adjancent matrix
        vector<vector<int>> g(numCourses);
        for (auto i = 0; i < prerequisites.size(); i++) 
            g[prerequisites[i][0]].push_back(prerequisites[i][1]);
        
        vector<int> explored(numCourses, 0);
        for (auto i = 0; i < numCourses; i++) {
            if(has_cycle(g, i, explored))
                return false;
        }
        return true;    
    }
    
    // return true iff a cycle (starting from node) is detected
    bool has_cycle(vector<vector<int>>& g, int node, vector<int>& explored) {
        // if node is fully explored, then skip
        if (explored[node] == 2)
            return false;    
        // mark node as being explored
        explored[node] = 1;
        if (!g[node].empty()) {
            for (auto i : g[node]) {
                // if i is not explored
                if (explored[i] == 0)
                    has_cycle(g, i, explored);
                // if i is being explored, then a cycle is detected
                if (explored[i] == 1)
                    return true;
            }
        }
        // mark node as fully explored
        explored[node] = 2;
        return false;
    }
};
