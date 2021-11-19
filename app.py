from moviepy.editor import VideoFileClip
import easygui
import numpy

def create_gif(start_time=0, end_time=0,new_name='output'):
    video = easygui.fileopenbox().replace('\\', '/')
    clip = (VideoFileClip(video).subclip(2).resize(0.6))
    return clip.write_gif(f"{new_name}.gif", loop=True)



if __name__ == "__main__":
    create_gif(new_name=input("Please name your file: "))
    