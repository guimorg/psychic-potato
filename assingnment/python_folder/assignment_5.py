import copy
from utils import mem_address


if __name__ == "__main__":
    frst_dict = {'key': {'chave': 'valor'}}
    
    # First approach: assignment
    scnd_dict = frst_dict

    print(f'frst_dict: {frst_dict}\n')
    print(mem_address(frst_dict))
    for key, value in frst_dict.items():
        print(f"{key}({mem_address(key)}):{value}({mem_address(value)})")
    print()
    
    print(f'\nscnd_dict: {scnd_dict}\n')
    print(mem_address(scnd_dict))
    for key, value in scnd_dict.items():
        print(f"{key}({mem_address(key)}):{value}({mem_address(value)})")
    print()

    # Second approach: copy
    thrd_dict = copy.copy(frst_dict)

    print(f'\nfrst_dict: {frst_dict}\n')
    print(mem_address(frst_dict))
    for key, value in frst_dict.items():
        print(f"{key}({mem_address(key)}):{value}({mem_address(value)})")
    print()
    
    print(f'\nthrd_dict: {thrd_dict}\n')
    print(mem_address(thrd_dict))
    for key, value in thrd_dict.items():
        print(f"{key}({mem_address(key)}):{value}({mem_address(value)})")
    print()

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
    import pdb; pdb.set_trace()