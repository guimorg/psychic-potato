from utils import mem_address


if __name__ == "__main__":
    list_var = [1, 55, 3, 350]

    for ix in range(len(list_var)):
        print(f"{list_var[ix]}: {mem_address(list_var[ix])}\n")