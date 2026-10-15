"""FocusBoard stage 03: local state and an event callback."""
from velto.ui import App, component, psx, use_state


@component
def FocusBoard():
    count, set_count = use_state(0)

    def add_task():
        set_count(lambda current: current + 1)

    return psx('<Flex direction="column" gap="8"><Text value={count} /><Button label="Add task" on_click={add_task} /></Flex>', scope={"count": count, "add_task": add_task})


def build():
    return FocusBoard()


if __name__ == "__main__":
    App(build(), renderer="headless").mount()
