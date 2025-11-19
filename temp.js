let ai = player2;
let human = player1;
let scores = {};
scores[player1] = -10;
scores[player2] = 10;
scores['tie'] = 0;
// COMPUTER AI CODE BELOW

function bestMove() {       // AI to make its turn
    
    let bestScore = -Infinity;
    let bestMove = null;
    board.forEach( (_, i) => {
        if (board[i] === '') {  
            board[i] = ai;
            let score = minimax(board, 0, false);
            board[i] = '';
            if (score > bestScore) {
                bestScore = score;
                bestMove = i;                
            }
        }
    });
    return bestMove;    
}

function minimax(board, depth, isMaximizing) {
    let result = checkGameStatus(board);
    if (result !== null) {   //checks if move is winning (base case for recursion)
        return scores[result];
    }
    if (isMaximizing) {
        let bestScore = -Infinity;
        board.forEach( (_,i) => {
             if (board[i] === '') {    
                board[i] = ai;
                let score = minimax(board, depth + 1, false);
                board[i] = '';
                bestScore = Math.max(score, bestScore);
            }
        });
        return bestScore;
    } else {
        let bestScore = Infinity; 
        board.forEach( (_,i) => {
            if (board[i] === '') {   
                board[i] = human;
                let score = minimax(board, depth + 1, true);
                board[i] = '';
                bestScore = Math.min(score, bestScore);
            }
        });
        return bestScore;
    }
}