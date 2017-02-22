class MuffledCalculator():
    muffed = False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError as e:
            if self.muffed:
                print(e)
            else:
                raise
