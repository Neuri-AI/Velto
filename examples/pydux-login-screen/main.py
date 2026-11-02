import sys
from velto import VeltoContext
from velto.ui import psx, use_state
from store import store, user_slice
from velto.state import use_dispatch, use_selector

class PyduxExample(VeltoContext):

    def render(self):
        auth, set_auth = use_state({
            "username": "",
            "password": ""
        })
        error, set_error = use_state({
            "show": False,
            "message": ""
        })
        dispatch = use_dispatch()
        authenticated = use_selector(lambda state: state["user"]["authenticated"])


        def handle_submit():
            if not auth["username"] or not auth["password"]:
                set_error({
                    "show": True,
                    "message": "Username and password are required"
                })
                return

            set_error({
                "show": False,
                "message": ""
            })

            dispatch(user_slice.actions.set_data({**auth, "authenticated": True}))

        def handle_input_change(e):
            set_auth({**auth, e.target.name: e.target.value})

        return psx("""
            <div>
                <link rel="stylesheet" href="css/styles.css"/>
                <div class="root">
                    <div class="header">
                        <h1>Sign In</h1>
                        <span>Please sign in to continue</span>
                    </div>

                    {
                        error.show
                            ? <div class="error">{error.message}</div>
                            : authenticated
                                ? <div class="success">Successfully authenticated</div>
                                : <></>
                    }

                    <form on_submit={handle_submit}>
                        <input type="text" name="username" placeholder="Username" value={auth.username} on_change={handle_input_change}/>
                        <input type="password" name="password" placeholder="Password" value={auth.password} on_change={handle_input_change}/>
                        <button type="submit">Sign In</button>
                    </form>
                    <a href="https://example.com/forgot-password">Forgot your password?</a>
                </div>
            </div>
        """)

if __name__ == "__main__":
    sys.exit(PyduxExample().run())
