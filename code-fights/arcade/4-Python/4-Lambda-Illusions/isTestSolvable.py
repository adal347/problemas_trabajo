def isTestSolvable(ids, k):
    digitSum = lambda nid: sum(list(map(int, list(str(nid)))))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
