import sys

game_mode_player_count = {
    "Y": 2,  # "Y" 모드는 2명 필요
    "F": 3,  # "F" 모드는 3명 필요
    "O": 4   # "O" 모드는 4명 필요
}

total_players, game_mode = input().split()
unique_players = set()
required_players = game_mode_player_count[game_mode]
current_group_size = 0
completed_games = 0

for _ in range(int(total_players)):
    player_name = sys.stdin.readline().rstrip()
    if player_name in unique_players:
        continue
    current_group_size += 1
    unique_players.add(player_name)

    if required_players == current_group_size + 1:
        completed_games += 1
        current_group_size = 0

print(completed_games)