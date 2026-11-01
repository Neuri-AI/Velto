from velto.ui import psx, component

@component
def RecentActivityItem(activity, time):
    return psx("""
        <div key={time} class="activity-item">
            <p class="activity-description">{activity}</p>
            <p class="activity-time">{time}</p>
        </div>
    """)