class Solution {
public:
    int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
        if (n == 1) return 1;
        if (maxMoves == 0) return 1;

        vector<vector<pair<int, int>>> graph(n);
        for (const auto& e : edges) {
            int u = e[0], v = e[1], cnt = e[2];
            int w = cnt + 1;
            graph[u].push_back({v, w});
            graph[v].push_back({u, w});
        }

        vector<int> dist(n, INT_MAX);
        vector<bool> visited(n, false);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        dist[0] = 0;
        pq.push({0, 0});

        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (visited[u]) continue;
            visited[u] = true;
            for (auto [v, w] : graph[u]) {
                if (!visited[v] && d + w < dist[v]) {
                    dist[v] = d + w;
                    pq.push({dist[v], v});
                }
            }
        }

        int ans = 0;
        vector<int> remain(n, 0);
        for (int i = 0; i < n; ++i) {
            if (dist[i] <= maxMoves) {
                ++ans;
                remain[i] = maxMoves - dist[i];
            }
        }

        for (const auto& e : edges) {
            int u = e[0], v = e[1], cnt = e[2];
            int fromU = min(cnt, remain[u]);
            int fromV = min(cnt, remain[v]);
            ans += min(cnt, fromU + fromV);
        }
        return ans;
    }
};