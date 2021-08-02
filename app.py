import requests
import sys


def requestPlayers():
    """Request all players to the URL provided"""
    return requests.get('https://mach-eight.uc.r.appspot.com/').json()


def mapPlayers(playerList):
    """Map the requested list of dicts to a new dict"""
    heightsList = {}
    for player in playerList['values']:
        if heightsList.get(player.get('h_in')):
            heightsList[player['h_in']].append(player)
        else:
            heightsList[player['h_in']] = [player]
    return heightsList


def main():
    """Get pairs of players whose heght sums up to input number"""
    checkedPlayers = []
    found = False

    if len(sys.argv) < 2:
        print('No arguments passed')
        return False
    else:
        try:
            maxHeight = int(sys.argv[1])
        except:
            print('Argument passed is not an integer')
            return False

    playerList = requestPlayers()

    heightsList = mapPlayers(playerList)

    # Search for each player's pair
    for player in playerList['values']:
        delta = maxHeight - int(player['h_in'])
        idealPlayers = heightsList.get(str(delta))
        if idealPlayers:
            found = True
            for idealPlayer in idealPlayers:
                if idealPlayer not in checkedPlayers:
                    print('- {} {}    {} {}'.format(
                        player['first_name'], player['last_name'],
                        idealPlayer['first_name'], idealPlayer['last_name']))
            checkedPlayers.append(player)

    if not found:
        print('No matches found')
        return False

    return True


if __name__ == '__main__':
    main()
