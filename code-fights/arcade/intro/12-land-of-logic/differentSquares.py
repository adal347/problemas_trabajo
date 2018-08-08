def differentSquares(matrix):
    listing = set() 
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
                listing.add((matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]))
    return len(listing)
