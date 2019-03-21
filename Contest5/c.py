while True:
    try:
        inp = input().split('\t')
        print("{}{:.>73}".format(inp[0][0:7], inp[4]))
    except EOFError:
        break
