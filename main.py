from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    year, month, day = date[:4], date[4:6], date[6:]
    storage.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
    storage[year][month][day] += number
    return f"Added expense of {number} rubles for {date}"


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    if str(year) not in storage:
        return f"No expenses recorded for {year}"
    total = sum(sum(storage[str(year)][month].values()) for month in storage[str(year)])
    return f"Total expenses for {year}: {total} rubles"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    if str(year) not in storage or str(month) not in storage[str(year)]:
        return f"No expenses recorded for {year}-{month}"
    total = sum(storage[str(year)][str(month)].values())
    return f"Total expenses for {year}-{month}: {total} rubles"


if __name__ == "__main__":
    app.run(debug=True)
