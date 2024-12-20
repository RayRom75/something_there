#!/usr/bin/env python3
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        pass

    def __str__(self):
        return f"{self.nickname}"
        pass

    def __int__(self):
        return int(self.age)
        pass

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

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
