def reverter(palavra):
  inversa = []
  for letra in palavra:
    inversa.app(letra)
  return inversa

if __name__ == "__main__":
  palavra = "daniel"
  print(reverter(palavra))