#1. question
def count_games(file_name): 
    with open(file_name) as f:        
        return sum(1 for _ in f)


#2. question
def decide(file_name, year): 
    with open((file_name), 'r') as f:
        line_list = f.readlines() #transforms the lines into lists.
        exist = False
    for k in range(len(line_list)):
        line_list[k] = (line_list[k]).split('\t') #to split the words that are seperated with tabs
    for l in range(len(line_list)):
        if year == int(line_list[l][2]):
            return True
    return False
             

#3. question
def get_latest(file_name): 
    with open((file_name), 'r') as f:
        line_list = f.readlines() #transforms the lines into lists.
    for k in range(len(line_list)):
        line_list[k] = (line_list[k]).split('\t') #to split the words that are seperated with tabs
    latest = 0
    for l in range(len(line_list)):
        if latest < int(line_list[l][2]): #[2] = release date
            latest = int(line_list[l][2])
            latest_name = line_list[l][0] #[0] = name of the game
    return latest_name


#4. question
def count_by_genre(file_name,genre):
    with open((file_name), 'r') as f:
        line_list = f.readlines() #transforms the lines into lists.
    for k in range(len(line_list)):
        line_list[k] = (line_list[k]).split('\t') #to split the words that are seperated with tabs
    count = 0
    for l in range(len(line_list)):
        if genre == line_list[l][3]: #[3] = genre
            count += 1
    return count


#5. question
def get_line_number_by_title(file_name,title): 
        with open((file_name), 'r') as f:
            line_list = f.readlines() #transforms the lines into lists.
        for k in range(len(line_list)):
            line_list[k] = (line_list[k]).split('\t') #to split the words that are seperated with tabs
            if (title.lower()).replace(" ", "") == (line_list[k][0].lower()).replace(" ", ""):
                return k+1
    #except ValueError:
        #print ("There is no game with the given title.")




#bonus questions
#def sort_abc(file_name)


#def get_genres(file_name)


#def when_was_top_sold_fps(file_name)


# count_games('game_stat.txt')
# decide ('game_stat.txt', '2000')
# get_latest('game_stat.txt')
# count_by_genre('game_stat.txt', 'First-person shooter')
#get_line_number_by_title('game_stat.txt','Goat Simulator')