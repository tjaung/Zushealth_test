from PrivateNetwork import PrivateNetwork
from pprint import pprint
def main():
    test = PrivateNetwork()
    test.add_key(("Alice", "Bob")) # 1
    test.add_key(("Alice", "Carlos")) # 2
    test.add_key(("Alice", "David")) # 3
    test.add_key(("Alice", "Bob", "Carlos", "David")) # 4
    test.add_key(("Bob", "Carlos", "David")) # 5
    test.add_key(("Bob", "Alice")) # 6
    test.print_networks()

if __name__ == "__main__":
    main()