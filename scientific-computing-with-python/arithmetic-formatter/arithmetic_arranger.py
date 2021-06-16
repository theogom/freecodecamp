from typing import List


MAX_PROBLEMS = 5 # Maximum number of problems
MAX_DIGITS = 4 # Maximum number digits in each numbers of a problem
SEPCHAR = '-' # Separator character after the arithmetic expression

def merge_multilines(strings: List[str]):
    """
    Add multilines strings
    Each strings must have the same number of lines
    """
    height = strings[0].count('\n') + 1
    lines = [[] for _ in range(height)]

    for string in strings:
        string_pieces = string.split('\n')
        for i in range(height):
            lines[i].append(string_pieces[i])

    merged = '\n'.join(['    '.join(line) for line in lines])
    
    return merged


def arithmetic_arranger(problems: List[str], display_answer=False):
    """
    Arrange arithmetic problems in a vertical format
    """
    length = len(problems)
    if length > MAX_PROBLEMS:
        return 'Error: Too many problems.'

    arranged_problems = []

    for problem in problems:
        first, operator, second = problem.split()

        if not first.isnumeric() or not second.isnumeric():
            return 'Error: Numbers must only contain digits.'

        if operator not in ['+', '-']:
            return 'Error: Operator must be \'+\' or \'-\'.'
        
        # Find the max length of the two numbers
        length = max(len(first), len(second))
        if length > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Add left space padding for the numbers to be aligned
        first_line = f'{first:>{length + 2}}'
        second_line = f'{operator} {second:>{length}}'
        separator = SEPCHAR * (length + 2)

        if display_answer:
            answer = eval(f'{first} {operator} {second}')
            answer_line = f'{answer:>{length + 2}}'
            arranged_problem = '\n'.join((first_line, second_line, separator, answer_line))
        else:
            arranged_problem = '\n'.join((first_line, second_line, separator))

        arranged_problems.append(arranged_problem)

    return merge_multilines(arranged_problems)