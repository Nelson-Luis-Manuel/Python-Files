def drawSquare(size):
    i = 1
    while i <= size:

        if i == 1 or i == size:
            print('* '*size)
        else:
            k = 1
            rw = []
            while k <= size:
                if k == 1 or k == size:
                    rw.append('*')
                else:
                    rw.append(' ')
                k = k+1
            print(' '.join(rw))
        i = i+1

drawSquare(5)