package main

import (
	"fmt"
	"net/http"
)

func healthHandler(w http.ResponseWriter, r *http.Request) {
	// Vérifier l'état de l'application et répondre avec un statut 200 OK
	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "OK")
}

func main() {
	// Définir le handler pour le healthcheck
	http.HandleFunc("/health", healthHandler)

	// Définir un handler pour la route principale
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello, World!")
	})

	// Lancer le serveur sur le port 8080
	fmt.Println("Le serveur tourne sur http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}