class Interpolations:

    class Point:
        def __init__(self, x, y):
            self.x = float(x)
            self.y = float(y)

    Points: list[Point] = []
    
    def __init__(self, points: list[tuple]):
        for point in points:
            self.Points.append(self.Point(point[0], point[1]))
        self.N = len(self.Points) - 1

    def lagrange(self):
        print(self.N)
        PN = ""
        for i in range(0, self.N + 1):

            num = ""
            den = ""
            for j in range(0, self.N + 1):
                if j != i:
                    num += f"(x-{self.Points[j].x})"
                    den += f"({self.Points[i].x - self.Points[j].x})"
                    if i == self.N:
                        if j != self.N - 1:
                            num += "*"
                            den += "*"                    
                    elif j != self.N:
                            num += "*"
                            den += "*"
                    
                
            PN += f"{self.Points[i].y}*{num}/{eval(den)}"
            if i != self.N:
                PN += "+"

        return PN # P_N(x)

    def cubic_spline(self):
        pass

    def test(self):
        print(self.Points[0].x)

abc = Interpolations([(1,2),(2,3),(4,2)])
print(abc.lagrange())