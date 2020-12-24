import pandas as pd
import datetime
import matplotlib

DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
WEEKLY_BUY_USD = 100

def seperate_into_weekdays(historical_data, start_date=datetime.datetime(2013, 9, 30), end_date=datetime.datetime.today()):
    '''Seperate historical data into days of week for intended time period'''
    period_data = historical_data.loc[(start_date <= historical_data['Date']) & (historical_data['Date'] <= end_date)]
    day_of_week_charts = {}
    for day in DAYS_OF_WEEK:
        day_data = period_data.loc[period_data['week_day'] == day].copy()
        day_data['total_btc_at_highest_cost'] = day_data.btc_at_highest_cost.cumsum()
        day_data['total_btc_at_lowest_cost'] = day_data.btc_at_lowest_cost.cumsum()
        day_data['total_btc_at_average_cost'] = day_data.btc_at_average_cost.cumsum()
        day_of_week_charts[day] = day_data
    return day_of_week_charts

def get_totals(day_of_week_charts):
    " get cumulutive sums"
    day_of_week_max = {}
    for day in DAYS_OF_WEEK:
        day_data = day_of_week_charts[day]
        day_of_week_max[day] = {'start': day_data.Date.min().date(),
                                'total_btc_at_lowest_cost': day_data.total_btc_at_lowest_cost.max(),
                                'total_btc_at_average_cost': day_data.total_btc_at_average_cost.max(),
                                'total_btc_at_highest_cost': day_data.total_btc_at_highest_cost.max()}
    day_of_week_max = pd.DataFrame(day_of_week_max)
    day_of_week_max_transposed = day_of_week_max.T
    return day_of_week_max_transposed

def get_average(day_of_week_charts):
    " get average purchases"
    day_of_week_average = {}
    for day in DAYS_OF_WEEK:
        day_data = day_of_week_charts[day]
        day_of_week_average[day] = {'start': day_data.Date.min().date(),
                                    'average_btc_at_lowest_cost': day_data.btc_at_lowest_cost.mean(),
                                    'average_btc_at_average_cost': day_data.btc_at_average_cost.mean(),
                                    'average_btc_at_highest_cost': day_data.btc_at_highest_cost.mean()}
    day_of_week_average = pd.DataFrame(day_of_week_average)
    day_of_week_average_transposed = day_of_week_average.T
    return day_of_week_average_transposed

def plot_range(day_of_week_vals, title):
    '''Bar plot for high, average and low cost'''
    plt = day_of_week_vals.plot.bar(title=f'{title} from weekly auto-buys of ${WEEKLY_BUY_USD} since week of {day_of_week_vals.start.min()}')
    plt.set_xlabel('Day of Week')
    plt.set_ylabel('BTC')
    plt.legend(loc='lower center')

def show_df(day_of_week_vals):
    '''Show df with coloring'''
    columns = list(day_of_week_vals.columns)
    columns.remove('start')
    day_of_week_vals = day_of_week_vals.style.background_gradient(cmap='Greens', subset=columns)
    return day_of_week_vals

