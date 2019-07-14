#include <iostream>


int main(){
    int list_var[5] = {1, 2, 3, 4, 5};

    std::cout << "list_var " << &list_var << "\n";
    std::cout << "list_var[0] " << &list_var[0] << "\n";

    return 0;
}