import tkinter as tk
import requests

# ================== CONFIG ==================
API_KEY = "AIzaSyAAPjzc7anEdRy96EPZzKgc9BLDN-OTRos"  # <-- paste your Gemini API key here
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"

# ================== CHATBOT APP ==================
class ChatBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gemini ChatBot")
        self.root.geometry("500x600")

        # Chat display
        self.chat_display = tk.Text(root, wrap="word", state="disabled", bg="white", fg="black")
        self.chat_display.pack(padx=10, pady=10, fill="both", expand=True)

        # User input
        self.user_input = tk.Entry(root, width=60)
        self.user_input.pack(side="left", padx=10, pady=10, fill="x", expand=True)
        self.user_input.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(side="right", padx=10, pady=10)

    def send_message(self, event=None):
        user_message = self.user_input.get().strip()
        if not user_message:
            return

        # Show user message
        self.display_message("You", user_message)
        self.user_input.delete(0, tk.END)

        # Get bot response
        bot_response = self.get_gemini_response(user_message)
        self.display_message("Bot", bot_response)

    def display_message(self, sender, message):
        self.chat_display.config(state="normal")
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.config(state="disabled")
        self.chat_display.see(tk.END)

    def get_gemini_response(self, prompt):
        try:
            headers = {
                "Content-Type": "application/json",
                "X-goog-api-key": API_KEY
            }
            data = {
                "contents": [
                    {
                        "parts": [
                            {"text": prompt}
                        ]
                    }
                ]
            }
            response = requests.post(API_URL, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()

            # Extract text safely
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"Error: {e}"


# ================== RUN APP ==================
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotGUI(root)
    root.mainloop()
