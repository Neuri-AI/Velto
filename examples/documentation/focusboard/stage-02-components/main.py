"""FocusBoard stage 02: reusable components and composition."""
from velto.ui import App, component, psx


@component
def TaskTitle(title: str):
    return psx('<Text value={title} />', scope={"title": title})


@component
def FocusBoard():
    return psx('<Flex direction="column" gap="8"><Text value="FocusBoard" /><TaskTitle title="Plan the week" /></Flex>', scope={"TaskTitle": TaskTitle})


def build():
    return FocusBoard()


if __name__ == "__main__":
    App(build(), renderer="headless").mount()
