#include <algorithm>
#include <iostream>
#include <vector>

struct Edge {
    Edge() : u(0), v(0), distance(0) {}
    Edge(std::size_t u, std::size_t v, int distance) : u(u), v(v), distance(distance) {}
    std::size_t u;
    std::size_t v;
    int distance;
};

struct Node {
    Node(std::size_t index) : index(index), parent(this), rank(0) {}
    std::size_t index;
    Node *parent;
    std::size_t rank;
};

class UnionFind {
  public: 
    UnionFind(std::size_t N) : _nodes(N) {
        for (std::size_t i = 0; i < N; ++i) {
            _nodes[i] = new Node(i);
        }
    }

    ~UnionFind() {
        for (std::size_t i = 0; i < _nodes.size(); ++i) {
            delete _nodes[i];
        }
    }

    std::size_t find(std::size_t x) {
        return find(_nodes[x])->index;
    }

    bool union_(std::size_t x, std::size_t y) {
        auto rx = find(_nodes[x]);
        auto ry = find(_nodes[y]);
        if (rx == ry) 
            return false;
        if (rx->rank == ry->rank) {
            rx->rank++; 
            ry->parent = rx;
        }
        else if (rx->rank > ry->rank)
            ry->parent = rx;
        else 
            rx->parent = ry;
        return true;
    }

  private:
    Node* find(Node *x) {
        if (x != x->parent) 
            x->parent = find(x->parent);
        return x->parent;
    }

    std::vector<Node*> _nodes;
};

std::vector<Edge> kruskal(size_t n, std::vector<Edge> edges) {
    UnionFind uf(n);
    std::vector<Edge> mst;
    std::sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.distance < b.distance;
    });
    for (const Edge& e : edges) {
        if (uf.union_(e.u, e.v))
            mst.push_back(e);
    } 
    return mst;
}

int main(int argc, char **argv) {
    size_t n, m;
    std::cin >> n >> m;
    while (n != 0 && m != 0) {
        std::vector<Edge> edges(m);
        int totEco = 0;
        for (size_t i = 0; i < m; ++i) {
            size_t u, v;
            int w;
            std::cin >> u >> v >> w;
            edges[i] = Edge(u, v, w);
            totEco += w;
        }
        auto mst = kruskal(n, edges);
        for (size_t i = 0; i < mst.size(); ++i) {
            totEco -= mst[i].distance;
        }
        std::cout << std::fixed;
        std::cout << totEco << std::endl;
        std::cin >> n >> m;
    }
}