from classes import Team, Driver

teams = {}

with open("f1_points.csv", "r") as file:
    lines = file.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")

    driver_name = parts[0]
    team_name = parts[1]
    points = int(parts[2])

    driver = Driver(driver_name, points)

    if team_name not in teams:
        teams[team_name] = Team(team_name)

    teams[team_name].add_driver(driver)

sorted_teams = sorted(teams.values())

for team in sorted_teams:
    print(team)