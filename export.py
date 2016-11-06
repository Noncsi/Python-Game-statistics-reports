import reports

file_name = 'game_stat.txt'
title = 'World of Warcraft'     #for example
total_copies_sold = '10'        #for example
year = '2000'                   #for example
genre = 'RPG'                   #for example
publisher = 'Valve Corporation' #for example

line0 = "Number of games: %s" % (reports.count_games(file_name))
line1 = "Is there a game from %s?: %s" %(year, reports.decide(file_name, year))
line2 = "%s is the latest game on the list." % (reports.get_latest(file_name))
line3 = "There is %s game with the genre %s" % (reports.count_by_genre(file_name, genre), genre)
line4 = "The %s game is in the %d-th line." % (title, reports.get_line_number_by_title(file_name, title))
text_list = [line1, line2, line3, line4]
with open("Judy's answers.txt", "w") as answertext:
    for k in range(len(text_list)):
        answertext.writelines(text_list[k]+"\n")

