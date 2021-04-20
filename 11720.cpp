#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
	char input[100] = { 0, };
	int length, i, result = 0;
	scanf("%d", &length);
	scanf("%s", input);

	for (i = 0; i<length; i++)
		result += (input[i] - '0');

	printf("%d\n", result);

	return 0;
}