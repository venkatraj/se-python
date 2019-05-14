def pascalTriangle(n):
    pt = [[None for _ in range(row+1)] for row in range(n)]
    print(pt)
    row = 0
    while row < n:
        pt[row][0] = 1
        column = 1
        while column < row:
            pt[row][column] = pt[row-1][column-1] + pt[row-1][column]
            column += 1
        pt[row][row] = 1
        row += 1

    # for i in pt:
    #     row = ''
    #     for j in i:
    #         row += str(j)
    #     print(row.center())
    print(pt)



def main():
    pascalTriangle(5)


if __name__ == '__main__':
    main()
