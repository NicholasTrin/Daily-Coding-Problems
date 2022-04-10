def step_possiblities(steps,step_sizes)->int:
    unique_possibilities = 0
    unique_possibilities += helper(steps,step_sizes)
    return unique_possibilities

def helper(steps, step_sizes)->int:
    count = 0
    for curr_step_size in step_sizes:
        if steps - curr_step_size == 0:
            count += 1
        elif steps - curr_step_size > 0:
            count += helper(steps-curr_step_size, step_sizes)
    return count

if __name__ == '__main__':
    print(step_possiblities(5, [1,2]))
    print(step_possiblities(4, [1,3,5]))