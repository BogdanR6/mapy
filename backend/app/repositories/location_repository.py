from sqlite3 import Row
from app.db.connection import get_connection
from app.models.location import Location

def save_location(location: Location) -> None:
    if location_exists(location.ip):
        return

    conn = get_connection()
    cur = conn.cursor()
    _ = cur.execute(
        "INSERT INTO locations (ip, name, lat, lon) VALUES (?, ?, ?, ?)",
        (location.ip, location.name, location.latitude, location.longitude)
    )
    conn.commit()
    conn.close()

def location_exists(ip: str) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    _ = cur.execute("SELECT COUNT(1) AS cnt FROM locations WHERE ip = ?", (ip,))

    row: Row | None = cur.fetchone()
    conn.close()

    return (row is not None) and (row["cnt"] > 0)


def get_all_locations() -> list[dict[str, float]]:
    conn = get_connection()
    cur = conn.cursor()
    _ = cur.execute("SELECT * FROM locations")
    rows: list[Row] = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]
