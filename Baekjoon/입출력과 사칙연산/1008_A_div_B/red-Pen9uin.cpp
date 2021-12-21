// 작성자: red-Pen9uin

#include<iostream>
using namespace std;
int main(void)
{
        int a,b;
        cin >> a >> b;
//      cout.unsetf(ios::fixed);
//      cout << (double)a/b;
        printf("%.10lf", (double)a/b);

        return 0;
}
