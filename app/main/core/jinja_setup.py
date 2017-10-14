from babel.dates import format_date, format_datetime
from ..main import app

def jinja_prettydate(value):
    return format_date(value, format='long', locale='nl')

def jinja_datetime(value):
    return format_datetime(value, 'yyyy-MM-dd')

app.jinja_env.filters['prettydate'] = jinja_prettydate
app.jinja_env.filters['datetime'] = jinja_datetime
