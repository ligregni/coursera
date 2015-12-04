/* Design and Analysis of Algorithms - Part II */

#include <cstdio>
#include <vector>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int
get_random(int n)
{
    return rand() % n;
}

inline bool
get_value(int x, bool b)
{
    return(  x / abs(x) ) < 0 ? !b : b;
}

void
print_vector(vector<int> v)
{
    for (auto x : v)
        cout << x << endl;
}

void
print_vector(vector<bool> v)
{
    for (auto x : v)
        cout << x << endl;
}

bool
check_clause(vector<int> &clauses, vector<bool> &variables)
{
    return get_value(clauses[0], variables[abs(clauses[0])]) || get_value(clauses[1], variables[abs(clauses[1])]);
}

int
preprocess(vector< vector<int> > &clauses, vector<bool> &variables)
{
    vector<bool> positives(variables.size());
    vector<bool> negatives(variables.size());
    vector<bool> discarded_variables(variables.size(), false);
    vector<bool> discarded_clauses(clauses.size(), false);
    bool changed = true;

    while ( changed )
    {
        changed = false;
        fill(positives.begin(), positives.end(), false);
        fill(negatives.begin(), negatives.end(), false);
        for (int i=0; i<clauses.size(); ++i)
        {
            if (!discarded_clauses[i])
                for (int j=0; j<2; ++j)
                    if ( clauses[i][j] < 0 )
                        negatives[-clauses[i][j]] = true;
                    else
                        positives[clauses[i][j]] = true;
        }


        for (int i=1; i<variables.size(); ++i)
        {
            if (positives[i] != negatives[i])
            {
                discarded_variables[i] = true;
            }
        }

        for (int j=0; j<clauses.size(); ++j)
        {
            if (!discarded_clauses[j] && (discarded_variables[abs(clauses[j][0])] || discarded_variables[abs(clauses[j][1])]))
            {
                changed = true;
                discarded_clauses[j] = true;
            }
        }
    }

    vector< vector<int> > new_clauses;

    for (int j=0; j<clauses.size(); ++j)
        if (!discarded_clauses[j])
            new_clauses.push_back(clauses[j]);

    clauses.clear();
    clauses.insert(clauses.begin(), new_clauses.begin(), new_clauses.end());
    
    return 0;
}

vector<int>
check_clauses(vector< vector<int> > &clauses, vector<bool> &variables)
{
    vector<int> falses;
    for (int i=0; i < clauses.size(); ++i)
        if (!check_clause(clauses[i], variables))
            falses.push_back(i);
    return falses;
}

bool
local_search(vector< vector<int> > &clauses, vector<bool> &variables)
{
    for (int i=1; i<=variables.size(); ++i)
        variables[i] = get_random(2) == 0;

    unsigned long long iterations = 2 * (variables.size()-1) * (variables.size()-1);
    //unsigned long long iterations = 2 * (variables.size()-1);

    for (int i=0; i<iterations; ++i)
    {
        if (i % 10000 == 0)
            printf("%d %llu, %d\n", i, iterations, clauses.size());
        vector<int> falses = check_clauses(clauses, variables);
        if (falses.size() == 0)
            return true;
        int var_to_modify = abs(clauses[falses[get_random(falses.size())]][get_random(2)]);
        variables[var_to_modify] = !variables[var_to_modify];
    }

    return check_clauses(clauses, variables).size() == 0;
}

int
main()
{
    int n, a, b;
    bool result = false;
    srand(time(0));
    scanf("%d", &n);
    vector<bool> variables = vector<bool>(n+1);
    vector< vector<int> > clauses;
    while (scanf("%d%d", &a, &b) == 2)
    {
        vector<int> clause(2);
        clause[0] = a;
        clause[1] = b;
        clauses.push_back(clause);
    }

    preprocess(clauses, variables);

    for (int i=0; !result && i<log2(n)+1; ++i)
    {
        printf("+%d, %d\n", i, (int) log2(n)+1);
        result |= local_search(clauses, variables);
    }
    printf("%s\n", result ? "satisfiable" : "unsatisfiable");
    return 0;
}

