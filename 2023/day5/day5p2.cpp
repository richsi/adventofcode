#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>

int main() {
    std::ifstream file("test.txt");
    std::string line;
    std::vector<int> seeds;

    // Read the first line and extract integers
    if (std::getline(file, line)) {
        std::istringstream iss(line);
        std::string token;
        while (iss >> token) {
            seeds.push_back(token[0]);
        }
    }

    for (int i = 0; i < seeds.size(); ++i) {
        std::cout << seeds[i] << std::endl;
    }
    // std::cout << seeds << std::endl;

    // for (size_t i = 1; i < seeds.size(); ++i) {
    //     if (i % 2 == 1) {
    //         seeds[i] = seeds[i] + seeds[i - 1];
    //     }
    // }

    // std::vector<int> newSeeds;
    // for (size_t i = 1; i < seeds.size(); i += 2) {
    //     for (int j = seeds[i - 1]; j < seeds[i]; ++j) {
    //         newSeeds.push_back(j);
    //     }
    // }
    // seeds = newSeeds;

    // std::vector<int> res;
    // for (int seed : seeds) {
    //     bool changed = false;
    //     file.clear(); // Clear EOF flag
    //     file.seekg(0); // Go back to the start of the file
    //     for (int j = 0; std::getline(file, line) && j < 3; ++j) { }

    //     while (std::getline(file, line)) {
    //         if (line.empty() || isalpha(line[0])) {
    //             continue;
    //         }
    //         std::istringstream iss(line);
    //         std::vector<int> values;
    //         for (int val; iss >> val;) {
    //             values.push_back(val);
    //         }
    //         int start = values[1];
    //         int end = values[1] + values[2] - 1;
    //         int change = values[0] - values[1];

    //         if (start <= seed && seed <= end) {
    //             seed += change;
    //             changed = true;
    //         }
    //     }
    //     res.push_back(seed);
    // }

    // std::cout << *std::min_element(res.begin(), res.end()) << std::endl;
    // return 0;
}
