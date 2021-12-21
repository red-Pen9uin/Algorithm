// 작성자: red-Pen9uin

#include<iostream>
using namespace std;

int main(void)
{
        int num1, num2;
        int n1, n2, n3;
        int result;

        cin >> num1 >> num2;

        result = num1*num2;

        n1 = num2/100;
        num2 %=100;
        n2 = num2/10;
        n3 = num2%10;

        cout << num1*n3 << '\n';
        cout << num1*n2 << '\n';
        cout << num1*n1 << '\n';
        cout << result << '\n';

        return 0;
}
