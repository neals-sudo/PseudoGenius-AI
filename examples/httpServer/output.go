package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"

	_ "github.com/lib/pq"
	"github.com/gorilla/mux"
)

const (
	host     = "localhost"
	port     = 8080
	user     = "admin"
	password = "pass"
	dbname   = "test"
)

func main() {
	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
		"password=%s dbname=%s sslmode=disable",
		host, port, user, password, dbname)

	db, err := sql.Open("postgres", psqlInfo)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	err = db.Ping()
	if err != nil {
		log.Fatal(err)
	}

	router := mux.NewRouter()

	router.HandleFunc("/api/create", func(w http.ResponseWriter, r *http.Request) {
		username := r.FormValue("username")
		password := r.FormValue("password")

		if username == "" || password == "" {
			http.Error(w, "Invalid parameters", http.StatusBadRequest)
			return
		}

		_, err := db.Exec("INSERT INTO users (username, password) VALUES ($1, $2)", username, password)
		if err != nil {
			http.Error(w, "Failed to create user", http.StatusInternalServerError)
			return
		}

		w.WriteHeader(http.StatusOK)
	}).Methods("POST")

	router.HandleFunc("/api/password_change", func(w http.ResponseWriter, r *http.Request) {
		username := r.FormValue("username")
		newpassword := r.FormValue("newpassword")

		if username == "" || newpassword == "" {
			http.Error(w, "Invalid parameters", http.StatusBadRequest)
			return
		}

		_, err := db.Exec("UPDATE users SET password = $1 WHERE username = $2", newpassword, username)
		if err != nil {
			http.Error(w, "Failed to update password", http.StatusInternalServerError)
			return
		}

		w.WriteHeader(http.StatusOK)
	}).Methods("PUT")

	router.HandleFunc("/api/retrieve", func(w http.ResponseWriter, r *http.Request) {
		username := r.FormValue("username")

		if username == "" {
			http.Error(w, "Invalid parameters", http.StatusBadRequest)
			return
		}

		var retrievedUsername string
		err := db.QueryRow("SELECT username FROM users WHERE username = $1", username).Scan(&retrievedUsername)
		if err != nil {
			http.Error(w, "User not found", http.StatusNotFound)
			return
		}

		w.WriteHeader(http.StatusOK)
	}).Methods("GET")

	router.HandleFunc("/api/remove", func(w http.ResponseWriter, r *http.Request) {
		username := r.FormValue("username")

		if username == "" {
			http.Error(w, "Invalid parameters", http.StatusBadRequest)
			return
		}

		_, err := db.Exec("DELETE FROM users WHERE username = $1", username)
		if err != nil {
			http.Error(w, "Failed to delete user", http.StatusInternalServerError)
			return
		}

		w.WriteHeader(http.StatusOK)
	}).Methods("DELETE")

	log.Fatal(http.ListenAndServe(":8080", router))
}
