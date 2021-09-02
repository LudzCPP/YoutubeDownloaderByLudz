import pytube
import tkinter as tk


class YoutubeDownloader(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Youtube Downloader by Ludz")
		self.geometry("500x450")

		self.window_top = tk.Label(text="Download a video!", font=("Comic Sans MS", 30, "bold"))
		self.window_top.pack(pady=30)

		self.url_input = tk.Entry(width=50)
		self.url_input.pack(pady=20)

		self.video_title = tk.Label(text="\n", font=("Arial", 13))
		self.video_title.pack()

		self.video_button = tk.Button(
			text="Download video",
			width=15,
			height=1,
			font=("Arial", 20),
			command=lambda:self.download_video(self.url_input.get())
		)
		self.video_button.pack(pady=20)

		self.audio_button = tk.Button(
			text="Download audio",
			width=15,
			height=1,
			font=("Arial", 20),
			command=lambda:self.download_audio(self.url_input.get())
		)
		self.audio_button.pack(pady=20)

		self.mainloop()

	def download_video(self, url):
		try:
			pytube.YouTube(url).check_availability()
		except:
			self.video_title.config(text="Video not found!\n", font=("Arial", 13))
		else:
			video_url = pytube.YouTube(url)
			video = video_url.streams.get_highest_resolution()
			video.download()
			self.video_title.config(text=f"Downloading...\n {video.title}", font=("Arial", 13))

	def download_audio(self, url):
		try:
			pytube.YouTube(url).check_availability()
		except:
			self.video_title.config(text="Video not found!\n", font=("Arial", 13))
		else:
			video_url = pytube.YouTube(url)
			audio = video_url.streams.get_audio_only()
			audio.download()
			self.video_title.config(text=f"Downloading...\n{audio.title}", font=("Arial", 13))
