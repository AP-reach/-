class Solution {

    int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    class Barrier {
        int[] parent;
        int[] rank;

        public Barrier(char[][] board) {
            int m = board.length;
            int n = board[0].length;
            parent = new int[m * n];
            rank = new int[m * n];
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (board[i][j] == 'O') {
                        parent[i * n + j] = i * n + j;
                        rank[i * n + j] = 1;
                    }
                }
            }
        }

        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }

    }

    public void solve(char[][] board) {
        Barrier barrier = new Barrier(board);
        HashSet<Integer> unBoards = new HashSet<>();
        // 记录包含边界的并查集，其他全部刷成X
        int m = board.length;
        int n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    for (int k = 0; k < 4; k++) {
                        int x = i + directions[k][0];
                        int y = j + directions[k][1];
                        if (x >= 0 && x < m && y >= 0 && y < n && board[x][y] == 'O') {
                            barrier.union(i * n + j, x * n + y);
                        }
                    }
                    if (i == 0 || i == m - 1 || j == 0 || j == n - 1) {
                        unBoards.add(barrier.find(i * n + j));
                    }
                }
            }
        }
        // 开始刷被包围的点
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O' && !unBoards.contains(barrier.find(i * n + j))) {
                    board[i][j] = 'X';
                }
            }
        }
    }
}

