def pressureGauges(morning, evening):
    return list(zip(*[sorted(x) for x in list(zip(morning, evening))]))
