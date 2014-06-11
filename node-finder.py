#You need to supply your own worldpath.  Mine is listed here as an example
#Should point to the folder that contains the level.dat
#WORLDPATH = r"C:\Users\rob\AppData\Roaming\.technic\modpacks\luddite-5-magicpack\saves\Test"
WORLDPATH = r"C:\Path\to\level\here"

import pymclevel
import sys
import os

try:
  world = pymclevel.mclevel.fromFile(WORLDPATH)
except IOError:
  sys.exit("IO error, check the world path")

#World should be loaded now.

chunks = list(world.allChunks)

if len(chunks) == 0:
  sys.exit("No chunks loaded?!")
print len(chunks), "chunks loaded"

print "Locating nodes:"

for (xc,zc) in chunks:
  chunk = world.getChunk(xc,zc)
  for entity in chunk.TileEntities:
    if entity["id"].value == "TileNode":
      print("x: %d y: %d z: %d") % (entity["x"].value, entity["y"].value, entity["z"].value)
      
input("Press Enter to exit...")