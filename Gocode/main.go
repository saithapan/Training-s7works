package main

import (
	"fmt"
	"net/http"

	"github.com/pluralsight/webservice/controllers"
)

func main() {
	fmt.Println("hello world")
	num := 12
	fmt.Println(num)
	var arr [3]int
	arr[0] = 1
	arr[1] = 2
	arr[2] = 3
	fmt.Println(arr)

	arrr := [3]int{1, 2, 3}
	fmt.Println(arrr)
	slice := arrr[:]
	arrr[1] = 22
	slice[2] = 27
	fmt.Println(arrr, slice)

	arrrr := []int{1, 2, 3}
	fmt.Println(arrrr)

	arrrr = append(arrrr, 4)
	fmt.Println(arrrr)

	controllers.RegisterControllers()
	http.ListenAndServe(":3000", nil)

}
