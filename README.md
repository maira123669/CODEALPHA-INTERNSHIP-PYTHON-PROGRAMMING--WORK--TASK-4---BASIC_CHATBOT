#  Rule-Based Chatbot (Python)

##  Project Description

The **Rule-Based Chatbot** is a simple Python command-line chatbot that responds to user messages using predefined rules. It recognizes common greetings and questions, then returns appropriate responses. If the input does not match any known rule, the chatbot provides a default reply.

This project demonstrates the basics of chatbot development using Python, including functions, conditional statements, loops, string manipulation, and user interaction.

---

##  Features

- Interactive command-line chatbot.
- Responds to greetings like **Hello** and **Hi**.
- Answers common questions such as:
  - "How are you?"
  - "What is your name?"
- Handles unknown inputs with a default response.
- Conversation continues until the user types **bye**.
- Simple and beginner-friendly implementation.

---

##  Technologies Used

- Python 3

---

##  Project Structure

```
Rule-Based-Chatbot/
│── chatbot.py
│── README.md
```

---

##  How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python chatbot.py
```

---

##  Example Conversation

```
--- AlphaBot Rules Chatbot ---

You: Hello
Bot: Hi! How can I help you today?

You: What is your name?
Bot: I am AlphaBot, your friendly neighborhood rule-based assistant.

You: How are you?
Bot: I'm just a Python script, but I'm running perfectly! Thanks for asking.

You: Bye
Bot: Goodbye! Have a fantastic day!
```

---

##  How It Works

1. The chatbot waits for user input.
2. User input is converted to lowercase for easier matching.
3. The program checks predefined rules using `if-elif-else` conditions.
4. If a matching rule is found, the corresponding response is displayed.
5. If no rule matches, the chatbot returns a default message.
6. The chat ends when the user enters **bye**.

---

##  Concepts Used

- Functions
- Conditional Statements (`if`, `elif`, `else`)
- Loops (`while`)
- String Manipulation
- User Input
- Rule-Based Decision Making

---

##  Future Improvements

- Add more conversation rules.
- Support multiple languages.
- Store chat history.
- Use Natural Language Processing (NLP).
- Integrate speech recognition and text-to-speech.
- Build a graphical user interface (GUI).

---

##  Author

**Maira Masood**

BS Computer Science (BSCS)

---

##  License

This project is created for learning and educational purposes.
