# import random

# def guess(x):
#   random_number = random.randint(1, x)
#   guess = 0

#   while guess != random_number:
#     guess = int(input(f'Adivinhe um número entre 1 e {x}: '))

#     if guess < random_number:
#       print('Desculpe, adivinhe novamente. Muito baixo.')
#     elif guess > random_number:
#       print('Desculpe, adivinhe novamente. Muito alto.')

#   print(f"Sim, parabéns. Você adivinhou o número {random_number} corretamente !!")

# guess(10)

import random

def guess(x):
  random_number = random.randint(1, x)
  guess = None
  attempt = 0
  attempts_list = []

  while guess != random_number:
    try:
      guess = int(input(f'Adivinhe um número entre 1 e {x} (ou digite "0" para desistir): '))
      if guess == 0:
        print("Desistindo... O número era", random_number)
        return
      if guess < 1 or guess > x:
        raise ValueError
    except ValueError:
      print(f'Desculpe, você deve inserir um número entre 1 e {x}.')
      continue

    attempts_list.append(guess)
    attempt += 1

    if guess < random_number:
      print('Desculpe, adivinhe novamente. Muito baixo.')
    elif guess > random_number:
      print('Desculpe, adivinhe novamente. Muito alto.')

  print(f"Sim, parabéns! Você adivinhou o número {random_number} corretamente em {attempt} tentativas!!")
  print(f'Histórico de tentativas: {attempts_list}')

guess(10)