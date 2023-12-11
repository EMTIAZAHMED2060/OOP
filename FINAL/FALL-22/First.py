class Netflix:
    shows = []

    def __init__(self, name, genres, episodes=10):
        self.name = name
        self.genres = genres
        self.episodes = episodes
        Netflix.shows.append(self)

    @staticmethod
    def printDetails():
        print("Total number of shows:", len(Netflix.shows))
        for show in Netflix.shows:
            print(f"Show name: {show.name}\nEpisodes: {show.episodes}\nGenre: {', '.join(show.genres)}")
            print("===================")

s1 = Netflix("Wednesday", ["Mystery", "Supernatural"], 15)
print("==========1==========")
s2 = Netflix("Dark", ["Mind-Bending", "Sci-fi"])
print("==========2==========")
Netflix.printDetails()
s3 = Netflix("Suits", ["Comedy", "Courtroom"], 20)
print("==========3==========")
s4 = Netflix("Demon Slayer", ["Anime"], 22)
print("==========4==========")
Netflix.printDetails()
