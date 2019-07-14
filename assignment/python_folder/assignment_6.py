import copy
from utils import mem_address


if __name__ == "__main__":
    frst_dict = {'key': [1, 2, 3]}

    # Third approach: deep_copy
    frth_dict = copy.deepcopy(frst_dict)

    print(f'\nfrst_dict: {frst_dict}\n')
    print(mem_address(frst_dict))
    for key, value in frst_dict.items():
        print(f"{key}({mem_address(key)}):{value}({mem_address(value)})")
    print()
    
    print(f'\nfrth_dict: {frth_dict}\n')
    print(mem_address(frth_dict))
    for key, value in frth_dict.items():
        print(f"{key}({mem_address(key)}):{value}({mem_address(value)})")
    print()

    print('Appending 6 in frth_dict[key]')
    frth_dict['key'].append(6)
    print()

    print(f'\nfrst_dict: {frst_dict}\n')
    for key, value in frst_dict.items():
        print(f"{key}({mem_address(key)}):{value}({mem_address(value)})")
    print()
    
    print(f'\nfrth_dict: {frth_dict}\n')
    print(mem_address(frth_dict))
    for key, value in frth_dict.items():
        print(f"{key}({mem_address(key)}):{value}({mem_address(value)})")
    