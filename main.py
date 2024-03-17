import tkinter as tk
import requests

class PostViewerApp:
    def __init__(self, app):
        self.app = app
        app.title("Получение информации о посте")

        self.label = tk.Label(app, text="Введите ID поста:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(app)
        self.entry.pack()

        self.button = tk.Button(app, text="Получить информацию", command=self.show_post_info)
        self.button.pack(pady=10)

        self.info_text = tk.Text(app, height=10, width=50)
        self.info_text.pack(pady=10)
        self.info_text.config(state=tk.DISABLED)

    def get_post_by_id(self, post_id):
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        response = requests.get(url)
        if response.status_code == 200:
            post_data = response.json()
            return post_data

    def show_post_info(self):
        post_id = self.entry.get()
        post_data = self.get_post_by_id(post_id)
        if post_data:
            self.info_text.config(state=tk.NORMAL)
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, f"ID: {post_data['id']}\n")
            self.info_text.insert(tk.END, f"Пользователь ID: {post_data['userId']}\n")
            self.info_text.insert(tk.END, f"Заголовок: {post_data['title']}\n")
            self.info_text.insert(tk.END, f"Текст: {post_data['body']}")
            self.info_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = PostViewerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()