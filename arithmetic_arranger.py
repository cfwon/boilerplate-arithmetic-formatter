def arithmetic_arranger(problems):
    ################# Error Detect in Input Format #################

    # 1. Judge len(problem) > 5, then return Too many problem:
    if len(problems) > 5:
        return "Error: Too many problems."

    # Separate list
    first_line = []
    second_line = []
    third_line = []
    for problem in problems:
        first_line.append(problem.split(" ")[0])
        second_line.append(problem.split(" ")[1])
        third_line.append(problem.split(" ")[2])

    # 2. Judge operator is either '+' or '-':
    for opt in second_line:
        if opt not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

    # 3. Judge input number is number:
    num_list = first_line + third_line
    for num in num_list:
        if num.isnumeric() is False:
            return "Error: Numbers must only contain digits."
    # 4 Judge len(num) <= 4:
    for num in num_list:
        if len(num) > 4:
            return "Error: Numbers cannot be more than four digits."

    ################# Put in String #################
    # 1. Determine width for each problem, according to the 'dash' required
    max_num_int = []
    i = 0
    for num1 in first_line:
        num2 = third_line[i]
        max_num_int.append(max(int(num1), int(num2)))
        i += 1
    max_num_str = map(str, max_num_int)
    dash = []
    for i in max_num_str:
        dash.append(len(i) + 2)

    # Print element right-aligned depend on the len(dash), aka 'width'

    print(first_line)
    for i in range(0, len(first_line)):
        print(first_line[i].rjust(dash[i]), end="    ")
    print()
    for i in range(0, len(second_line)):
        print((second_line[i] + third_line[i]).rjust(dash[i]), end="    ")
        # print(third_line[i].rjust(dash[i]), end="")

    # print(second_line)
    # print(third_line)

    return True
