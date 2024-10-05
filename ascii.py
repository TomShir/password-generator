run_condition=True
while run_condition:
  try:
    from colorama import Fore 
    import sys 
    import time 
    import random
    def color_random():
      color_txt=Fore.RED,Fore.CYAN,Fore.GREEN 
      print(random.choice(color_txt))

    color_random()
    msg=['Length','of','password',':']
    user=int(input('_'.join(msg)))
    if user<=4:
      error_msg='error that password is weak'
      print(Fore.RED)
      for txt in error_msg.upper():
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write(txt)
        sys.stdout.write('\n')
      print('Error:Your password exceeds 26 letters')
    elif user>=5:
      time.sleep(0.2)
      print('Ok... password strong')
      time.sleep(0.2)
      special_chars=str(input('Do you want special characters in your new password y/n:'))
      yes='y'
      no='n'
      if special_chars==yes:
        letters='abcdefghijklmnopqrstuwxyz'
        UPPER_CASE='ABCDEFGHIJKLMNOPQRSTUWXYZ'
        special_chars=['#','@']
        numerical_values=['1','2','3','4','5','6','7']
        sampled=random.sample(letters,user-len(random.sample(special_chars,2)))
        sampled_2=random.sample(UPPER_CASE,user-len(random.sample(special_chars,2)))
        ultimate_sampled=sampled,sampled_2
        print('Your new password:',''.join(random.choice(ultimate_sampled))+''.join(random.choice(special_chars)+''.join(random.choice(special_chars))))
        time.sleep(0.2)
        save_1=input('Do you want you save your newly acquired password?\ny/n:')
        if save_1==yes:
          with open('save.txt','a')as a:      a.write(str(''.join(random.choice(ultimate_sampled))+''.join(random.choice(special_chars)+''.join(random.choice(special_chars)))))
          time.sleep(0.2)
          a.write('\n')
        elif save_1==no:
          pass
      elif special_chars==no:
        letters2=random.sample('abcdefghijklmnopq_rstuwxyz0123456789ABCDEFGHIJKLMNO_PQRSTUWXYZ',user)
        print('Your new password,',''.join(letters2))
        save=input('Do you want to save your newly aquired password?\ny/n:')
        if save==yes:
          with open('save.txt','a')as ab:
            ab.write(''.join(letters2))
            time.sleep(0.2)
            ab.write('\n')

        elif save==no:
          pass
  except ValueError:
    pass
  except NameError:
    pass
