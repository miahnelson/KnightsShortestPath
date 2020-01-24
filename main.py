knightmoves = [(2, 1), (2, -1), (1, 2), (1, -2),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]


def makeGameBoard(n):
    """ 
    Create a gameboard represented as a dictionary. 

    Game board consistis of numeric placeholders starting 
    with zero and going to the last number stipulated
    -------------------------
    | 0| 1| 2| 3| 4| 5| 6| 7|
    -------------------------
    | 8| 9|10|11|12|13|14|15|
    -------------------------
    |16|17|18|19|20|21|22|23|
    -------------------------
    |24|25|26|27|28|29|30|31|
    -------------------------
    |32|33|34|35|36|37|38|39|
    -------------------------
    |40|41|42|43|44|45|46|47|
    -------------------------
    |48|49|50|51|52|53|54|55|
    -------------------------
    |56|57|58|59|60|61|62|63|
    -------------------------

    Parameters: 
    n (int): number of last gameboard cell 

    Returns: 
    dict(): Dictionary with key values representing game 
    board cells, values representing visited or not

    """
    gameBoard = {}
    for i in range(0, n + 1):
        gameBoard[i] = None
    return gameBoard


def validator(coord):
    """ 
    Coordinate validator. 

    Used to ensure that coordnates of move are within the gameboard boundaries

    Parameters: 
    tuple: (x, y)

    Returns: 
    boolean: Within boundaries True or False

    """
    for x in coord:
        if x not in range(0, 8):
            return False
            break
    return True


def solution(source, destination):
    """ 
    Identifies shortest distance a knight would have to move between two points of a chess board. 

    Accepts a source cell number and a destination cell number

    Parameters: 
    source: int
    destination: int

    Returns: 
    int: Shortest number of levels traversed to get from source to destination

    """
    def coordToPosition(x): return x[0]*8+x[1]
    gameBoard = makeGameBoard(63)
    gameBoard[source] = 0
    queue = []
    queue2 = []
    counter = 0
    queue.append(source)
    visited = str()
    while len(queue) > 0:
        counter += 1
        for q in queue:
            oldCoord = divmod(q, 8)
            for moves in knightmoves:
                newCoord = (oldCoord[0] + moves[0], oldCoord[1] + moves[1])
                visited = coordToPosition(newCoord)
                if validator(newCoord) == True and gameBoard[visited] == None:
                    gameBoard[visited] = counter
                    queue2.append(visited)
        queue = queue2
        queue2 = []

    return(gameBoard[destination])


if __name__ == "__main__":
    print(solution(0, 1) == 3)
    print(solution(19, 36) == 1)
