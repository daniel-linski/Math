import random

play_again = "yes"
play_count = 0
play_score = []
while play_again == "yes":
  a = random.randrange(1,101)
  print(a)
  guess = ""
  j = 1
  while guess != a:
    guess = input("The number is between 1 and 100. What is your guess #" + str(j) + "? ")
    if guess.isdigit() == False:
      print("Please type a number.")
      j -= 1
    elif int(guess) < a:
      print("It's bigger than " + str(guess))
    elif int(guess) > a:
      print("It's smaller than " + str(guess))
    else:
      if j == 1:
        print("Wow! It's " + str(a) + " indeed. You guessed it in only " + str(1) + " attempt! Congratulations!")
      elif j < 6:
        print("Great! It's " + str(a) + " indeed. You guessed it in " + str(j) + " attempts! Nice!")
      elif j < 11:
        print("Okay! It's " + str(a) + " indeed. You guessed it in an unfortunate " + str(j) + " attempts. Better luck next time!")
      else:
        print("Finally! It's " + str(a) + " indeed. You guessed it in a miserable " + str(j) + " attempts. Unfortunate.")
      play_count += 1
      guess = int(guess)
      play_score.append(j)
      j = 0
      play_again = input("Would you like to play again? (yes/no) ")
      
    j += 1
  
if (sum(play_score) / len(play_score)) <=5:
  average = "This is your lucky day!"
else:
  average = "You suck! Try again."
if play_count >= 3:
  print("You played " + str(play_count) + " games. Thank you for playing! Here are your scores: " + ", ".join(map(str, play_score)) + ". Here is your average number of attempts: " + (sum(play_score) / len(play_score)) + ". " + str(average))
else:
  exit(print("Thank you for playing!"))
  
# part 1
# generate number $a from 1 to 101; do not print it
# organize a guessing game, by using input() function, where you prompt user to enter number from 1 to 101, # and script telsl user whether it's bigger or smaller than $a.
# use this: 
# guess = int(input("The number is between 1 and 100. Your guess #" + str(j) + ">"))
# where j is the amount of guesses so far + 1
# print "It's smaller than " + str(guess)" or "It's bigger than " + str(guess)"
# if you guessed it right, print "Great! It's " + str(a) +" indeed. You guessed it right with only " + str(j) + " attempts" - if number of attempts were less than 6
# print "Well finally! It's " + str(a) +" indeed. You guessed it right with miserable " + str(j) + " attempts" - if number of attempts were more than 5

# part 2
# run this game 3 times, and then print the statistics
# print "Statistics:"
# print "Number of guesses: " + "j1, j2, j3"
# print "Average number of attempts per game: " + str(j)
# if average is more than 6, print "You suck at this!" 
# if average is less than 6, print "You are lucky today" 