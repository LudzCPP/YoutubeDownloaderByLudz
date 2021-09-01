import pytube
import tkinter as tk
from PIL import ImageTk, Image


class YoutubeDownloader(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Youtube Downloader by Ludz")
		self.geometry("500x300")

		# # logo
		# self.logo_image = ImageTk.PhotoImage(Image.open("yt_logo.png").resize((500, 150)))
		# self.logo = tk.Label(image=self.logo_image)
		# self.logo.grid(row=0, column=0)

		self.window_top = tk.Label(text="Download a video!", font=("Comic Sans MS", 30, "bold"))
		self.window_top.pack(pady=30)

		self.url_input = tk.Entry(width=50)
		self.url_input.pack()

		self.submit_button = tk.Button(text="Download", width=15, height=1, font=("Arial", 20), command=self.download_video)
		self.submit_button.pack(pady=20)

		self.mainloop()

	def download_video(self):
		video = pytube.YouTube(self.url_input.get())
		video.streams.get_highest_resolution().download()