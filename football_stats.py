import requests
from bs4 import BeautifulSoup


def get_football_stats():
    url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?page=1"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables on the page
    tables = soup.find_all('table', {'class': 'data'})

    if not tables:
        print("Could not find any tables on the webpage.")
        return None

    players = []

    # Iterate through each table to find the relevant statistics table
    for table in tables:
        headers = table.find_all('th')
        header_texts = [header.text.strip() for header in headers]

        if 'PLAYER' in header_texts and 'TEAM' in header_texts and 'TD' in header_texts:
            # This table seems to contain the relevant statistics
            rows = table.find('tbody').find_all('tr')[:20]  # Top 20 players
            for row in rows:
                columns = row.find_all('td')
                player_name = columns[0].get_text(strip=True)
                position = columns[1].get_text(strip=True)
                team = columns[2].get_text(strip=True)
                touchdowns = columns[8].get_text(strip=True)

                player_info = {
                    'Player': player_name,
                    'Position': position,
                    'Team': team,
                    'Touchdowns': touchdowns
                }
                players.append(player_info)

            return players

    print("Could not find the relevant statistics table on the webpage.")
    return None


if __name__ == "__main__":
    football_stats = get_football_stats()

    if football_stats:
        print("Top 20 players by passing touchdowns:")
        for player in football_stats:
            print(player)
