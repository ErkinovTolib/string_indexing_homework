from gettext import find


def main(s):
    """
    Given a variable s string of length five. Determine the number of digits 
    involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    n = 0
    if s[0].isdigit():
        n+=1
    else:
        0

    if s[1].isdigit():
        n+=1
    else:
        0

    if s[2].isdigit():
        n+=1
    else:
        0
    
    if s[3].isdigit():
        n+=1
    else:
        0
    
    if s[4].isdigit():
        n+=1
    else:
        0

    return n
print(main("32g4h8"))