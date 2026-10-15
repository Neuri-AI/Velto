"""FocusBoard stage 05: layout with Flex, Scroll, and Grid."""
from velto.ui import App, Grid, GridItem, Text, component, psx


@component
def FocusBoard():
    return psx('''<Flex direction="column" gap="12"><Scroll height="320"><Flex direction="column" gap="8"><Text value="Inbox" /><Text value="Today" /></Flex></Scroll></Flex>''')


def grid_layout():
    """Build the verified Grid contract for a renderer-specific content root."""
    return Grid(GridItem(Text("Inbox"), span=6), GridItem(Text("Today"), span=6), gap=12)


def build():
    return FocusBoard()


if __name__ == "__main__":
    App(build(), renderer="headless").mount()
