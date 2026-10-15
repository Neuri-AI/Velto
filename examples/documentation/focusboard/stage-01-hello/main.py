"""FocusBoard stage 01: a headless hello screen."""
from velto.ui import App, component, psx


@component
def FocusBoard():
    return psx('<Flex direction="column" gap="8"><Text value="FocusBoard" /><Text value="Your calm task list" /></Flex>')


def build():
    return FocusBoard()


if __name__ == "__main__":
    App(build(), renderer="headless").mount()
