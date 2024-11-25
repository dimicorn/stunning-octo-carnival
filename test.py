import sys
import json

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def leftIndex(points):
	'''Finding the left most point'''
	minn = 0
	for i in range(1,len(points)):
		if points[i].x < points[minn].x:
			minn = i
		elif points[i].x == points[minn].x:
			if points[i].y > points[minn].y:
				minn = i
	return minn

def orientation(p, q, r):
	'''
	To find orientation of ordered triplet (p, q, r). 
	The function returns following values 
	0 --> p, q and r are collinear 
	1 --> Clockwise 
	2 --> Counterclockwise 
	'''
	val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

	if val == 0:
		return 0
	elif val > 0:
		return 1
	return 2

def JarvisWrap(points: list[Point], n: int) -> list:
	if n < 3:
		return []

	l = leftIndex(points)

	hull = []
	p, q = l, 0

	while True:
		hull.append(p)
		q = (p + 1) % n

		for i in range(n):
			if orientation(points[p], points[i], points[q]) == 2:
				q = i
		p = q

		if p == l:
			return hull
'''
int main(int argc, char** argv) {
    return 0;
}
'''
def main():
	input_file = sys.argv[1]
	with open(input_file) as f:
		input = json.load(f)
	points = [Point(*point) for point in input['test_points']]
	idx = JarvisWrap(points, len(points))
	for each in idx:
		print(points[each].x, points[each].y)

if __name__ == '__main__':
	main()