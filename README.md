# **Library Manager**

**Library Manager** is a Command-Line Interface (CLI) based Library Management System built in Python. It allows users to manage their personal digital library by adding, removing, searching, and viewing books. The system stores book details in a file and provides an interactive menu for seamless book management.

---

## **Features**

- **Add a Book 📖**: Input book details (title, author, year, genre, read status) and store them.
- **Remove a Book 🗑️**: Delete a book by its title if it exists.
- **Search for Books 🔍**: Find books by title or author.
- **Display All Books 📚**: View a complete list of books along with their details.
- **Library Statistics 📊**: Get insights like total books and percentage read.
- **Data Persistence 💾**: All book records are saved in a file to ensure they are not lost.
- **CLI-Based Interface 🖥️**: Simple text-based menu for easy interaction.

---

## **How It Works**

1. The program loads existing books from the file (`library.txt`) when started.
2. Users navigate through an interactive menu to manage their library.
3. All updates (adding/removing books) are saved automatically to the file.
4. The program continues running until the user chooses to exit.

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/library-manager.git
   cd library-manager
