import os, sys, tkinter, tkinter.filedialog, tkinter.messagebox, ffmpeg, json

root = tkinter.Tk()
root.withdraw()

fTyp = [("",".webm .mkv .mp4")]
iDir = os.path.abspath(os.path.dirname(__file__))
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
filename = os.path.splitext(file)[0]
file_ext = os.path.splitext(file)[1][1:]

if len(file) == 0:
    tkinter.messagebox.showerror('エラー', 'ファイルが選択されていません')
    sys.exit()

if file_ext == "mkv":
    (
    ffmpeg
    .input(file)
    .output(filename+".mp4", vcodec='copy')
    .overwrite_output()
    .run()
    )

elif file_ext == "webm":
    (
    ffmpeg
    .input(file)
    .output(filename+".mp4")
    .overwrite_output()
    .run()
    )

elif file_ext == "mp4":
    (
    ffmpeg
    .input(file)
    .output(filename+".mp3", acodec="libmp3lame", ab="128k")
    .overwrite_output()
    .run()
    )
