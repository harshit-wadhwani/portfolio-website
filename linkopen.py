from bokeh.models.widgets import Div

def open_link(link):
    js = f"window.open({link})"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    return div
    