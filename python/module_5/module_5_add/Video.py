#!/usr/bin/env python3

class Video:

    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
        pass

    def __contains__(self, value):
        return value.lower() in self.title.lower()
        pass

    def __eq__(self, value):
        if isinstance(value, Video):
            return self.title == value.title

        if isinstance(value, str):
            return self.title == value
        pass

    def __repr__(self):
        return self.title
        pass
