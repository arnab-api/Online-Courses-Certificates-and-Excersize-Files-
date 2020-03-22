package main

import (
	"fmt"
)

func cleanup(name string) {
	fmt.Printf("Cleaning up %s\n", name)
}

func worker() {
	defer cleanup("A")
	fmt.Println("workerA")

	defer cleanup("B")
	fmt.Println("workerB")
}

func main() {
	worker()
}
