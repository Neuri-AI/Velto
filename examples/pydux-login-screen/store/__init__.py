from velto.state import (
    configure_store,
    create_slice,
)
from velto.runtime import is_frozen

user_slice = create_slice(
    name="user",
    initial_state={
        "username": "",
        "password": "",
        "authenticated": False
    },
    reducers={
        "set_data": lambda state, action: state.update(action.payload)
    }
)

store = configure_store(
    {
        "user": user_slice
    },
    devtools=not is_frozen()
)