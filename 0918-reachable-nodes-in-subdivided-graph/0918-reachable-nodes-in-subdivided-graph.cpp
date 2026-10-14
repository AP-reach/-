class Solution {
public:
    int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
        int ans { 0 };
        if(n == 1){
            return 1;
        }
        if(!maxMoves){
            return 1;
        }
        // minimize weight: Dijkstra
        vector<vector<int>> weight(n,vector<int>(n,0));
        vector<int> len(n,INT_MAX); 
        vector<bool> visited(n,false);
        for( const auto& edge: edges ){
            weight[edge[1]][edge[0]] = edge[2] + 1;
            weight[edge[0]][edge[1]] = edge[2] + 1;

        }   
        len[0] = 0;
        pair<int,int> cache(0,0),dist;
        priority_queue<pair<int, int>, vector<pair<int, int>>,greater<pair<int, int>>> pq;
        pq.push(cache);

        while(!pq.empty()){
            cache = pq.top();
            if(!visited[cache.second]){
                pq.pop();
                len[cache.second] = cache.first;
                visited[cache.second] = true;
                for(int i = 0; i < n; ++i){
                    if(weight[cache.second][i] && !visited[i]){
                        dist.first = min(len[i] , cache.first + weight[cache.second][i]);
                        dist.second = i;
                        pq.push(dist);
                    }
                }
            }
            else{
                pq.pop();
            }
        }
        for(auto& i : len){
            if(i <= maxMoves){
                ++ans;
            }
            i = max(maxMoves - i , 0) ;
        }
        for(int i = 0; i < n - 1; ++i){
            for(int j = i + 1 ; j < n ; ++j){
                if(weight[i][j] > 0 && (len[i] < INT_MAX && len[j] < INT_MAX))
                ans += min(len[i] + len[j] , weight[i][j] - 1) ;
            }
        }

        return ans;


    }
};