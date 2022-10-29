
import pygame

pygame.font.init()

class Tile:
    """
    Represents a tile on the board.
    """

    COLORS = {
        'Black' : (0, 0, 0),
        'Brown' : (102, 51, 0),
        'LightBlue' : (153, 204, 255),
        'Pink' : (255, 153, 204),
        'Orange' : (255, 128, 0),
        'Red' : (255, 0, 0),
        'Yellow' : (255, 255, 51),
        'Green' : (0, 255, 0),
        'Blue' : (0, 128, 255)
    }

    WIDTH, HEIGHT = 70, 70  # Tile size

    FONT = pygame.font.SysFont('segoeui', 12, True)  # Tile font

    def __init__(self):
        """
        Initializes the tile.
        """
        self.name = "undefined tile"

    def draw(self, window: pygame.Surface, x: int, y: int):
        """
        Draws the tile onto a specified window.
        """
        pygame.draw.rect(
            window,
            self.COLORS['Black'],
            (x, y, self.WIDTH, self.HEIGHT),
            2
        )

        text = self.FONT.render( self.name, 1, self.COLORS['Black'] )
        window.blit( text, (
            x + self.WIDTH / 2 - text.get_width() / 2,
            y + self.HEIGHT / 2 - text.get_height() / 2
        ))
