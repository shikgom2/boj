#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool visited[1001];

int main(void)
{
	int L, N;
	cin >> L;

	vector<int> luckySet(L + 1, 0);

	for (int i = 1; i <= L; i++)
	{
		cin >> luckySet[i];

		visited[luckySet[i]] = true;
	}

	cin >> N;

	if (visited[N])
	{
		cout << 0 << "\n";

		return 0;
	}

	sort(luckySet.begin(), luckySet.end());

	int left = 0;
	int right = 0;

	for (int i = 0; i < L; i++)
	{
		if (luckySet[i] <= N && luckySet[i + 1] > N)
		{
			left = luckySet[i];
			right = luckySet[i + 1];

			break;
		}
	}

	cout << (N - left) * (right - N) - 1 << "\n";

	return 0;
}