#include <iostream>
#include <vector>

void makeChange(int amount) {
    std::vector<int> coins = {25, 10, 5, 1};
    std::vector<int> coinCount(coins.size(), 0);
    // 遍历每种面额
    for (size_t i = 0; i < coins.size(); ++i) {
        coinCount[i] = amount / coins[i];
        amount %= coins[i];
    }


    std::cout << "找零结果：" << std::endl;
    for (size_t i = 0; i < coins.size(); ++i) {
        if (coinCount[i] > 0) {
            std::cout << coins[i] << "美分: " << coinCount[i] << "个" << std::endl;
        }
    }
}

int main() {
    int amount;
    std::cout << "请输入金额（美分）: ";
    std::cin >> amount;

    makeChange(amount);

    return 0;
}