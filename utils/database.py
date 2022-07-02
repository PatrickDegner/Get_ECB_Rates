import utils.scrapper
from utils.connectDB import DatabaseConnection

def create_db_table():
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('DROP TABLE IF EXISTS "DailyRates"')
        cursor.execute('CREATE TABLE IF NOT EXISTS "DailyRates"("Date" date , "Currency" text, "Rate" real)')


def add_daily_rates():
    create_db_table()
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        for i in utils.scrapper.stats:
            date = utils.scrapper.date
            currency = (i)
            rates = (utils.scrapper.stats[i])

            cursor.execute('INSERT INTO "DailyRates"("Date", "Currency", "Rate") VALUES (%s,%s,%s)', (date, currency, rates))


def get_rate(currency):
    with DatabaseConnection() as connection:
         cursor = connection.cursor()

         cursor.execute('Select * from "DailyRates" where "Currency" = %s', (currency,))
         rate = [{'Date': str(i[0]), 'Currency': i[1], 'Rate': i[2]} for i in cursor.fetchall()]

         return rate


def get_all_rates():
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('Select * from "DailyRates"')
        rates = ({'Date': str(i[0]), 'Currency': i[1], 'Rate': i[2]} for i in cursor.fetchall())

        return rates
