# ⭐ Name Pattern Printer

A Python program that takes a user's name as input and prints it using **7×7 star patterns** for each alphabet letter.

## 📌 Features

* Takes the name as user input.
* Automatically converts the input to uppercase.
* Supports all letters from **A to Z**.
* Generates individual 7×7 patterns for each character.
* Prints the complete name horizontally.
* Uses Python `match-case` for letter selection.

## 🖥️ Example

### Input

```text
Enter Name: Sarthak
```

### Output

```textEnter Name: sarthak

Name:  SARTHAK

============================== SARTHAK ==============================

  * * * * *         * * * * *       * * * * * *       * * * * * * *     *           *       * * * * *       *       *         
*                 *           *     *           *           *           *           *     *           *     *     *           
*                 *           *     *           *           *           *           *     *           *     *   *             
  * * * * *       * * * * * * *     * * * * * *             *           * * * * * * *     * * * * * * *     * *               
            *     *           *     *       *               *           *           *     *           *     *   *             
            *     *           *     *         *             *           *           *     *           *     *     *           
  * * * * *       *           *     *           *           *           *           *     *           *     *       *         

```

> The exact appearance depends on the patterns defined in the program.

## ⚙️ How It Works

1. The program asks the user to enter a name.
2. The name is converted to uppercase.
3. Each character is stored separately.
4. A `match-case` statement selects the corresponding alphabet pattern.
5. Each letter is generated as a 7-row pattern.
6. The patterns are printed row by row to form the complete name.

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Loops
* Conditional statements
* `match-case`
* String formatting

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Name-Pattern-Printer.git
```

Open the project folder:

```bash
cd Name-Pattern-Printer
```

Run the program:

```bash
python name_pattern.py
```

Enter your name when prompted.

## 📚 Learning Purpose

This project was created to practice:

* Nested loops
* Pattern printing
* Lists
* Conditional logic
* Python `match-case`
* String manipulation
* Basic programming logic

## 🔮 Future Improvements

* Add support for spaces between names.
* Improve the design of individual letter patterns.
* Add numbers and special characters.
* Allow users to select different pattern styles.
* Reduce repetitive code using functions.

## 👨‍💻 Author

**Sarthak Ankolekar**

---

⭐ If you find this project useful, consider giving the repository a star!
