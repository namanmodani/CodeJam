# Google CodeJam 2022
# Chain Reactions
# Naman Modani

from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 8)

def dfs(curr, path):
  path.append(curr)
  
  if curr not in invNeighborMap:
    global paths
    
    paths.append(path)
    return
  
  for neighbor in invNeighborMap[curr]:
    dfs(neighbor, path.copy())

def handle(root):
  res = 0
  global paths, triggered
  paths = []
  
  if root not in invNeighborMap:
    return funFactors[root - 1]
  
  for pointing in invNeighborMap[root]:
    dfs(pointing, [root])

  maximums = []
  
  for path in paths:
    funFactorPath = [funFactors[p - 1] for p in path]
    funFactorPath.sort(reverse = True)
    maximums.append((funFactorPath, path))
    
  maximums.sort(key = lambda x: x[0])
  
  for mx, path in maximums:
    notTriggeredPath = []
    for node in path:
      if node not in triggered:
        notTriggeredPath.append(node)
        triggered.add(node)
    
    pathMax = max([funFactors[p - 1] for p in notTriggeredPath])
    res += pathMax
  
  return res
  
def solve():
  global neighborMap, invNeighborMap, roots, triggered, funFactors
  neighborMap = {}
  invNeighborMap = defaultdict(list)
  triggered = set()
  roots = []
  
  N = int(input())
  funFactors = [int(x) for x in input().split()]
  neighbors = [int(x) for x in input().split()]  
  
  for i in range(len(neighbors)):
    neighborMap[i + 1] = neighbors[i]
    invNeighborMap[neighbors[i]].append(i + 1)
    if (neighbors[i] == 0):
      roots.append(i + 1)

  final = 0
  for root in roots: 
    final += handle(root)
  
  return final
  
def main():
  N = int(input())

  results = []
  
  for _ in range(N):
    results.append(solve())
    
  for i in range(len(results)):
    print(f'Case #{i+1}: {results[i]}')
    
main()