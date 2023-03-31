import unittest


def point_in_ngon(X, Y, T):
    X_arr = [float(i) for i in X.split()]
    X_arr.append(X_arr[0])
    X_arr.append(X_arr[1])
    Y_arr = [float(i) for i in Y.split()]
    Y_arr.append(Y_arr[0])
    Y_arr.append(Y_arr[1])
    cd = list(zip(X_arr, Y_arr))
    xt, yt = [float(i) for i in T.split()]
    for i, (x, y) in enumerate(cd):
        if i+3 <= len(cd):
            x1, y1 = cd[i+1][0], cd[i+1][1]
            x2, y2 = cd[i+2][0], cd[i+2][1]
            if x1 != x:
                k = (y1-y)/(x1-x)
                b = y-k*x
                if (y2-k*x2-b)*(yt-k*xt-b) > 0:
                    continue
                return (0)
            else:
                if (x2-x)*(xt-x) > 0:
                    continue
                return (0)
        else:
            return (1)


class Tests(unittest.TestCase):
    def test_1(self):
        X = " ".join(["-2", "2", "6"])
        Y = " ".join(["-2", "2", "-2"])
        self.assertEqual(point_in_ngon(X, Y, "2 -1"), 1)
        self.assertEqual(point_in_ngon(X, Y, "2 1"), 1)
        self.assertEqual(point_in_ngon(X, Y, "2 2"), 0)
        self.assertEqual(point_in_ngon(X, Y, "2 4"), 0)
        self.assertEqual(point_in_ngon(X, Y, "0 0"), 0)
        self.assertEqual(point_in_ngon(X, Y, "2 -3"), 0)

    def test_2(self):
        X = " ".join(["-2", "2", "2"])
        Y = " ".join(["-2", "2", "-2"])
        self.assertEqual(point_in_ngon(X, Y, "0 -3"), 0)
        self.assertEqual(point_in_ngon(X, Y, "0 1"), 0)
        self.assertEqual(point_in_ngon(X, Y, "4 0"), 0)
        self.assertEqual(point_in_ngon(X, Y, "1 0.5"), 1)
        self.assertEqual(point_in_ngon(X, Y, "1 -1"), 1)
        self.assertEqual(point_in_ngon(X, Y, "4 4"), 0)
        self.assertEqual(point_in_ngon(X, Y, "4 -2"), 0)


unittest.main()
