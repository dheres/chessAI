import chess

class State(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.board = chess.Board()

	def serialize(self):
		# 257 bits acording to readme
		pass

	def edges(self):
		return list(self.board.legal_moves)

	def value(self):
		return 1 

if __name__ == '__main__':
	s = State()
	print(s.edges())

