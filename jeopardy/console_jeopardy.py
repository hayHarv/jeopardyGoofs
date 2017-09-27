#TODO add prompt for # of questions (and include final jeopardy?)
#TODO add timer

from random_clue import get_question, c, rows


def play(rows, sqlite_cursor):
    '''
    Shows one random question

    parameters
    ----------
    rows: int
        count of rows in jeopardy database
    sqlite_cursor:
        cursor to query database for question

    Returns
    ---------
    interactive question/answer
    '''
    cat, val, q, ans = get_question(rows, sqlite_cursor)
    user ='y' 
    if user == 'y':
        print("Category: {}".format(cat))
        print("Value: ${}".format(val))
        print("{}".format(q))
        user = input("Type [a] if you're ready for the answer: ")
        if user == 'a':
            print(ans)
            return ""


def keep_playing(rows, sqlite_cursor):
    play(rows, sqlite_cursor)
    user = input("play another? [y/n] ")
    if user == 'y':
       keep_playing(rows, sqlite_cursor)
    else:
        return ""

if __name__=="__main__":
    keep_playing(rows, c)
