class Rating:
        def __init__(self,up,down):
                self.up=up
                self.down=down
        def __str__(self):
                return "Rating: 👍"+str(self.up)+" 👎"+str(self.down)
        def __gt__(self,m):
                return self.up-self.down > m.up-m.down
        def __lt__(self, m):
                return self.up-self.down < m.up-m.down
        def __eq__(self, m):
                return self.up-self.down == m.up-m.down
        def __add__(self, m):
                return self.up-self.down + m.up-m.down
        def __sub__(self, m):
                return self.up-self.down - m.up-m.down 
#########################################
video_1_rating= Rating(11111,22)
video_2_rating= Rating(11,22)
print(video_1_rating)
print(video_2_rating)
print(video_1_rating>video_2_rating)
print(video_1_rating<video_2_rating)
print(video_1_rating==video_2_rating)
print(video_1_rating-video_2_rating)
print(video_1_rating+video_2_rating)