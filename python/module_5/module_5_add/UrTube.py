#!/usr/bin/env python3

import time
from User import User
from Video import Video

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        pass

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
        pass

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {user} уже существует.')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        pass

    def log_out(self):
        self.current_user = None
        pass

    def add(self, *videos):
        for video in videos:
            if isinstance(video, Video):
                for exist_video in self.videos:
                    if video == exist_video:
                        break
                else:
                    self.videos.append(video)
        pass

    def get_videos(self, search):
        find = []
        for video in self.videos:
            if search in video:
                find.append(video)
        return find
        pass

    def watch_video(self, title_video):
        if self.current_user:
            for exist_video in self.videos:
                if exist_video == title_video:
                    if exist_video.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        return

                    for i in range(1, exist_video.duration + 1):
                        print(i, end=" ")
                        time.sleep(1)
                        exist_video.time_now += 1

                    exist_video.time_now = 0
                    print("Конец видео")
                    break
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")
        pass
