#include <iostream>
#include <list>

using namespace std;

int main()
{
    list<int>rn;         //Rn
    list<int>sum;        //前Rn的累加和


    int n = 500;         //计算500位
    rn.push_back(2);     //R1的第一位初始化为2;
    sum.push_back(2);    //sum的第一位初始化为2;

    for(int i = 1; i < n; ++i)
        rn.push_back(0), sum.push_back(0);  //Rn和sum的其他位初始化为0
    list<int>::reverse_iterator rit1, rit2; //逆序迭代器
    list<int>::iterator it;                 //正序迭代器
    int temp, ret;
    for(int i = 1; i < 500; i ++)
    {
        //R(n) = R(n-1)*i/(2*i+1)

        //乘法
        ret = 0;
        for(rit1 = rn.rbegin(); rit1 != rn.rend(); ++rit1)
        {
            temp = *rit1*i+ret;
            *rit1 = temp%10;
            ret = temp/10;
        }

        //除法
        ret = 0;
        for(it = rn.begin(); it != rn.end(); ++it)
        {
            temp = (*it+ret*10);
            *it = temp/(2*i+1);
            ret = temp%(2*i+1);
        }

        //加法,计算sum
        ret = 0;
        for(rit1 = sum.rbegin(), rit2 = rn.rbegin(); rit1 != sum.rend()&& rit2!=rn.rend(); ++rit1, ++rit2)
        {
            temp = *rit1 + *rit2+ret;
            *rit1 = temp%10;
            ret = temp/10;
        }
    }

    int i;
    cin >> i;
    it = sum.begin();
    cout << *it << ".";
    it ++;
    while(it != sum.end() && i)
    {
        cout << *it;
        it++, i--;
    }

}