/*
 * Design and analysis of Algorithms II
 * Week 5
 * Traveling Salesman Problem
 * Bottom up approach
 */

#include <vector>
#include <unordered_map>
#include <cmath>
#include <algorithm>
#include <cstdio>

#define min2(a,b) ( (a) < (b) ? (a) : (b) )
#define max2(a,b) ( (a) > (b) ? (a) : (b) )

using namespace std;

double distance(pair<double, double> a, pair<double, double> b)
{
    return sqrt( (a.first-b.first) * (a.first-b.first) +
                (a.second-b.second) * (a.second-b.second) );
}

vector<int> construct_sets(int m, int n, int i)
{
    if (m == 0)
        return vector<int>(1,0);
    vector<int> r;
    for ( int x : construct_sets(m-1, n-1, i*2) )
        r.push_back(x | i);
    if (m < n)
    {
        vector<int> k = construct_sets(m, n-1, i*2);
        r.insert(r.end(), k.begin(), k.end());
    }
    return r;
}

vector<int> get_sets(int m, int n)
{
    vector<int> r = construct_sets(m-1, n-1, 1);
    /* transform(r.begin(), r.end(), r.begin(), [](int x) -> int { return x | 0x01; }); */
    return r;
}

int remove_from_set(int s, int j)
{
    return s & ~(0x01 << (j-1));
}

vector<int> get_elem(int s, int exclude = -1)
{
    if (exclude != -1 && exclude !=0)
        s = remove_from_set(s, exclude);
    vector<int> r;
    if (exclude != 0)
        r.push_back(0);
    int i = 1;
    while (s)
    {
        if (s & 0x01)
            r.push_back(i);
        ++i;
        s >>= 1;
    }
    return r;
}

int main()
{
    int n;
    double a, b;
    vector< pair<double, double> > mapa;
    scanf("%d", &n);

    for (int i=0; i<n; ++i)
    {
        scanf("%lf%lf", &a, &b);
        mapa.push_back(make_pair(a,b));
    }

    vector< vector<double> > A = vector< vector<double> >(0x01 << (n-1), vector<double>(n, INT_MAX));

    A[1][0] = 0.0;

    for (int m=2; m<=n; ++m)
    {
        printf("m %d\n", m);
        for (int s : get_sets(m, n))
            for (int j : get_elem(s, 0))
                for (int k : get_elem(s, j))
                    if (k==0)
                        A[s][j] = min2(A[s][j], A[s][k] + distance(mapa[j], mapa[k]));
                    else
                        A[s][j] = min2(A[s][j], A[remove_from_set(s,j)][k] + distance(mapa[j], mapa[k]));
    }

    double r = INT_MAX;

    for (int j=1; j<=n; ++j)
        r = (double) min2(r, A[get_sets(n,n)[0]][j] + distance(mapa[j], mapa[0]));

    printf("%d\n", (int) r);

    return 0;
}

