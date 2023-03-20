import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("stockfish")

class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    def jogar(self, movimento):
        if movimento not in self.board.legal_moves:
            raise ValueError('Movimento inválido.')
        self.board.push(movimento)

    def jogar_ia(self, depth=3):
        result = engine.play(self.board, chess.engine.Limit(depth=depth))
        self.board.push(result.move)

    def avaliar_tabuleiro(self):
        # Implemente a avaliação do tabuleiro aqui, usando uma heurística ou rede neural
         piece_values = {'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': -100, 'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 100, '.': 0}
    matrix_board = [[0 for i in range(8)] for j in range(8)] #cria matriz 8x8 de zeros
    for row_index, row in enumerate(board.split('/')):
        column_index = 0
        for cell in row:
            if cell.isdigit(): # se o caractere for um número, significa que existem células vazias neste local
                column_index += int(cell)
            else: # caso contrário, é uma peça
                matrix_board[row_index][column_index] = piece_values[cell]
                column_index += 1

    def minimax(self, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.board.is_game_over():
            return self.avaliar_tabuleiro()

        if maximizing_player:
            best_value = float('-inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                value = self.minimax(depth - 1, alpha, beta, False)
                self.board.pop()
                best_value = max(best_value, value)
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return best_value
        else:
            best_value = float('inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                value = self.minimax(depth - 1, alpha, beta, True)
                self.board.pop()
                best_value = min(best_value, value)
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return best_value
