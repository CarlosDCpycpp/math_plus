import math


# this doesn't r work

class Term:
    def __init__(self, term_: str):
        self.term_ = term_
        self.parts = list(term_.split())
        self.num_tot = None
        self.lit_tot = None

        self.parts_lit_ = []
        self.parts_num_ = []

        for part in self.parts:
            if 'x' in part:
                if part == 'x':
                    part = '1*x'
                self.parts_lit_.append(part)
            else:
                self.parts_num_.append(part)

        self.num_tot_ = "".join(self.parts_num_)
        if self.num_tot_ == "":
            self.num_tot_ = "0"
        self.num_tot = eval(self.num_tot_)

        self.lit_tot_ = ""
        for part in self.parts_lit_:
            if '**' in part:
                power = int(part.split('**')[-1])
                base_coeff = part.split('*')[0]
                if base_coeff == 'x':
                    base_coeff = '1'
                self.lit_tot_ += f"({base_coeff}*x**{power})"
            else:
                self.lit_tot_ += part
        if self.lit_tot_ == "":
            self.lit_tot_ = "0"
        self.lit_tot = eval(self.lit_tot_)


class Equation:
    def __init__(self, equation_):
        self.equation = equation_

        self.term1_, self.term2_ = self.equation.split("=")
        self.term1 = Term(self.term1_)
        self.term2 = Term(self.term2_)

        self.num = self.term1.num_tot - self.term2.num_tot
        self.lit = self.term1.lit_tot - self.term2.lit_tot

        if '**' not in equation_:
            self.result = self.num / self.lit
        else:
            a = self.lit
            b = self.num
            c = 0

            discriminant = b ** 2 - 4 * a * c
            if discriminant < 0:
                self.result = "No real solution"
            else:
                self.result = [
                    (-b + math.sqrt(discriminant)) / (2 * a),
                    (-b - math.sqrt(discriminant)) / (2 * a)
                ]

    def __str__(self):
        if isinstance(self.result, list):
            return f"x = {self.result[0]} or x = {self.result[1]}"
        return f"x = {self.result}"

    def __float__(self):
        if not isinstance(self.result, (list, str)):
            return float(self.result)
        else:
            return None


def solve(equation: str):
    """Solves the equation that is given as an argument (as a string).
    WARNING:
        It's limited to one variable that is necessarily "x" and to two terms"""
    return float(Equation(equation))


if __name__ == "__main__":
    print(float(Equation("3 = x**2 +15 -173")))
