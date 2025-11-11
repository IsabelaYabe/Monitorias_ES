from typing import Protocol

class ContentCreator(Protocol):
    def create_content(self) -> str: 
        ...

class Blogger(ContentCreator, Protocol):
    posts: list[str]

    def add_post(self, title: str, content: str) -> None:
        ...

class Vlogger(ContentCreator, Protocol):
    videos: list[str]

    def add_video(self, title: str, path: str) -> None:
        ...

class Vlog:
    def __init__(self):
        self.videos = []

    def add_video(self, title: str, path: str) -> None:
        pass

    def create_content(self) -> str:
        return ""
    
vlog: Vlogger = Vlog()