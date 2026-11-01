from velto.ui import psx, component

@component
def InfoCard(title, value):
    return psx("""
        <GridItem span={{"base": 12, "sm": 4, "md": 3}}>
            <div class="card">
                <p class="card-title">{title}</p>
                <p class="card-value">{value}</p>
            </div>
        </GridItem>
    """)