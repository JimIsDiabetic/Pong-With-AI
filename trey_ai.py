prev_ball_frect = None
game_started = False
morphin_time = False
position_to_move_to = 0

def move_to_position(paddle_frect, position):
    if position > paddle_frect.pos[1] + paddle_frect.size[1] / 2:
        return "down"
    else:
        return "up"

def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    global game_started
    if not game_started:
        global prev_ball_frect
        prev_ball_frect = ball_frect
        game_started = True
        global morphin_time
        morphin_time = False
        global position_to_move_to
        position_to_move_to = 0

    if paddle_frect.pos[0] < table_size[0] / 2:
    # paddle on left side
        if ball_frect.pos[0] > prev_ball_frect.pos[0]:
            # ball moving from paddle
            morphin_time = False
            position_to_move_to = table_size[1] / 2
        else:
            # ball moving towards paddle
            if ball_frect.pos[0] < prev_ball_frect.pos[0] and ball_frect.pos[0] < other_paddle_frect.pos[0] - ball_frect.size[0] * 2:
                if not morphin_time:
                    multiverse_height = abs(((ball_frect.pos[0] - (paddle_frect.pos[0] + paddle_frect.size[0])) * (ball_frect.pos[1] - prev_ball_frect.pos[1])) / (ball_frect.pos[0] - prev_ball_frect.pos[0]))
                    morphin_time = True
                    if ball_frect.pos[1] > prev_ball_frect.pos[1]:
                        # ball starting going down
                        if (multiverse_height - (table_size[1] - ball_frect.pos[1])) % (table_size[1] * 2) < table_size[1]:
                            # ball going opposite direction from start
                            position_to_move_to = table_size[1] - ((multiverse_height - (table_size[1] - ball_frect.pos[1])) % (table_size[1] * 2))
                        else:
                            # ball going same direction from start
                            if multiverse_height + ball_frect.pos[1] > table_size[1]:
                                position_to_move_to = (multiverse_height - (table_size[1] - ball_frect.pos[1])) % (table_size[1])
                            else:
                                position_to_move_to = None
                    else:
                        # ball starting going up
                        if (multiverse_height - ball_frect.pos[1]) % (table_size[1] * 2) < table_size[1]:
                            # ball going opposite direction from start
                            position_to_move_to = (multiverse_height - ball_frect.pos[1]) % (table_size[1] * 2)
                        else:
                            # ball going same direction from start
                            if multiverse_height > ball_frect.pos[1]:
                                position_to_move_to = table_size[1] - ((multiverse_height - ball_frect.pos[1]) % (table_size[1]))
                            else:
                                position_to_move_to = None
    else:
        # paddle on right side
        if ball_frect.pos[0] < prev_ball_frect.pos[0]:
            # ball moving from paddle
            morphin_time = False
            position_to_move_to = table_size[1] / 2
        else:
            # ball moving towards paddle
            if ball_frect.pos[0] > prev_ball_frect.pos[0] and ball_frect.pos[0] > other_paddle_frect.pos[0] + other_paddle_frect.size[0] + ball_frect.size[0] * 2:
                if not morphin_time:
                    multiverse_height = abs(((paddle_frect.pos[0] - ball_frect.pos[0]) * (ball_frect.pos[1] - prev_ball_frect.pos[1])) / (ball_frect.pos[0] - prev_ball_frect.pos[0]))
                    morphin_time = True
                    if ball_frect.pos[1] > prev_ball_frect.pos[1]:
                        # ball starting going down
                        if (multiverse_height - (table_size[1] - ball_frect.pos[1])) % (table_size[1] * 2) < table_size[1]:
                            # ball going opposite direction from start
                            position_to_move_to = table_size[1] - ((multiverse_height - (table_size[1] - ball_frect.pos[1])) % (table_size[1] * 2))
                        else:
                            # ball going same direction from start
                            if multiverse_height + ball_frect.pos[1] > table_size[1]:
                                position_to_move_to = (multiverse_height - (table_size[1] - ball_frect.pos[1])) % (table_size[1])
                            else:
                                position_to_move_to = None
                    else:
                        # ball starting going up
                        if (multiverse_height - ball_frect.pos[1]) % (table_size[1] * 2) < table_size[1]:
                            # ball going opposite direction from start
                            position_to_move_to = (multiverse_height - ball_frect.pos[1]) % (table_size[1] * 2)
                        else:
                            # ball going same direction from start
                            if multiverse_height > ball_frect.pos[1]:
                                position_to_move_to = table_size[1] - ((multiverse_height - ball_frect.pos[1]) % (table_size[1]))
                            else:
                                position_to_move_to = None

    prev_ball_frect = ball_frect
    if position_to_move_to != None:
        return move_to_position(paddle_frect, position_to_move_to)
    else:
        return move_to_position(paddle_frect, ball_frect.pos[1])