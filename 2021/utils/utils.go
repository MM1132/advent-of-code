package utils

import (
	"io/ioutil"
	"strconv"
	"strings"
)

func ReadLines(filePath string) (strLines []string, err error) {
	bytes, err := ioutil.ReadFile(filePath)
	if err != nil {
		return
	}
	strLines = strings.Split(strings.ReplaceAll(string(bytes), "\r\n", "\n"), "\n")
	return
}

func ReadFileLinesAsInt(filePath string) (intLines []int, err error) {
	strLines, err := ReadLines(filePath)
	if err != nil {
		return
	}
	for _, v := range strLines {
		var intValue int
		intValue, err = strconv.Atoi(v)
		if err != nil {
			return
		}
		intLines = append(intLines, intValue)
	}
	return
}

func SumInts(ints ...int) (sum int) {
	for _, v := range ints {
		sum += v
	}
	return
}

func Atoi(number string) int {
	n, _ := strconv.Atoi(number)
	return n
}
