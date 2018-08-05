def bishopAndPawn(bishop, pawn):

    bishop=[ord(bishop[0]), int(bishop[1])]
    pawn=[ord(pawn[0]), int(pawn[1])]

    return bishop[1] - bishop[0] == pawn[1] - pawn[0] or sum(bishop) == sum(pawn)
