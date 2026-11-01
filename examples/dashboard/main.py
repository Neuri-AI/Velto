import sys
from velto import VeltoContext
from velto.ui import psx, use_state, use_effect, component
from components.sidebar import Sidebar
from components.recent_activity import RecentActivityItem
from components.info_card import InfoCard

class MyApp(VeltoContext):

    def render(self):
        active_tab, set_active_tab = use_state("Resumen")

        btns = ["Resumen", "Usuarios", "Reportes", "Configuración"]

        cards = [
            {"title": "Usuarios", "value": "1,248"},
            {"title": "Ventas", "value": "$3,456"},
            {"title": "Pedidos", "value": "356"},
            {"title": "Pendientes", "value": "12"}
        ]

        activity = [
            {"time": "23 de Octubre", "activity": "Ana López creó un reporte"},
            {"time": "23 de Octubre", "activity": "Carlos Pérez actualizó un pedido"},
            {"time": "23 de Octubre", "activity": "María Gómez eliminó un usuario"},
        ]

        use_effect(lambda: print(f"Active tab changed to: {active_tab}"), [active_tab])

        return psx("""
            <div class="layout">
                <link rel="stylesheet" href="css/styles.css" />
                <Grid gap="0px">
                    <GridItem span={{"base": 3, "md": 3, "lg": 2}}>
                        <Sidebar btns={btns} active_tab={active_tab} set_active_tab={set_active_tab} />
                    </GridItem>


                <Scroll direction="vertical" height="100vh">
                    <GridItem>
                        <div class="content">
                            <div class="flex header">
                                <p class="bold">{active_tab}</p>
                                <p class="greetings">Hola, Fredo</p>
                            </div>

                            <div class="container">
                                <Grid gap="16px">
                                    {cards.map((card, index) => (
                                        <InfoCard title={card["title"]} value={card["value"]} key={index} />
                                    ))}
                                </Grid>
                            </div>

                            <div class="container">
                                <div class="activity-card">
                                    <h5 class="prueba">Actividad Reciente</h5>

                                    {activity.map((item, index) => (
                                        <RecentActivityItem activity={item["activity"]} time={item["time"]} key={index} />
                                    ))}
                                </div>
                            </div>
                        </div>
                    </GridItem>
                </Scroll>
                </Grid>
            </div>
        """)


if __name__ == "__main__":
    app = MyApp()
    sys.exit(app.run())