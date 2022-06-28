def main(s):
    """
    A string of length five is given. Return the index of the "*" character,
     return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s.count("*")!=0:
        n = s.index("*")
    else:
        n = False
    return n
        