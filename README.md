# 📚 Library Chatbot (Google PaLM-powered)

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)  
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green)](https://www.langchain.com/)  
[![PaLM](https://img.shields.io/badge/Google%20PaLM-AI-orange)](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/overview)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](./CONTRIBUTING.md)  

An intelligent **library management chatbot** powered by **Google PaLM API** and built with **Python + LangChain**.  
It allows users to borrow/return items, manage audiobooks, e-magazines, and track fines seamlessly – all through a **conversational interface**.

---

## ✨ Features
- 👤 **User Management** – Register & authenticate users  
- 📖 **Borrow & Return** – Books, Audiobooks, and E-Magazines  
- ⏳ **Waitlist Handling** – Auto-issue when available  
- 💰 **Fine Calculation** – Late returns = auto fines  
- 📂 **Archive E-Magazines** – Manage digital editions  
- 📊 **Reports** – Usage summary, fines, popular books  
- 🤖 **Conversational Flow** – Powered by **LangChain + PaLM**  

---

## ⚡ Tech Stack
- **Python 3.11+**
- **LangChain**
- **Google Generative AI (PaLM API)**
- **Flask** (Optional: Web interface)
- **Virtualenv**

---

## 📸 Sample Output
```powershell
(.venv) PS C:\Users\KIIT\portfolio-main\library_palm_chatbot> python .\app.py

📚 Welcome to Library Chatbot (Google PaLM-powered, free tier)
Type 'exit' anytime to quit.

You: register user 101 "Suchit" "suchit@kiit.ac.in"
Bot 🤖: ✅ User registered successfully!

You: borrow "Harry Potter" as book by user 101
Bot 🤖: ✅ User 101 borrowed "Harry Potter" (Book).
Due in 10 days. Please return on time.

You: return "Harry Potter" late by 2 days
Bot 🤖: ⚠️ Returned late. Fine = Rs.20

You: borrow "AI Revolution" as e-magazine by user 101
Bot 🤖: ✅ E-Magazine "AI Revolution" issued to User 101.
Archive copy saved in library database.

You: show reports
Bot 🤖: 📊 Library Report
   - Total fines collected: Rs.20
   - Most borrowed item: "Harry Potter"
   - Active borrowings: 1
   - Waitlists active: 0
