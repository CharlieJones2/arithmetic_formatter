import re


def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    first = ''
    second = ''
    lines = ''
    sumx = ''

    for problem in problems:

        first_num = problem.split(' ')[0]
        operator = problem.split(' ')[1]
        second_num = problem.split(' ')[2]

        if re.search('[^\s0-9+-]', problem):
            if operator.strip() == '/' or operator.strip() == '*':
                return 'Error: Operator must be \'+\' or \'-\'.'
            return 'Error: Numbers must only contain digits.'

        if len(first_num) >= 5 or len(second_num) >= 5:
            return 'Error: Numbers cannot be more than four digits.'

        result = ''
        if operator == '+':
            result = str(int(first_num) + int(second_num))
        elif operator == '-':
            result = str(int(first_num) - int(second_num))
        else:
            return 'Error: Operator must be \'+\' or \'-\'.'

        length = max(len(first_num), len(second_num)) + 2
        top = str(first_num).rjust(length)
        bottom = operator + str(second_num).rjust(length - 1)
        line = ''
        res = str(result).rjust(length)
        for s in range(length):
            line += '-'

        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumx += res

    if solve:
        string = first + '\n' + second + '\n' + lines + '\n' + sumx
        return string
    else:
        string = first + '\n' + second + '\n' + lines
        return string
