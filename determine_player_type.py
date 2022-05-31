def determine_player_type(X) -> int:
    '''
    will determine type of player, and return either
    1,2,3 (1 = human, 2 = random, 3 = simple)
    '''
    while True:
        player_type = input(('Choose the type for Player {}\n'+ 'Enter Human or Random or Simple: ').format(X))

        player_type = player_type.strip()
        player_type = player_type.lower()                 # probaby not the most graceful way to do this but it works


        if player_type == 'h' or player_type == 'hu' or player_type == 'hum' or player_type == 'huma' or player_type == 'human':
            return 1
        elif player_type == 's' or player_type == 'si' or player_type =='sim' or player_type == 'simp' or player_type == 'simpl' or player_type == 'simple':
            return 3
        elif player_type == 'r' or player_type == 'ra' or player_type == 'ran' or player_type == 'rand' or player_type == 'rando' or player_type == 'random':
            return 2
        else:
           print('{} is not one of Human or Random or Simple. Please try again.'.format(player_type))

