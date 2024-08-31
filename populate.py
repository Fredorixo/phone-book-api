from psycopg2 import connect
from os import getenv
from dotenv import load_dotenv

load_dotenv()

connection = connect(
    dbname = getenv("DATABASE_NAME"),
    user = getenv("DATABASE_USER"),
    password = getenv("DATABASE_PASSWORD"),
    host = getenv("DATABASE_HOST")
)

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        name VARCHAR(200) NOT NULL,
        phone_number VARCHAR(15) PRIMARY KEY,
        email VARCHAR(254)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        user_details VARCHAR(15) NOT NULL,
        contact_number VARCHAR(15) NOT NULL,
        alias VARCHAR(200) NOT NULL,
        FOREIGN KEY (user_details) REFERENCES users (phone_number) ON DELETE CASCADE
    )
''')

def add_user(name, phone_number, email):
    try:
        cursor.execute('''
            INSERT INTO users (name, phone_number, email)
            VALUES (%s, %s, %s)
            ''', (name, phone_number, email)
        )

        connection.commit()
        print(f"User '{name}' with Phone {phone_number} added successfully")
    except:
        print("Error Occurred")

def add_contact(user_details, contact_number, alias):
    try:
        cursor.execute('''
            INSERT INTO contacts (user_details, contact_number, alias)
            VALUES (%s, %s, %s)
            ''', (user_details, contact_number, alias)
        )

        connection.commit()
        print(f"Phone {contact_number} added successfully to {user_details}'s contact")
    except:
        print("Error Occurred")

def get_all_users():
    try:
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()
    except:
        print("Error Occurred")

def get_contacts_of_user(user_details):
    try:
        cursor.execute('''
            SELECT contact_number, alias FROM contacts WHERE user_details = %s
            ''', (user_details,)
        )

        return cursor.fetchall()
    except:
        print("Error Occurred")

if __name__ == "__main__":
    # Registering Alice and Bob with the application
    add_user("Alice Johnson", "+1234567890", "alice@example.com")
    add_user("Bob Smith", "+0987654321", "bob@example.com")

    # Adding contacts for Alice (phone_number = "+1234567890")
    add_contact("+1234567890", "+1122334455", "Charlie")
    add_contact("+1234567890", "+5566778899", "Dave")
    add_contact("+1234567890", "+1239447565", "Dank Memer")

    # Adding contacts for Bob (phone_number = "+0987654321")
    add_contact("+0987654321", "+6677889900", "Eve")
    add_contact("+0987654321", "+2233445566", "Frank")
    add_contact("+0987654321", "+1239447565", "Dank")
    add_contact("+0987654321", "+1234567890", "Alice")

    # Retrieve all users
    users = get_all_users()
    print("\nAll Users:")
    for user in users:
        print(user)

    # Retrieve all contacts
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    print("\nAll Contacts:")
    for contact in contacts:
        print(contact)

    # Retrieve contacts for Alice
    alice_contacts = get_contacts_of_user("+1234567890")
    print("\nAlice's Contacts:")
    for contact in alice_contacts:
        print(contact)

    # Retrieve contacts for Bob
    bob_contacts = get_contacts_of_user("+0987654321")
    print("\nBob's Contacts:")
    for contact in bob_contacts:
        print(contact)

connection.close()