from velto.ui import psx, component

@component
def Sidebar(btns, active_tab, set_active_tab):
    return psx("""
        <div class="sidebar">
            <h5>Mi panel</h5>

            <div class="sidebar-content">
                {btns.map((button, index) => (
                    <button
                        key={index}
                        class={active_tab == button ? "active" : ""}
                        on_click={() => set_active_tab(button)}
                    >
                        {button}
                    </button>
                ))}
            </div>
        </div>
    """)