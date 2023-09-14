def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    print(f"reverse: {fruit_list}")

    fruit_list.append("orange")
    print(f"append: {fruit_list}")

    apple = fruit_list.index("apple")
    fruit_list.insert(apple, "cherry")
    print(f"insert: {fruit_list}")

    fruit_list.remove("banana")
    print(f"remove: {fruit_list}")

    fruit_list.pop()
    print(f"pop: {fruit_list}")

    fruit_list.sort()
    print(f"sort: {fruit_list}")

    fruit_list.clear()
    print(f"clear: {fruit_list}")







main()