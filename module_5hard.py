# Дополнительное практическое задание по модулю: "Классы и объекты."
# Задание "Свой YouTube":

import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
            return self.nickname + ' ' + str(self.password) + ' age: ' + str(self.age)

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user_ in self.users:
            #  print("log_in")
            #  print(user_)
            if (nickname == user_.nickname and hash(password) == user_.password):
                self.current_user = user_
            #    print("log_in  пользователь  найден:", user_)
            else:
                print("** log_in**  Пользователь с указанным паролем не найден!  ", nickname, "Зарегистрируйтесь!")


    def register(self, nickname, password, age):
        if nickname in self.users:
            print("Пользователь ", nickname, " уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            print("Пользователь ", nickname, " добавлен в список")
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта, чтобы смотреть видео войдите снова")

    def add(self, *args):
        for vid_in in args:
            if vid_in.title not in self.videos:
                self.videos.append(vid_in)
        print("после добавления видео:")
        for i in self.videos:
            print(i.title)

    def get_videos(self, find_string):
        videos_list = []
        for vid_in in self.videos:
            if str(find_string).lower() in str(vid_in.title).lower():
                videos_list.append(vid_in.title)
                print("нашли видео, где в Названии есть: ", find_string)
            else:
                print("Не нашли видео, где в Названии есть: ", find_string)
            return videos_list

    def watch_video(self, find_string):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return -1
        elif self.current_user.age <= 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return 0
        else:
            for vid_in in self.videos:
                if str(find_string).lower() == str(vid_in.title).lower():
                     print("нашли видео по запросу: ", find_string)
                     print("\n =====  Старт видео  ==== Приятного просмотра ! =====")
                     for i in range(vid_in.duration):
                         time.sleep(1)
                         print(" ", i,  end="")
                     print("\n =================== Конец видео=====================")
                     return 1
            print("Не нашли видео по запросу:: ", find_string)


ur = UrTube([],[], None )
#  print(ur)

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(*ur.get_videos('2024'))
print(*ur.get_videos('лучший'))
print(*ur.get_videos('худший'))
print(*ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')

ur.log_in('vasya_pupkin', 'lolkek')
ur.log_in('vasya_pupkin', 'lolkekcheburek')


ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
print(ur.current_user)
ur.watch_video('Для чего девушкам парень программист?')
ur.log_out()

# Проверка входа в другой аккаунт.  Вася не дурак!
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Для чего девушкам парень программист?')

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
