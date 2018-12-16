def mergingVines(vines, n):
    def nTimes(n):
        def func_decor(func):
            def func_wrapper(vines):
                for _ in range(n):
                    vines = func(vines)
                return vines
            return func_wrapper
        return func_decor

    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res

    return sumOnce(vines)
