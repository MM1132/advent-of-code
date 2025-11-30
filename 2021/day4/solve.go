package day4

import (
	"fmt"
	"strings"

	"github.com/MM1132/advent-of-code-2021/utils"
)

type Number struct {
	value  int
	marked bool
}

type Board struct {
	numbers [5][5]Number
	solved  bool
}

func Solve() {
	lines, _ := utils.ReadLines("./day4/input.txt")
	tmpNumbers := strings.Split(lines[0], ",")
	drawNumbers := []int{}
	for _, v := range tmpNumbers {
		drawNumbers = append(drawNumbers, utils.Atoi(v))
	}

	boards := []Board{}

	// The index of the board
	for i := 0; i < (len(lines))/6; i++ {
		tmpBoard := Board{}
		// The y
		for j := 0; j < 5; j++ {
			tmpRow := strings.Split(lines[(i*6)+j+2], " ")
			// Remove empty elements
			row := []string{}
			for _, v := range tmpRow {
				if len(v) > 0 {
					row = append(row, v)
				}
			}
			// The x
			for k := range row {
				tmpBoard.numbers[j][k] = Number{value: utils.Atoi(row[k])}
			}
		}
		boards = append(boards, tmpBoard)
	}

	// Go through numbers
	for _, v := range drawNumbers {
		// Go through all the locations of all boards
		// Mark a single number
		for k, b := range boards {
			for i := 0; i < 5; i++ {
				for j := 0; j < 5; j++ {
					if b.numbers[i][j].value == v {
						boards[k].numbers[i][j].marked = true
					}
				}
			}
		}
		for boardIndex := 0; boardIndex < len(boards); boardIndex++ {
			// And now checked if any of the boards has been solved
			if checkSolve(boards[boardIndex]) {
				if boards[boardIndex].solved == false {
					sum := 0
					for i := 0; i < 5; i++ {
						for j := 0; j < 5; j++ {
							if boards[boardIndex].numbers[i][j].marked == false {
								sum += boards[boardIndex].numbers[i][j].value
							}
						}
					}
					sum *= v
					fmt.Println(sum)
					boards[boardIndex].solved = true
				}
			}
		}
	}
}

// Check if the board has been solved or not
func checkSolve(board Board) bool {
	// Rows and columns
	for i := 0; i < 5; i++ {
		rowCounter := 0
		colCounter := 0
		for j := 0; j < 5; j++ {
			if board.numbers[i][j].marked {
				rowCounter++
			}
			if board.numbers[j][i].marked {
				colCounter++
			}
		}
		if rowCounter == 5 || colCounter == 5 {
			return true
		}
	}
	return false
}
