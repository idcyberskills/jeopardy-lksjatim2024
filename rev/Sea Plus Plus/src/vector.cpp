#include <bits/stdc++.h> 
#include <vector> 
using namespace std; 
  
int main() {

    std::string input;
    std::cout << "Welcome to easy RE LKS JATIM! Please enter LKS Flag: ";
    std::cin >> input;

    if (input.length() != 25 && input[0] != 'L' && input[1] != 'K' && input[2] != 'S' && input[3] != 'J' && input[4] != 'A' && input[5] != 'T' && input[6] != 'I' && input[7] != 'M' && input[8] != '{' && input[24] != '}') {
        std::cout << "Your flag should be in form of LKSJATIM{.*}, and looks like the length is still incorrect!" << std::endl;
        return -1;
    }
	
	char flag[15] = {'c', 'p', '_', 'r', 'v', '0', 'c', '5', 'w', '4', 't', '+', '3', '_', '+'};
	std::vector<char> vec(15);
	for(int i=9; i < 25; i++){
		vec[i-9] = input[i];
	}
	std::vector<std::pair<int, int>> swaps = {
        {0, 14}, {1, 2}, {2, 13}, {3, 11}, {4, 6}, {5, 4},
        {6, 0}, {7, 8}, {8, 7}, {9, 9}, {10, 3}, {11, 5},
        {12, 1}, {13, 10}, {14, 12}
    };

	for (int i = 0; i < 3317; i++){
		    for (const auto& swap : swaps) {
        		std::swap(vec[swap.first], vec[swap.second]);
    		}
	}
	
	std::cout << "Checking for your LKS Flag . . ." << std::endl;
    for (std::size_t i = 0; i < vec.size(); ++i) {
        if (vec.at(i) != flag[i]) {
            std::cout << "Wrong!" << std::endl;
            return -1;
        }
    }
    std::cout << "Correct! Submit the flag! Thaks for solving easy RE ^-^ " << std::endl;
    return 1;
}
