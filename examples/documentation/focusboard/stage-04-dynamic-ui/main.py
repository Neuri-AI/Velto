"""FocusBoard stage 04: conditions, lists, keys, and fragments."""
from velto.ui import App, component, psx


@component
def FocusBoard():
    tasks = ({"id": "a", "title": "Plan"}, {"id": "b", "title": "Write"})
    return psx("""<Flex direction="column" gap="8">{tasks.map((task) => <Text key={task.id} value={task.title} />)}</Flex>""")


def build():
    return FocusBoard()


if __name__ == "__main__":
    App(build(), renderer="headless").mount()
