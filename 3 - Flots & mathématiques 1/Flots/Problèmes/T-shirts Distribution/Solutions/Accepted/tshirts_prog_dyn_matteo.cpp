#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<int>> flow_value;
vector<vector<int>> capacity;
vector<vector<int>> neighbors;
int INF = 100000;

int find_augm_path(int s, int t, vector<int>& parent) {
    fill(begin(parent), end(parent), -1);
    parent[s] = -2;
    queue<pair<int, int>> q;
    q.push({s, INF});
    while (!q.empty()) {
        int cur = q.front().first;
        int flow = q.front().second;
        q.pop();

        for (int next : neighbors[cur]) {
            if (parent[next] == -1 && capacity[cur][next] > 0) {
                parent[next] = cur;
                int new_flow = min(flow, capacity[cur][next]);
                if (next == t) {
                    return new_flow;
                }
                q.push({next, new_flow});
            }
        }
    }
    return 0;
}

int max_flow(int s, int t) {
    int flow = 0;
    vector<int> parent(n);
    int new_flow;
    while ((new_flow = find_augm_path(s, t, parent)) > 0) {
        flow += new_flow;
        int cur = t;
        while (cur != s) {
            int prev = parent[cur];
            flow_value[prev][cur] += new_flow;
            capacity[prev][cur] -= new_flow;
            flow_value[cur][prev] -= new_flow;
            capacity[cur][prev] += new_flow;
            cur = prev;
        }
    }
    return flow;
}

void add_edge(int from, int to, int weight)
{
    capacity[from][to] = weight;
    capacity[to][from] = 0;
    neighbors[from].push_back(to);
    neighbors[to].push_back(from);
}

enum Nodes {
    NODE_SOURCE,
    NODE_SINK,
    NODE_S,
    NODE_M,
    NODE_L,
    NODE_XL,
    NODE_XXL,
    NODE_XXXL,
    NODE_S_OR_M,
    NODE_M_OR_L,
    NODE_L_OR_XL,
    NODE_XL_OR_XXL,
    NODE_XXL_OR_XXXL,
    MAX_NODE
};

int main() {
    int S, M, L, XL, XXL, XXXL;
    cin >> S >> M >> L >> XL >> XXL >> XXXL;

    int participants;
    cin >> participants;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    n = MAX_NODE;
    flow_value = vector<vector<int>>(n, vector<int>(n));
    capacity = vector<vector<int>>(n, vector<int>(n));
    neighbors = vector<vector<int>>(n);

    add_edge(NODE_SOURCE, NODE_S, 0);
    add_edge(NODE_SOURCE, NODE_M, 0);
    add_edge(NODE_SOURCE, NODE_L, 0);
    add_edge(NODE_SOURCE, NODE_XL, 0);
    add_edge(NODE_SOURCE, NODE_XXL, 0);
    add_edge(NODE_SOURCE, NODE_XXXL, 0);
    add_edge(NODE_SOURCE, NODE_S_OR_M, 0);
    add_edge(NODE_SOURCE, NODE_M_OR_L, 0);
    add_edge(NODE_SOURCE, NODE_L_OR_XL, 0);
    add_edge(NODE_SOURCE, NODE_XL_OR_XXL, 0);
    add_edge(NODE_SOURCE, NODE_XXL_OR_XXXL, 0);

    add_edge(NODE_S_OR_M, NODE_S, participants);
    add_edge(NODE_S_OR_M, NODE_M, participants);
    add_edge(NODE_M_OR_L, NODE_M, participants);
    add_edge(NODE_M_OR_L, NODE_L, participants);
    add_edge(NODE_L_OR_XL, NODE_L, participants);
    add_edge(NODE_L_OR_XL, NODE_XL, participants);
    add_edge(NODE_XL_OR_XXL, NODE_XL, participants);
    add_edge(NODE_XL_OR_XXL, NODE_XXL, participants);
    add_edge(NODE_XXL_OR_XXXL, NODE_XXL, participants);
    add_edge(NODE_XXL_OR_XXXL, NODE_XXXL, participants);

    add_edge(NODE_S, NODE_SINK, S);
    add_edge(NODE_M, NODE_SINK, M);
    add_edge(NODE_L, NODE_SINK, L);
    add_edge(NODE_XL, NODE_SINK, XL);
    add_edge(NODE_XXL, NODE_SINK, XXL);
    add_edge(NODE_XXXL, NODE_SINK, XXXL);

    vector<int> participant_choices;
    participant_choices.reserve(participants);

    for (int i = 0; i < participants; ++i)
    {
        string choices;
        getline(cin, choices);

        if (choices == "S")
        {
            ++capacity[NODE_SOURCE][NODE_S];
            participant_choices.push_back(NODE_S);
        }
        else if (choices == "S,M")
        {
            ++capacity[NODE_SOURCE][NODE_S_OR_M];
            participant_choices.push_back(NODE_S_OR_M);
        }
        else if (choices == "M")
        {
            ++capacity[NODE_SOURCE][NODE_M];
            participant_choices.push_back(NODE_M);
        }
        else if (choices == "M,L")
        {
            ++capacity[NODE_SOURCE][NODE_M_OR_L];
            participant_choices.push_back(NODE_M_OR_L);
        }
        else if (choices == "L")
        {
            ++capacity[NODE_SOURCE][NODE_L];
            participant_choices.push_back(NODE_L);
        }
        else if (choices == "L,XL")
        {
            ++capacity[NODE_SOURCE][NODE_L_OR_XL];
            participant_choices.push_back(NODE_L_OR_XL);
        }
        else if (choices == "XL")
        {
            ++capacity[NODE_SOURCE][NODE_XL];
            participant_choices.push_back(NODE_XL);
        }
        else if (choices == "XL,XXL")
        {
            ++capacity[NODE_SOURCE][NODE_XL_OR_XXL];
            participant_choices.push_back(NODE_XL_OR_XXL);
        }
        else if (choices == "XXL")
        {
            ++capacity[NODE_SOURCE][NODE_XXL];
            participant_choices.push_back(NODE_XXL);
        }
        else if (choices == "XXL,XXXL")
        {
            ++capacity[NODE_SOURCE][NODE_XXL_OR_XXXL];
            participant_choices.push_back(NODE_XXL_OR_XXXL);
        }
        else if (choices == "XXXL")
        {
            ++capacity[NODE_SOURCE][NODE_XXXL];
            participant_choices.push_back(NODE_XXXL);
        }
        else
        {
            cout << "Choix invalide : " << choices << '\n';
            return 1;
        }
    }

    int result = max_flow(NODE_SOURCE, NODE_SINK);

    if (result == participants)
    {
        cout << "YES\n";

        for (int i = 0; i < participants; ++i)
        {
            auto choice = participant_choices[i];

            switch (choice)
            {
            case NODE_S_OR_M:
                if (flow_value[NODE_S_OR_M][NODE_S] > 0)
                {
                    --flow_value[NODE_S_OR_M][NODE_S];
                    choice = NODE_S;
                }
                else
                {
                    choice = NODE_M;
                }
                break;

            case NODE_M_OR_L:
                if (flow_value[NODE_M_OR_L][NODE_M] > 0)
                {
                    --flow_value[NODE_M_OR_L][NODE_M];
                    choice = NODE_M;
                }
                else
                {
                    choice = NODE_L;
                }
                break;

            case NODE_L_OR_XL:
                if (flow_value[NODE_L_OR_XL][NODE_L] > 0)
                {
                    --flow_value[NODE_L_OR_XL][NODE_L];
                    choice = NODE_L;
                }
                else
                {
                    choice = NODE_XL;
                }
                break;

            case NODE_XL_OR_XXL:
                if (flow_value[NODE_XL_OR_XXL][NODE_XL] > 0)
                {
                    --flow_value[NODE_XL_OR_XXL][NODE_XL];
                    choice = NODE_XL;
                }
                else
                {
                    choice = NODE_XXL;
                }
                break;

            case NODE_XXL_OR_XXXL:
                if (flow_value[NODE_XXL_OR_XXXL][NODE_XXL] > 0)
                {
                    --flow_value[NODE_XXL_OR_XXXL][NODE_XXL];
                    choice = NODE_XXL;
                }
                else
                {
                    choice = NODE_XXXL;
                }
                break;
            }

            switch (choice)
            {
                case NODE_S: cout << "S\n"; break;
                case NODE_M: cout << "M\n"; break;
                case NODE_L: cout << "L\n"; break;
                case NODE_XL: cout << "XL\n"; break;
                case NODE_XXL: cout << "XXL\n"; break;
                case NODE_XXXL: cout << "XXXL\n"; break;
            }
        }
    }
    else
    {
        cout << "NO\n";
    }
}
