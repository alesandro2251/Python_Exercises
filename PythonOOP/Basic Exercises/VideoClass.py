# // Create the constructor function for a Video object. The function should take
# //     in arguments of title (a string), uploader (a string, the person who uploaded it),
# //      and seconds (a number, the duration), and it should save them as properties of the object.
# // Create a method on the Video object called watch(). When that method is called,
# //     it should use console.log to output a string like "You watched all 60 seconds of Otters Holding Hands!"
# // Instantiate a new Video object and call the watch() method on it.
# // Instantiate another Video object with different constructor arguments.


class Video:
    def __init__(self, title, uploader, seconds, ):
        self.title = title
        self.uploader = uploader
        self.seconds = seconds

    def watch(self):
        print(f"{self.uploader} watched all {self.seconds} seconds of {self.title}!")


video = Video("Lord of the rings", "Steven", 60)
video.watch()
