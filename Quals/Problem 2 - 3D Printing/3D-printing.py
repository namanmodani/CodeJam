# Google Code Jam 2022
# 3D Printing
# Naman Modani

from collections import defaultdict
INF = 10e15

def minimum(color, printers):
  mn = INF
  for printer in printers:
    mn = min(mn, printer[color])
  return mn

def solve():
  printers = []

  for _ in range(3):
    printers.append([int(x) for x in input().split(' ')])

  res = []
  remainder = int(1e6)

  for color in range(4):
    if remainder == 0:
      res.append(0)
      continue

    taken = minimum(color, printers)

    if remainder - taken < 0:
      taken = remainder
    remainder -= taken
    res.append(taken)

  if (remainder > 0):
    return 'IMPOSSIBLE'

  return " ".join([str(x) for x in res])

def main():
  N = int(input())
  result = []

  for _ in range(N):
    result.append(solve())

  for i in range(len(result)):
    print(f'Case #{i+1}: {result[i]}')

main()
