/* Solution of "Two Sum" problem at https://leetcode.com/problems/two-sum/. */
#include <cstdlib>
#include <iostream>
#include <unordered_map>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::unordered_map;
using std::vector;


class Solution {
public:
    vector<int> naiveTwoSum(vector<int> &nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) return {i, j};
            }
        }
        return {};
    }

    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> seen;
        for (size_t i = 0; i < nums.size(); i++) {
            auto it = seen.find(target - nums[i]);
            if (it != seen.end() && it->second != i) {
                return {it->second, i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};


int solve() {
    int n, target;
    cin >> n >> target;
    vector<int> nums(n);

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    auto answer = Solution().twoSum(nums, target);
    cout << answer[0] << " " << answer[1] << endl;
    return 0;
}


int stress_test() {
    while (true) {
        // random numbers
        int n = rand() % 100 + 2;
        cout << "size=" << n <<endl;
        vector<int> nums;
        for (int i = 0; i < n; i++) {
            nums.push_back(rand() % 100);
        }

        // random indexes and target
        int i = rand() % n;
        int j = rand() % n;
        long target = nums[i] + nums[j];
        cout << "target=" << target << endl;

        // compare naive and final solution
        Solution s = Solution();

        auto effec_result = s.twoSum(nums, target);
        int effec_i = effec_result[0];
        int effec_j = effec_result[1];
        cout << nums[effec_i] << " " << nums[effec_j] << endl;

        auto naive_result = s.naiveTwoSum(nums, target);
        int naive_i = naive_result[0];
        int naive_j = naive_result[1];
        cout << nums[naive_i] << " " << nums[naive_j] << endl;

        if (effec_i != naive_i) {
            cout << "Error: got i=" << effec_i << " should be i=" << naive_i << endl;
            break;
        } else if (effec_j != naive_j) {
            cout << "Error: got j=" << effec_j << " should be j=" << naive_j << endl;
            break;
        } else {
            cout << "OK" << endl;
        }
    }
    return 0;
}


int main() {
    return stress_test();
}

