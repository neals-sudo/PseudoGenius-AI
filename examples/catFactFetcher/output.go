package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

type FactResponse struct {
	Data []Fact `json:"data"`
}

type Fact struct {
	Fact string `json:"fact"`
}

func GetRandomFact() (string, error) {
	// Send GET request
	resp, err := http.Get("https://meowfacts.herokuapp.com/?count=1")
	if err != nil {
		fmt.Println("Error: Failed to send GET request")
		return "", err
	}
	defer resp.Body.Close()

	// Make sure the http response is 200
	if resp.StatusCode != http.StatusOK {
		fmt.Println("Error: Non-200 HTTP status:", resp.StatusCode)
		return "", fmt.Errorf("Non-200 HTTP status: %v", resp.StatusCode)
	}

	// Decode JSON response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error: Failed to read body")
		return "", err
	}

	var factResponse FactResponse
	err = json.Unmarshal(body, &factResponse)
	if err != nil {
		fmt.Println("Error: Failed to decode JSON")
		return "", err
	}

	// Read Fact
	if len(factResponse.Data) == 0 {
		fmt.Println("Error: No facts found in response")
		return "", fmt.Errorf("No facts found in response")
	}
	fact := factResponse.Data[0].Fact

	// Return Fact
	return fact, nil
}

func main() {
	fact, err := GetRandomFact()
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}

	fmt.Println("Random Cat Fact:", fact)
}
