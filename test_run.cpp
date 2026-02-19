#include <iostream>
#include <chrono>
#include <thread>
int main(){ std::cout << "STDOUT: " << 42 << std::endl; std::this_thread::sleep_for(std::chrono::milliseconds(50)); return 0; }
