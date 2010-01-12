import time
import sys

# (0, 0)
#         (W-1, H-1)
def get_point(value, maze, w, h):
	#print [ (maze[y][x], (x, y)) for x in range(w) for y in range(h) ]
	return filter(lambda h: h[0]==value, [ (maze[y][x], (x, y)) for x in range(w) for y in range(h) ])[0][1]

def make_potential_map(maze, w, h, start, goal):
	potential = [ [9999]*w for y in range(h) ]
	mark = [ [ maze[y][x] for x in range(w) ] for y in range(h) ]
	def push_next(x, y, v):
		if mark[y][x] != "*" and mark[y][x] != ".":
			q.append( ((x, y), v+1))
			mark[y][x] = "."
	q = []
	push_next(start[0], start[1], -1)
	while len(q)>0:
		((x, y), v) = q.pop(0)
		potential[y][x] = v
		if (x, y)==goal: break
		push_next(x, y-1, v)
		push_next(x-1, y, v)
		push_next(x, y+1, v)
		push_next(x+1, y, v)
		#time.sleep(0.5)
		#print q
	#print "potential map"
	#print "\n".join([ " ".join(["%4d"%x for x in line]) for line in potential])
	return potential

def draw_one_path(maze, potential, w, h, start, goal):
	pos = goal
	result = [ [ maze[y][x] for x in range(w) ] for y in range(h) ]
	for i in range(potential[goal[1]][goal[0]]-1, 0, -1):
		pos = filter(lambda h: h[0]==i, [ (potential[p[1]][p[0]], p) for p in [ (dp[0]+pos[0], dp[1]+pos[1]) for dp in [(0, -1), (-1, 0), (0, 1), (1, 0)] ] ])[0][1]
		result[pos[1]][pos[0]] = "$"
	return result

maze_raw = sys.stdin.readlines()
w = len(maze_raw[0])-1
h = len(maze_raw)
maze = [ [ maze_raw[y][x] for x in range(w) ] for y in range(h) ]

print "w h", w, h
print "\n".join(["".join(line) for line in maze])

start = get_point("S", maze, w, h)
goal  = get_point("G", maze, w, h)

print "start goal", start, goal

potential = make_potential_map(maze, w, h, start, goal)
result = draw_one_path(maze, potential, w, h, start, goal)

#print result
print "\n".join([ "".join(lst) for lst in result])

