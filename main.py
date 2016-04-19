from display import *
from draw import *
from parser  import *
from matrix import *
import sys

screen = new_screen()
color = [ 255, 255, 100 ]
edges = []
imat = new_matrix()
ident(imat)
stack = [imat]
#print stack

if len(sys.argv) == 2:
    f = open(sys.argv[1])

parse_file( f, edges, stack, screen, color )
f.close()
