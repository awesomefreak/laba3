class State: 
    def __init__(self, n, src, dest, tmp, step): 
        self.n = n
        self.src = src
        self.dest = dest 
        self.tmp = tmp
        self.step = step
def tower(n, src, dest, tmp):
	stack = [State(n, src, dest, tmp, 0)]
	while len(stack):
		state = stack[-1]
		if state.step == 0:
			if state.n == 0:
				stack.pop()
			else:
				state.step += 1
				stack.append(State(state.n - 1, state.src, state.tmp, state.dest, 0))

		elif state.step == 1:
			print(f"from stand №{state.src} to №{state.dest}")
			state.step += 1
			stack.append(State(state.n - 1, state.tmp, state.dest, state.src, 0))
		elif state.step == 2:
			stack.pop()
if __name__=='__main__':
	tower(int(input("write size of first tower")), 1, 2, 3)
