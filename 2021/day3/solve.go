package day3

import (
	"fmt"
	"strconv"

	"github.com/MM1132/advent-of-code-2021/utils"
)

func Solve() int64 {
	lines, _ := utils.ReadLines("./day3/input.txt")

	/* lines := []string{
		"00100",
		"11110",
		"10110",
		"10111",
		"10101",
		"01111",
		"00111",
		"11100",
		"10000",
		"11001",
		"00010",
		"01010",
	} */
	/* test = removeAllWithout(test, '0', 7)
	fmt.Println("Test: ", test) */

	for i := 0; i < 12; i++ {
		fmt.Println(lines)
		if mostCommon(lines, i) == '0' {
			fmt.Println("more ones, index", i)
			lines = removeAllWithout(lines, '1', i)
		} else if mostCommon(lines, i) == '1' {
			fmt.Println("more zeroes, index", i)
			lines = removeAllWithout(lines, '0', i)
		}
		if len(lines) == 1 {
			fmt.Println("one left")
			break
		}
	}
	fmt.Println(lines)

	i, _ := strconv.ParseInt(string(lines[0]), 2, 64)
	return i

}

func removeAllWithout(input []string, char rune, index int) []string {
	output := []string{}
	for _, v := range input {
		if rune(v[index]) == char {
			output = append(output, v)
		}
	}
	return output
}

func mostCommon(input []string, index int) rune {
	counter0 := 0
	counter1 := 0
	for _, v := range input {
		if v[index] == '0' {
			counter0++
		} else if v[index] == '1' {
			counter1++
		}
	}
	// If we have more zeroes, return false
	if counter0 > counter1 {
		return '0'
	} else if counter1 > counter0 {
		return '1'
	}
	// But if they are both equal, we are going for number 1
	// Default
	// oxygen generator rating 1
	// CO2 scrubber rating 0
	return '1'
}
