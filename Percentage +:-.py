print()
print()

while True:
   old = input(f'Old Integer > ')
   new = input(f'New Integer > ')

   try:
      val = int(old)
      try:
         val = int(new)
         
         old = int(old)
         new = int(new)
         
         if old == new:
            print('Answer : ', 'Unchanged')
            print()
         else:
            tmp = new - old
            fin = tmp / old * 100
            if fin > 0:
               print('Answer : ', 'Increase by', fin, '%')
               print()
            else:
               fin = fin * -1
               print('Answer : ', 'Decrease by', fin, '%')
               print()

      except ValueError:
         print("Ensure the input is numeric.")
   except ValueError:
      print("Ensure the input is nemeric.")


