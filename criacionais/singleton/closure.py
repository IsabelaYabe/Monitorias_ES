def counter(start: int = 0):
    count = start
    def increment():
        nonlocal count # Count is a free variable
        count += 1
        return count
    return increment

if __name__ == "__main__":
    c = counter()
    print(c())  # Output: 1
    print(c())  # Output: 2 
    print(c())  # Output: 3