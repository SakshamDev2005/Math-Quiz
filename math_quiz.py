import random as r

class Math_Quiz:
    def __init__(self):

        print('Welcome to Math Quiz')
        print('\nEach Level contains 10 Ques')
        print('Answer the following sums and Level shows no of digits')

        while True:
            self.Game()

            print('\n')
            ch = input('Do you want to play game again? ->')
            if ch.upper() not in ['Y', 'YES']:
                break

    def Lvl(self):
      if self.v == 1:
        return r.randint(0, 9)

      elif self.v == 2:
        return r.randint(10, 99)

      elif self.v == 3:
        return r.randint(100, 999)


    def Game(self):
      self.s = 0

      print('\n1 - 1 Digit \n2 - 2 Digit \n3 - 3 Digit')
      print('\n')
      self.v = int(input('Select The Level ->'))

      if self.v > 3 or self.v == 0:
        print('\n')
        print('Error')
        self.Game()

      for i in range(10):
          x = self.Lvl()
          y = self.Lvl()
          t = x + y

          print(f'{x} + {y}')
          ans = int(input('Enter the Answer ->'))

          if ans == t:
              print('Correct Answer')
              self.s += 1
          else:
              print('Incorrect \nCorrect Answer is', t)

      print('\nYour Score is ', self.s)
      print('Your Score(in %) is', self.s * 10, '%')



if __name__ == '__main__':
    Math_Quiz()
