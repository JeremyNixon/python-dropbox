import copy

def make_graph(n):
	return [[0]*n for i in range(n)]

def input_graph():
	N = input()
	g = make_graph(N)
	for n in range(N):
		x = map(int, raw_input().split())
		for i in x:
			g[n][i] = 1
	return g

def matrix_multiply(A, B):
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    C = [[0]*p for i in range(n)]
    for i in range(n):
        ai = A[i]
        ci = C[i]
        for k in range(m):
            bk = B[k]
            a = ai[k]
            for j in range(p):
                ci[j] += a * bk[j]
    return C

def subtract(matr_a, matr_b):
    return map(lambda i: map(lambda x, y: x - y, matr_a[i], matr_b[i]), xrange(len(matr_a)))

def print_graph(A):
	construct = ""
	for i in range(len(A)):
		for imp in range(len(A[i])):
			if (A[i][imp] == 1):
				construct += str(imp)
				if (imp < len(A[i])-1):
					construct += " "
		if (i < len(A)-1):
			construct += "\n"
	print construct
	
A = input_graph()
B = copy.deepcopy(A)

for i in range(0,len(A)):
	B = matrix_multiply(A,B)
	#Be efficient about this subtraction

	A = subtract(A,B)
print_graph(A)








#A = matrix_multiply(A, A**A)