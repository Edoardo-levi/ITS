def proDict()-> dict:
    d={}
    for x in range( 0,101):
        for y in range (2,89,2):
            d[(x,y)]=x*y
    return d


if __name__ == "__main__":
    d=proDict()

    x1, y1 = 13, 88
    x2, y2 = 83, 56
    x3, y3 = 71, 44



    print(f"d[(13, 88)] = {d[(x1, y1)]}")
    print(f"d[(83, 56)] = {d[(x2, y2)]}")
    print(f"d[(71, 44)] = {d[(x3, y3)]}")