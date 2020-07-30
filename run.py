from sel import sel
from plot import Plot
import const

data = []
plot = Plot()

# getting data

try:
    sel = sel()
    # sel.go_to_page(const.FANTASY_LEAGUE_URL)
    # cur_week = sel.get_current_week(const.week_xpath)
    # print("Current week: " + str(sel.get_current_week(const.week_xpath)))
    # number_of_teams = sel.get_team_number(const.team_number)
    # overall_points_list = {}
    # week = 1
    # while week is not 5:
    #     print(week)
    #     team_result = {}
    #     team_num = 1
    #     w_result = []
    #
    #     while team_num is not number_of_teams + 1:
    #         t_result = {}
    #         team = sel.read_team("//table[@class='stat-table']/tbody/tr[{0}]/td[3]".format(team_num))
    #         week_points = sel.read_sum_points("//table[@class='stat-table']/tbody/tr[{}]/td[5]".format(team_num))
    #         #overall_points = sel.read_sum_points("//table[@class='stat-table']/tbody/tr[{}]/td[6]".format(team_num))
    #
    #         t_result["week"] = week
    #         t_result["team"] = team
    #         t_result["week_points"] = week_points
    #
    #         team_num += 1
    #         print(str(t_result))
    #         w_result.append(t_result)
    #     week += 1
    #     data.append(w_result)
    #     sel.go_to_page(const.FANTASY_LEAGUE_URL + "?num=" + str(week))
    #
    # print("Finish")
    #
    # sel.write_file(data)
    data = sel.read_file("data.json")
    # calc
    #data.reverse()
    for week in data:
        points = []
        teams = []

        team_points_list = []

        for index, results in enumerate(week):
            teams.append(results['team'])
            if results['week'] is not 1:
                results['overall_points'] = data[results['week']-2][index-1]['overall_points'] + results['week_points']

            else:
                results['overall_points'] = results['week_points']
            points.append(results['overall_points'])

        print(teams)
        print(points)

        points, teams = sel.sort_two_lists(teams, points)
        plot.show_plot(teams, points)
        print("hehe")

    # creating plot
    for week in data:

        points = []
        teams = []
        for results in week:
            teams.append(results['team'])
            points.append(results['overall_points'])
        print(teams)
        print(points)
    teams, points = sel.sort_two_lists(points, teams)
    plot.show_plot(teams, points)
    print("hehe")


finally:
    sel.teardown()
