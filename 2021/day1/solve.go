package day1

import "github.com/MM1132/advent-of-code-2021/utils"

// Return the count of times the value increases
func Solve() (counter int, err error) {
	intLines, err := utils.ReadFileLinesAsInt("./day1/input.txt")
	if err != nil {
		return
	}
	for i := 1; i < len(intLines); i++ {
		if intLines[i] > intLines[i-1] {
			counter++
		}
	}
	return
}

// Return the count of three-measurement increasements
func Solve2() (counter int, err error) {
	intLines, err := utils.ReadFileLinesAsInt("./day1/input.txt")
	if err != nil {
		return
	}
	for i := 3; i < len(intLines); i++ {
		previous := utils.SumInts(intLines[i-1], intLines[i-2], intLines[i-3])
		current := utils.SumInts(intLines[i], intLines[i-1], intLines[i-2])
		if current > previous {
			counter++
		}
	}

	return
}
