class Search(object):
    def __init__(self):
        pass
    def linear_Search(self,A, N, X):
        for i in range(N):
            count = 0
            for j in range(X):
                index = i+j
                if (index > N-1):
                    break
                if (A[index] == -1):
                    count += 1

            if (count == X):
                return i
            i = j
        return -1


    def direct_search(self, A, N, X, POS):
        if (POS[X-1] != -1):
            return POS[X-1]
        else:
            return -1

