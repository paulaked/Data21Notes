  
class Fizzbuzz:

    def __init__(self, start_of_range, end_of_range):
        self.fizzrange = range(start_of_range, end_of_range)
        self.fizzbuzz_list = []
        self._fizzbuzz_iterator()

    def print_something(self):
      return "hello"
        
    def _divisible_by(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    def _fizzbuzz_iterator(self):

        for num in self.fizzrange:
            if self._divisible_by(num, 15):
                self.fizzbuzz_list.append("fizzbuzz")
            elif self._divisible_by(num, 5):
                self.fizzbuzz_list.append("sdfghfsdghfz")
            elif self._divisible_by(num, 3):
                self.fizzbuzz_list.append("f45645645zz")
            else:
                self.fizzbuzz_list.append(num)
