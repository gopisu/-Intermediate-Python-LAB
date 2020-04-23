projects = ["Brexit", "Nord Stream", "US Mexico Border"]
leaders = ["Theresa May", "Wladimir Putin", "Donald Trump and Bill Clinton"]
dates = ["2016-06-23", "2016-08-29", "1994-01-01"]

for project, leader in zip(projects, leaders):
    print("The leader of", project, "is", leader)

for project, date, leader in zip(projects, dates, leaders):
    print("The leader of", project, "started", date, "is", leader)

for pos, (project, date, leader) in enumerate(zip(projects, dates, leaders)):
    print(pos, "The leader of", project, "started", date, "is", leader)
