def parse(text):
    tokens = list(text)
    res = exp(tokens)
    return res


# def parse_number(number):
#     # Convert the number to an integer
#     return int(number)


def digit(tokens):
    """
    <digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    """
    if tokens[0] in '0123456789':
        value = int(tokens[0])
        tokens.pop(0)
    else:
        raise SyntaxError(f"Found {tokens[0]}")
    return value


def number(tokens):
    """
    <number> ::= <digit> { <digit> }
    """
    value = digit(tokens)
    while tokens:
        if tokens[0] in '0123456789':
            value = 10 * value + digit(tokens)
        else:
            break
    return value, tokens


def factor(tokens):
    """
    <factor> ::= <number> | ( <exp> )
    """
    if tokens[0] == '(':
        tokens.pop(0)
        value, tokens = exp(tokens)
        tokens.pop(0)
    else:
        value, tokens = number(tokens)
    return value, tokens


def term(tokens):
    """
    <term> ::= <factor> { <mulop> <factor> }
    """
    value, tokens = factor(tokens)
    while tokens:
        if tokens[0] == '*':
            tokens.pop(0)
            value *= factor(tokens)[0]
        elif tokens[0] == '/':
            tokens.pop(0)
            value /= factor(tokens)[0]
        else:
            break
    return value, tokens


def exp(tokens):
    """
    <exp> ::= <term> { <addop> <term> }
    """
    value, tokens = term(tokens)
    while tokens:
        if tokens[0] == '+':
            tokens.pop(0)
            value += term(tokens)[0]
        elif tokens[0] == '-':
            tokens.pop(0)
            value -= term(tokens)[0]
        else:
            break
    return value, tokens


print("Recursive descent parser - math expressions")
print(parse('1+2*3'))  # outputs: 7
print(parse('1*2+3'))  # outputs: 5
print(parse('1+2*3+4'))  # outputs: 11
print(parse('1+2*3+4*5'))  # outputs: 27
print(parse('(1+2)*(3+4)'))  # outputs: 21
print(parse('1+2*(3+4)'))  # outputs: 15
print(parse('1+2*(3+4)*5'))  # outputs: 71
