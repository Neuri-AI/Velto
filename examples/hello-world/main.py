import sys
from velto import VeltoContext
from velto.ui import psx, use_state

class Test(VeltoContext):

    def render(self):
        count, set_count = use_state(0)
        tree = psx("""
            <>
                <link rel="stylesheet" href="css/styles.css"/>
                <div class="root">
                    <img src="images/logo.svg"/>

                    <h1>Get started</h1>
                    <p>Edit <span>main.py</span> and save to test HMR</p>

                    <button on_click={() => set_count(count + 1)}>Count is {count}</button>

                    <a href="https://getvelto.dev">Explore the docs</a>
                </div>
            </>
        """)
        print(tree)
        return tree

if __name__ == "__main__":
    sys.exit(Test().run())
