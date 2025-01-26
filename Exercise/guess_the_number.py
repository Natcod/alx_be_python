import random
secret_number = random.randint(1, 10)
guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it?"))

# if guess == secret_number:
#     print(f"You got it! My number was {secret_number}")
# if guess < secret_number:
#     print(f"Too low! My number was {secret_number}")
# if guess > secret_number:
#     print(f"Too high! My number was {secret_number}")

match secret_number:
   case _ if guess == secret_number:
        print(f"🎉 Congratulations! You guessed it! My number was {secret_number}.")
   case _ if guess < secret_number:
        print(f"😕 Too low! My number was {secret_number}.")
   case _ if guess > secret_number:
        print(f"😅 Too high! My number was {secret_number}.")   