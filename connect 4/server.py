from flask import Flask, jsonify, request, send_from_directory
import os
import connect4 as c4

app = Flask(__name__, static_folder='web')

board = c4.create_board()
turn = 0  # 0 for player 1, 1 for player 2
winner = None

def game_state():
    return {
        'board': board,
        'turn': turn + 1,
        'winner': winner,
        'game_over': winner is not None
    }

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    # serve static files
    return send_from_directory(app.static_folder, path)

@app.route('/api/state')
def state():
    return jsonify(game_state())

@app.route('/api/move', methods=['POST'])
def move():
    global turn, winner
    data = request.get_json(force=True)
    col = data.get('col')
    if winner is not None:
        return jsonify(game_state())
    if col is None or not (0 <= col < c4.COLS) or not c4.is_valid_location(board, col):
        return jsonify(game_state())
    row = c4.get_next_open_row(board, col)
    c4.drop_piece(board, row, col, turn + 1)
    if c4.winning_move(board, turn + 1):
        winner = turn + 1
    else:
        turn = (turn + 1) % 2
    return jsonify(game_state())

@app.route('/api/reset', methods=['POST'])
def reset():
    global board, turn, winner
    board = c4.create_board()
    turn = 0
    winner = None
    return jsonify(game_state())

if __name__ == '__main__':
    app.run(debug=True)
