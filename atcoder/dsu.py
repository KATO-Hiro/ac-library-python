import typing


class DSU:
    '''
    Implement (union by size) + (path compression)
    Reference:
    Zvi Galil and Giuseppe F. Italiano,
    Data structures and algorithms for disjoint set union problems
    '''

    def __init__(self, n: int = 0):
        self._n = n
        self._parent_or_size = [-1] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self._parent_or_size[x] < -self._parent_or_size[y]:
            x, y = y, x

        self._parent_or_size[x] += self._parent_or_size[y]
        self._parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n

        if self._parent_or_size[a] < 0:
            return a

        self._parent_or_size[a] = self.leader(self._parent_or_size[a])
        return self._parent_or_size[a]

    def size(self, a: int) -> int:
        assert 0 <= a < self._n

        return -self._parent_or_size[self.leader(a)]

    def groups(self) -> typing.List[typing.List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))


# https://atcoder.jp/contests/practice2/tasks/practice2_a
def main() -> None:
    import sys

    n, q = map(int, sys.stdin.readline().split())
    dsu = DSU(n)

    for _ in range(q):
        t, u, v = map(int, sys.stdin.readline().split())
        if t == 0:
            dsu.merge(u, v)
        if t == 1:
            if dsu.same(u, v):
                print(1)
            else:
                print(0)


if __name__ == '__main__':
    main()
