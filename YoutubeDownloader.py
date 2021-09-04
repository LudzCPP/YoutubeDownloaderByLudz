import pytube
import tkinter as tk
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


class YoutubeDownloader(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Youtube Downloader by Ludz")
		self.geometry("500x680")

		self.window_top = tk.Label(text="Download a video!", font=("Comic Sans MS", 30, "bold"))
		self.window_top.pack(pady=30)

		self.input_title = tk.Label(text="URL:", font=("Comic Sans MS", 17, "bold"))
		self.input_title.pack()

		self.url_input = tk.Entry(width=50)
		self.url_input.pack(pady=15)

		self.video_title = tk.Label(text="\n", font=("Arial", 13), wraplength=500)
		self.video_title.pack()

		self.video_button = tk.Button(
			text="Download video",
			width=15,
			height=1,
			font=("Arial", 20),
			command=lambda: self.download_video(self.url_input.get())
		)
		self.video_button.pack(pady=20)

		self.audio_button = tk.Button(
			text="Download audio",
			width=15,
			height=1,
			font=("Arial", 20),
			command=lambda: self.download_audio(self.url_input.get())
		)
		self.audio_button.pack(pady=15)

		self.start = tk.Entry(width=3, justify=tk.CENTER)
		self.start.insert(0, 0)
		self.start.pack()

		self.stop = tk.Entry(width=3, justify=tk.CENTER)
		self.stop.insert(0, 5)
		self.stop.pack()

		self.cut_button = tk.Button(
			text="Cut audio",
			width=15,
			height=1,
			font=("Arial", 20),
			command=lambda: self.cut_audio(self.url_input.get(), float(self.start.get()), float(self.stop.get()))
		)
		self.cut_button.pack(pady=2)

		self.keywords_button = tk.Button(
			text="Keywords",
			width=15,
			height=1,
			font=("Arial", 20),
			command=lambda: self.get_keywords(self.url_input.get())
		)
		self.keywords_button.pack(pady=15)

		self.mainloop()

	def download_video(self, url):
		try:
			pytube.YouTube(url).check_availability()
		except:
			self.video_title.config(text="Video not found!\n", font=("Arial", 13))
		else:
			video_url = pytube.YouTube(url)
			video = video_url.streams.get_highest_resolution()
			video.download(filename=f"{video_url.title}.mp4".replace(":", ""))
			self.video_title.config(text=f"Downloading...\n {video.title}", font=("Arial", 13))

	def download_audio(self, url):
		try:
			pytube.YouTube(url).check_availability()
		except:
			self.video_title.config(text="Video not found!\n", font=("Arial", 13))
		else:
			video_url = pytube.YouTube(url)
			audio = video_url.streams.get_audio_only()
			audio.download(filename=f"{video_url.title}.mp4".replace(":", ""))
			self.video_title.config(text=f"Downloading...\n{audio.title}", font=("Arial", 13))

			return f"{video_url.title}".replace(":", "")

	def get_keywords(self, url):
		try:
			pytube.YouTube(url).check_availability()
		except:
			self.video_title.config(text="Video not found!\n", font=("Arial", 13))
		else:
			video = pytube.YouTube(url)
			keywords_string = ""

			for keyword in video.keywords:
				keywords_string += f"{keyword}\n"

			keywords_file = open(f"keywords_{video.title}.txt".replace(":", ""), 'w')
			keywords_file.write(keywords_string)
			os.startfile(f"keywords_{video.title}.txt".replace(":", ""))

	def cut_audio(self, url, start, stop):
		video_title = self.download_audio(url)
		ffmpeg_extract_subclip(f"{video_title}.mp4", start, stop, targetname=f"cut_{video_title}.mp4")