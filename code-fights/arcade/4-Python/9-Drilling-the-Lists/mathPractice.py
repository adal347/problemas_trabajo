def mathPractice(numbers):
    return functools.reduce(lambda acc,x: (acc+x[1] if x[0]%2 else acc*x[1]),
                  enumerate(numbers), 1)
