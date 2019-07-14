#include <iostream>


int main(){
    int list_var[4] = {1, 55, 3, 350};

    for (int i = 0; i < 4; i++){
        std::cout << "list_var[" << i << "]" << "\n";
        std::cout << list_var[i] << "\n";
        std::cout << "mem_address " << &list_var[i] << "\n\n";
    };

    return 0;
}