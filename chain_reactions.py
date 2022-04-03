# Google CodeJam 2022
# Chain Reactions
# Naman Modani

from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

def dfs(curr, path):
  path.append(curr)
  
  if curr not in invNeighborMap:
    global paths
    
    paths.append(path)
    return
  
  for neighbor in invNeighborMap[curr]:
    dfs(neighbor, path.copy())