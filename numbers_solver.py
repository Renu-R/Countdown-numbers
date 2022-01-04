operations = ['+', '-', '*', '/']

class Number:
    
    def __init__(self, num, steps):
        self.value = num
        self.steps = steps

    def getValue(self):
        return self.value

    def getSteps(self):
        return self.steps

    def calculate(self, rhs_Num, operator):
        rhs = rhs_Num.getValue()
        result = {
            '+': lambda rhs: self.value + rhs,
            '-': lambda rhs: self.value - rhs,
            '*': lambda rhs: self.value * rhs,
            '/': lambda rhs: self.value / rhs,
        }[operator](rhs)

        if result <1 or not (result - int(result))==0:
            return None
        else:
            if not rhs_Num.getSteps() == '' and not self.steps =='':
                steps = '('+ self.steps+')' + operator +'(' + rhs_Num.getSteps() + ')' 
            elif not rhs_Num.getSteps() == '':
                steps = str(self.value) + operator +'(' + rhs_Num.getSteps() + ')'
            elif not self.steps =='':
                steps = '('+ self.steps+')' + operator + str(rhs_Num.getValue())
            else:
                steps = str(self.value) + operator  + str(rhs_Num.getValue())

            v = Number(result, steps)
            return v


def getNums(nums):
    numbers = []
    for num in nums:
        numbers.append(Number(num, ''))
    return numbers


def solve(target, numbers):
    for num1 in numbers:
        remaining = numbers.copy()
        remaining.remove(num1)
        for num2 in remaining:
            for operator in operations:
                result = num1.calculate(num2, operator)

                if result == None:
                    continue
                if result.getValue() == target:
                    return result.getSteps()

                if len(numbers) > 2:
                    updated_nums = numbers.copy()
                    updated_nums.remove(num1)
                    updated_nums.remove(num2)
                    updated_nums.append(result)
                    result = solve(target, updated_nums)
                    if not result == None:
                        return result
    return None

def getSolution(target, nums):
    numbers = getNums(nums)
    solution = solve(target, numbers)
    return(str(target) + ' = ' + solution)


