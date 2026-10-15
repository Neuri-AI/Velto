"""FocusBoard stage 06: a Pydux slice with a PSX provider."""
from velto.state import configure_store, create_slice
from velto.ui import App, StoreProvider, component, psx, use_dispatch, use_selector


tasks = create_slice(
    name="tasks",
    initial_state={"count": 0},
    reducers={"add": lambda state, action: state.update({"count": state["count"] + 1})},
)
store = configure_store({"tasks": tasks}, devtools=False)


@component
def FocusBoard():
    count = use_selector(lambda state: state["tasks"]["count"])
    dispatch = use_dispatch()
    return psx('<Flex direction="column" gap="8"><Text value={count} /><Button label="Add task" on_click={add_task} /></Flex>', scope={"count": count, "add_task": lambda: dispatch(tasks.actions.add())})


def build():
    return StoreProvider(store, FocusBoard())


if __name__ == "__main__":
    App(build(), renderer="headless").mount()
