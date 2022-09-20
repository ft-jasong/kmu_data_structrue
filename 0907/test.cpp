#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	long long	sum;
	int	num;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		sum = 0;
		for (int i = 0; i < 10; i++) {
			cin >> num;
			if (num & 0x01)
				sum += num;
		}
		cout << '#' << test_case << ' ' << sum << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}