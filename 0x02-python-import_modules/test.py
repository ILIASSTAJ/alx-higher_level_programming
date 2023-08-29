#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv)
    print(len(sys.argv))
    name = 'iliass'
    age = 22
    print(f"hey {name} you are {age}")
    print(f"{name}"
            f"{age}")
    print(f"{name}"
            "{age}")
    print(f"""{name}
    {age}""")



