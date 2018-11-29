def checkParticipants(participants):
    return [i[0] for i in enumerate(participants) if i[0]>i[1]]
