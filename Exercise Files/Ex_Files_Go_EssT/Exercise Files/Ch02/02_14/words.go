package main

import (
	"fmt"
	"strings"
)

func main() {
	text := `
	Needles and pins
	Needles and pins
	Sew me a sail
	To catch me the wind
	`

	words := strings.Fields(text)
	fmt.Println(words)
	counts := map[string]int{} // Empty map
	for _, word := range words {
		_ , ok := counts[word]
		if !ok {
			counts[strings.ToLower(word)] = 0
		}
		counts[strings.ToLower(word)]++
	}

	for key, value := range(counts) {
		fmt.Printf("%s >> %d\n" , key , value)
	}
}
