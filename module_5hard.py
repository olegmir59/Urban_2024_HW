# Дополнительное практическое задание по модулю: "Классы и объекты."
# Задание "Свой YouTube":

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        #self.password = hash((self.age, self.nickname))


    def __eq__(self, other):
        return self.age == other.age and self.nickname == other.nickname
    def __hash__(self):
        return hash((self.age, self.nickname))

user = User("Aaaa","rrrr",25 )
print("The hash is: %d" % hash(user))
print("Password is: %d" % user.password)




class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def  log_in(self,nickname, password):
        for user_Tube in self.users:
            if nickname == user_Tube.nickname and hash(password) == user_Tube.password:
                self.current_user = user_Tube
    def add(self, *args):
        for vid_in in args:
            if vid_in not in self.videos:
                self.videos.append(vid_in)



ur = UrTube([],[], None )
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