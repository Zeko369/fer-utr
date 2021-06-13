class Main:
    index = 0
    out = ''

    def __init__(self, s: str):
        self.s = s

    def run(self):
        return self.run_s() and self.index == len(self.s)

    def get_curr(self):
        if self.index >= len(self.s):
            return None

        tmp = self.s[self.index]
        self.index += 1
        return tmp

    def run_s(self):
        self.out += 'S'
        curr = self.get_curr()

        if curr == 'a':
            return self.run_a() and self.run_b()
        elif curr == 'b':
            return self.run_b() and self.run_a()
        else:
            self.index -= 1
            return False

    def run_a(self):
        self.out += 'A'
        curr = self.get_curr()

        if curr == 'a':
            return True
        elif curr == 'b':
            return self.run_c()
        else:
            self.index -= 1
            return False

    def run_b(self):
        self.out += 'B'

        if self.index == len(self.s):
            return True

        if self.get_curr() != 'c':
            self.index -= 1
            return True

        if self.get_curr() != 'c':
            self.index -= 2
            return True

        if not self.run_s():
            self.index -= 3
            return True

        if self.get_curr() != 'b':
            self.index -= 4
            return True

        if self.get_curr() != 'c':
            self.index -= 5

        return True

    def run_c(self):
        self.out += 'C'
        return self.run_a() and self.run_a()


if __name__ == '__main__':
    runner = Main(input())
    if runner.run():
        res = 'DA'
    else:
        res = 'NE'

    print(runner.out)
    print(res)
