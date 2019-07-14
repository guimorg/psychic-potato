from utils import mem_address


# Checking name scope
def fun_1():
    in_scope_var = 5
    print(mem_address(in_scope_var)


def fun_2():
    in_scope_var = 5
    print(mem_address(in_scope_var)

if __name__ == "__main__":
    fun_1()
    fun_2()