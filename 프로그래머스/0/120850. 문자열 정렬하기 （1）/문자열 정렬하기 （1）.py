def solution(my_string):
    answer = []
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in my_string:
        if i in num:
            answer.append(int(i))
    return sorted(answer)