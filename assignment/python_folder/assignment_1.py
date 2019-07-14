from utils import mem_address


if __name__ == "__main__":
    # Assigning values to names
    int_var_1 = 5
    int_var_2 = 5

    # Printing memory addresses of names
    print(mem_address(int_var_1))
    print(mem_address(int_var_2))