#a frog wants to get to the other side of road
#From position X to position >= Y. It can jump on a len
#of D each time. Compute number of jumps required

#well, that's simple. We just compute distance and divide it
#by the jump len to get number of jumps needed. Then ceil round it
#(meaning that 2.1 transforms into 3) - since we can't have a fraction of jump


def solution(X, Y, D):
    distance = Y - X
    if distance>0:
        if distance % D == 0:
            return distance/D
        else:
            return (distance/D) + 1
    else:
        return 0
