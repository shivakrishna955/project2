import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class JarvisGUI:

    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("900x600")
        self.root.title("JARVIS AI")

        self.title = ctk.CTkLabel(
            self.root,
            text="JARVIS AI ASSISTANT",
            font=("Arial", 28, "bold")
        )
        self.title.pack(pady=20)

        self.output = ctk.CTkTextbox(
            self.root,
            width=700,
            height=350
        )
        self.output.pack(pady=20)

        self.button = ctk.CTkButton(
            self.root,
            text="Start Listening"
        )
        self.button.pack(pady=20)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = JarvisGUI()
    app.run()