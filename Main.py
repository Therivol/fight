from Game import Game


if __name__ == "__main__":
    game = Game()

    while game.is_running:
        game.calculate_delta_time()
        game.capture_input()
        game.early_update()
        game.update()
        game.late_update()
        game.draw()
