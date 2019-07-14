from utils import mem_address


if __name__ == "__main__":
    # Checking for mutable objects
    list_var = [1, 2, 3, 4, 5]

    print(mem_address(list_var))
    print(mem_address(list_var[0]))