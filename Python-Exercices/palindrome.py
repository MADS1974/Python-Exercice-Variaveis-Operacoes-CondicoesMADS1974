# -*- coding: utf-8 -*-
"""Palindrome

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19PRk4S8kCnYqo7icxnVV-VMkP7xFInEU
"""

#escreva uma função para testar se uma palavra do usuário é um palíndromo. 
#As declarações de função são fornecidas para você."""

def isPalindrome(str):
  str = str.lower()
  if (str == str[::-1]):
    return True
  else:
    return False


# Solicitar ao usuário que introduza a sentença
def main():
  userInput = input("Enter a WORD to be tested as a palindrome:")

  if (isPalindrome(userInput)):
    print(userInput + " is a palindrome!")
  else:
    print(userInput + " is NOT a palindrome!")
    
if __name__ == "__main__":
    main()