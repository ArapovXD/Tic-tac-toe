
class field:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.field = [[j if ((i == 0) and (j != 0 and j != self.x + 1)) else "#" for j in range(self.x + 1)] for i in range(self.y + 1)]
        for i in range(1, self.y + 1):
            self.field[i][0] = i
        self.field[0][0] = " "

        self.to_win = int(min(self.x, self.y) * 0.6) 



    def show_field(self):

        print("\n" * 50)
        for i in range(self.y + 1):
            print(*self.field[i])
        print("Need to win: " + str(self.to_win))



    def change_map(self, yc, xc, flag):

        try:
            if self.field[yc][xc] == "#":
                if flag:
                    self.field[yc][xc] = "X"
                else:
                    self.field[yc][xc] = "O"
        except:
            return 0

        return 1



    def check_for_row(self, yc, xc, flag):

        if self.horizon_check(yc, xc): return 1
        if self.vertical_check(yc, xc): return 1
        if self.main_diagonal_check(yc, xc): return 1
        if self.another_diagonal_check(yc, xc): return 1

        return 0



    def horizon_check(self, yy, xx):

        count = 0
        for i in range(1, x + 1):
            if (flag == 1):
                if self.field[yy][i] != "X":
                    if count < self.to_win:
                        count = 0
                else:
                    count += 1
            else:
                if self.field[yy][i] != "O":
                    if (count < self.to_win):
                        count = 0
                else:
                    count += 1

        if (count >= self.to_win): return 1
        else: return 0



    def vertical_check(self, yy, xx):

        count = 0
        for i in range(1, y + 1):
            if (flag == 1):
                if self.field[i][xx] != "X":
                    if count < self.to_win:
                        count = 0
                else:
                    count += 1
            else:
                if self.field[i][xx] != "O":
                    if (count < self.to_win):
                        count = 0
                else:
                    count += 1

        if (count >= self.to_win): return 1
        else: return 0



    def main_diagonal_check(self, yy, xx):

        if min(yy, xx) == yy:
            xx -= (yy - 1)
            yy = 1
        else:
            yy -= (xx - 1)
            xx = 1

        count = 0
        while (xx <= x and yy <= y):
            if (flag == 1):
                if self.field[yy][xx] != "X":
                    if count < self.to_win:
                        count = 0
                else:
                    count += 1
            else:
                if self.field[yy][xx] != "O":
                    if (count < self.to_win):
                        count = 0
                else:
                    count += 1
            yy += 1
            xx += 1

        if (count >= self.to_win): return 1
        else: return 0



    def another_diagonal_check(self, yy, xx):

        if min(x - xx + 1, yy) == yy:
            xx += (yy - 1)
            yy = 1
        else:
            xx = 1
            yy += (xx - 1)

        count = 0
        while (xx >= 1 and yy >= 1 and yy <= y):
            if (flag == 1):
                if self.field[yy][xx] != "X":
                    if count < self.to_win:
                        count = 0
                else:
                    count += 1
            else:
                print(yy, xx)
                if self.field[yy][xx] != "O":
                    if (count < self.to_win):
                        count = 0
                else:
                    count += 1
            yy += 1
            xx -= 1

        if (count >= self.to_win): return 1
        else: return 0



    def is_gap_exist(self):

        for row in self.field:
            for gap in row:
                if gap == "#":
                    return 1

        return 0


print("Enter 2 numbers: 1 - rows, 2 - columns",)
y, x = list(map(int, input().split()))
flag = False
ex = field(x, y)

# Gameplay
while True:
    ex.show_field()

    print("Player's " + str(int(flag) + 1) + " step: ", end="")
    yc, xc = list(map(int, input().split()))

    changed = ex.change_map(yc, xc, flag)
    res = 0
    if changed: res = ex.check_for_row(yc, xc, flag)

    if res:
        ex.show_field()
        print("Player " + str(int(flag) + 1) + " win!")
        break

    elif not ex.is_gap_exist():
        print("Game over! No more gaps.")
        break

    flag = (flag + 1) % 2