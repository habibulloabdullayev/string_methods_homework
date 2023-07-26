def main(s):
    """
    A variable of type str is given. Check that it consists of letters only.
    Args:
        s: str
    Returns:
        bool: answer
    """
    
    return s.isalpha()
print(main('12345'))
print(main('2022ABC'))
print(main('hello'))