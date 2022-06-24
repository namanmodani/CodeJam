# Google Code Jam 2022
# d1000000: Submit Version
# Naman Modani

from collections import defaultdict
INF = 1e15

def solve():
  N = int(input())
  dice = [int(x) for x in input().split(' ')]
  dice.sort()

  count = 0
  for die in dice:
    if die > count:
      count += 1

  return count

def main():
  N = int(input())
  results = []

  for _ in range(N):
    results.append(solve())
  for i in range(len(results)):
    print(f'Case #{i+1}: {results[i]}')

main()