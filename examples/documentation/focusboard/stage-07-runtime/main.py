"""FocusBoard stage 07: runtime facts supplied by Qyro."""
from velto.runtime import is_frozen
from velto.ui import App, component, psx


@component
def FocusBoard():
    mode = "frozen" if is_frozen() else "development"
    return psx('<Flex direction="column"><Text value="FocusBoard" /><Text value={mode} /></Flex>', scope={"mode": mode})


def build():
    return FocusBoard()


if __name__ == "__main__":
    App(build(), renderer="headless").mount()
