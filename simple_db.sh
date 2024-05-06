#!/bin/bash

# File where the database entries are stored
DB_FILE="database"

# Function to set a key-value pair
db_set() {
    echo "$1,$2" >> "$DB_FILE"
}

# Function to get the value by key
db_get() {
    grep "^$1," "$DB_FILE" | sed -e "s/^$1,//" | tail -n 1
}

# Simple text-based menu for database interaction
while true; do
    echo "Simple DB Menu:"
    echo "1. Set a new key-value pair"
    echo "2. Get a value by key"
    echo "3. Exit"
    read -p "Select an option: " option

    case $option in
        1)
            read -p "Enter key: " key
            read -p "Enter value: " value
            db_set "$key" "$value"
            echo "Stored $key with value $value."
            ;;
        2)
            read -p "Enter key: " key
            value=$(db_get "$key")
            echo "Value: $value"
            ;;
        3)
            break
            ;;
        *)
            echo "Invalid option. Please try again."
            ;;
    esac
done
