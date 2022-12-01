from some_functions import *

def solve_it(variable):

    variables = variable.split("+")

    n = len(variables[0])-1


    def find_same_positions(variables):
        l = []
        l2 = []
        for i in range(len(variables)):
            for j in range(len(variables)):
                for k in range(len(variables[0])):
                    if variables[i] != variables[j]:
                        if variables[i][k] == variables[j][k] and variables[i][k] != "-":
                            my_list = [f'{k}', variables[i], variables[j]]
                            not_my_list = my_list.copy()
                            my_list.sort()
                            not_my_list2 = my_list.copy()
                            # print(my_list, not_my_list)
                            if my_list not in l2:
                                l2.append(my_list)
                                if not_my_list not in l:
                                    l.append(not_my_list)
        return l

    def start_of_first_step(same, solve1, n):
        for i in range(len(same)):
            a = []
            a.append([same[i][1], same[i][2]])
            for j in range(len(same)):
                if same[i][1] == same[j][1] and same[i][2] == same[j][2]:
                    a.append(same[i][0])
            # a.remove(a[1])
            if len(a) > n:
                solve1.append(a)
            # else:
            #     solve2.append(a)

    def remove_duplicates(solve1):
        new_solve1 = []
        for i in range(len(solve1)):
            new = []
            [new.append(x) for x in solve1[i] if x not in new]
            new_solve1.append(new)
        return new_solve1

    # print(new_solve1)

    def divide_to_continue(new_solve1, n):
        # n = len(variables[0])-1
        nnew_solve1 = []
        for i in range(0, len(new_solve1), n):
            nnew_solve1.append(new_solve1[i:i+n])
        return nnew_solve1


    def end_of_first_step(nnew_solve1):
        answer = []
        for i in nnew_solve1:
            indexes = []
            for j in i:
                indexes.append(j[1])
            answer.append([i[0][0], indexes])
        return answer


    #0001 0100 0101 1000 1010 1100 1110

    def very_end_of_1st_step(answer):
        end = []
        for i in answer:
            result = ''
            n = len(i[0][0])
            indexes = i[1]
            ind = []
            for k in indexes:
                h = int(k)
                if h not in ind:
                    ind.append(h)

            for j in range(n):
                if j in ind:
                    result+=i[0][0][j]
                else:
                    result+="-"
            end.append(result)
        return end


    def my_first_step(var):
        same = find_same_positions(var)
        solve1 = []
        start_of_first_step(same, solve1, n)
        new_solve1 = remove_duplicates(solve1)
        nnew_solve1 = divide_to_continue(new_solve1, n)
        answer = end_of_first_step(nnew_solve1)
        end = very_end_of_1st_step(answer)
        return end
    g = my_first_step(variables)
    print(g)
    f = g

    if len(g)>4:
        def my_second_step(g):
            start = find_same_positions(g)
            solve1 = []
            start_of_first_step(start, solve1, n-1)
            new_solve1 = remove_duplicates(solve1)
            nnew_solve1 = divide_to_continue(new_solve1, n-1)
            answer = end_of_first_step(nnew_solve1)
            result = very_end_of_1st_step(answer)
            return result
        # #0001+0100+0101+1000+1010+1100+1110
        close = my_second_step(g)
        f = close

    print(f)

    def most_frequent(List):
        counter = 0
        num = 0
        for i in List:
            curr_frequency = List.count(i)
            if (curr_frequency > counter):
                counter = curr_frequency
                num=i
        return num
    m = most_frequent(f)
    # print(m)
    answer = []
    answer.append(m)
    if m != 0:
        def pre_last_step(g, m):
            h = []
            for i in range(len(m)):
                if m[i] != "-":
                    h.append([i, m[i]])

            for i in g:
                b = True
                for j in range(len(i)):
                    for k in range(len(h)):
                        if j == h[k][0] and i[j] == h[k][1]:
                            b = False
                if b:
                    answer.append(i)

            return answer

        answer = pre_last_step(g, m)
    else:
        answer = f
    print(answer)
    final_answer = numbers_to_circuit(answer)
    return [g, f, set(final_answer)]

# print(final_answer)

# var = input()
# print(solve_it(var))

