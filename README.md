
# 🏴‍☠️ Pirate AI Chatbot ⚓

Ahoy, matey! Welcome to **Pirate AI Chatbot**, a fun and interactive Streamlit app powered by **AISuite** where you can chat with an AI bot that talks like a true pirate! Choose from multiple AI models and ask your questions in the Pirate tongue. 🦜

## 📖 Features
- Interactive chatbot that responds in Pirate English.
- Select your preferred AI model from **OpenAI GPT-4o Mini**, **Anthropic Claude**, or **Groq Llama**.
- Simple and user-friendly interface built with **Streamlit**.
- Stylish and visually engaging output for a great user experience.

---

## 🚀 Getting Started

Follow these instructions to set up and run the Pirate AI Chatbot locally.

### Prerequisites

Make sure you have the following installed on your system:
- Python 3.8 or later
- `pip` for managing Python packages

---

### 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pirate-ai-chatbot.git
   cd pirate-ai-chatbot
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

3. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory to store your API keys:
   ```bash
   touch .env
   ```

---

### 🗝️ Setting Up API Keys

The app uses **Anthropic**, **OpenAI**, and **Groq** APIs for its AI models. You need to set up the following API keys in the `.env` file.

1. Open the `.env` file in a text editor.
2. Add the API keys in the following format:
   ```env
   ANTHROPIC_API_KEY=your_anthropic_api_key
   OPENAI_API_KEY=your_openai_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

   - Replace `your_anthropic_api_key`, `your_openai_api_key`, and `your_groq_api_key` with your actual API keys. You can obtain these keys from:
     - [Anthropic API](https://www.anthropic.com/)
     - [OpenAI API](https://platform.openai.com/)
     - [Groq API](https://groq.com/)

---

### ▶️ Running the App

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at [http://localhost:8501](http://localhost:8501).

3. Interact with the Pirate AI Chatbot:
   - Choose your preferred model from the dropdown.
   - Enter your query, and click **"Get Pirate Response"** to chat with the Pirate AI!

---

## 📂 Project Structure

```
pirate-ai-chatbot/
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
├── .env                # API keys (ignored by Git)
├── README.md           # Documentation
└── .gitignore          # Files to ignore in Git
```

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) - Web framework for Python.
- [AISuite](https://aisuite.docs.example.com) - For integrating with AI models.
- [Python](https://www.python.org/) - Programming language.

---

## ✨ Features in Progress
- Add more pirate-themed design elements to the UI.
- Support additional AI models and response customization.

---

## 🤝 Contributing

Feel free to fork the repository and submit a pull request for any feature enhancements or bug fixes. All contributions are welcome!

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🏴‍☠️ Contact

For any issues or queries, open an issue on GitHub or reach out to me on:

- Discord: [exala.h](https://discord.com/users/exala.h)
- Instagram: [@exala.h](https://www.instagram.com/exala.h/)
- Email: **hasan.ag93@gmail.com**
