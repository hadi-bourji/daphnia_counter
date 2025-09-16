import tkinter as tk
import vlc

root = tk.Tk()
root.title("VLC Player")

instance = vlc.Instance()
player = instance.media_player_new()

media = instance.media_new("Basler_boA8100-16cc__40578090__20250815_164944800.mp4")
player.set_media(media)

# Video frame
video_frame = tk.Frame(root)
video_frame.pack(fill="both", expand=1)
player.set_hwnd(video_frame.winfo_id())


# Start playback
player.play()
root.mainloop()
