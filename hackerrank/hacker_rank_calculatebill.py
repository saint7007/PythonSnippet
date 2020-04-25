
import datetime
import calendar

def bill_for(month, active_subscription, users):
    # your code here!
    date_time_str = month + '-01'
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
    start_day_of_month = first_day_of_month(date_time_obj)
    end_day_of_month = last_day_of_month(date_time_obj)
    user_daily_charge = []

    for user in users:
        #user_daily_charge = []
        print(user["activated_on"])
        if (user["activated_on"] < date_time_obj.date()):
            print("old user")
            for day in range(start_day_of_month.day, end_day_of_month.day + 1):
                daily_charge = active_subscription["monthly_price_in_dollars"] / (
                            (end_day_of_month.day - start_day_of_month.day) + 1)
                print(daily_charge)
                user_daily_charge.append(daily_charge)
        else:
            print("new user")
            for day in range(user["activated_on"].day, end_day_of_month.day + 1):
                daily_charge = active_subscription["monthly_price_in_dollars"] / (
                            (end_day_of_month.day - start_day_of_month.day) + 1)
                print(daily_charge)
                user_daily_charge.append(daily_charge)

    sum = 0
   # print("len(user_daily_charge)")
    #print(len(user_daily_charge))
    for i in range(0, len(user_daily_charge)):
       # print(user_daily_charge[i])
        #print("sum + = " +str(sum))

        sum = sum + user_daily_charge[i];

    return sum;


def first_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the first day of that month. For example:

    >>> first_day_of_month(datetime.date(2019, 2, 7))  # Feb 7
    datetime.date(2019, 2, 1)                          # Feb 1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date.replace(day=1)


def last_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the last day of that month. For example:

    # >>> last_day_of_month(datetime.date(2019, 2, 7))  # Feb  7
    # datetime.date(2019, 2, 28)                        # Feb 28

    Input type: datetime.date
    Output type: datetime.date
    """
    last_day = calendar.monthrange(date.year, date.month)[1]
    return datetime.date(date.year, date.month, last_day)


def next_day(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the next day. For example:

    # >>> next_day(datetime.date(2019, 2, 7))   # Feb 7
    # datetime.date(2019, 2, 8)                 # Feb 8
    # 
    # >>> next_day(datetime.date(2019, 2, 28))  # Feb 28
    datetime.date(2019, 3, 1)                 # Mar  1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date + datetime.timedelta(days=1)


#---------------------------------------------------------------

user_signed_up = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 3,
        'name': 'Employee #3',
        'activated_on': datetime.date(2019, 1, 10),
        'deactivated_on': None,
        'customer_id': 1,
    },
]

new_plan = {
    'id': 1,
    'customer_id': 1,
    'monthly_price_in_dollars': 4
}

constant_users=[
  {
    'id': 1,
    'name': 'Employee #1',
    'customer_id': 1,

    # when this user started
    'activated_on': datetime.date(2018, 11, 4),

    # last day to bill for user
    # should bill up to and including this date
    # since user had some access on this date
    'deactivated_on': datetime.date(2019, 1, 10)
  },
  {
    'id': 2,
    'name': 'Employee #2',
    'customer_id': 1,

    # when this user started
    'activated_on': datetime.date(2018, 12, 4),

    # hasn't been deactivated yet
    'deactivated_on': None
  }
]

no_users=[]


cost1=bill_for('2019-01', new_plan, user_signed_up)
print("test case 1")
print(cost1)
cost2=bill_for('2019-01', new_plan, constant_users)
print("test case 2")
print(cost2)
cost3=bill_for('2019-01', new_plan, no_users)
print("test case 3")
print(cost3)

import datetime
import calendar


def bill_for(month, active_subscription, users):
    # your code here!
    date_time_str = month + '-01'
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
    start_day_of_month = first_day_of_month(date_time_obj)
    end_day_of_month = last_day_of_month(date_time_obj)
    users_daily_charge = []

    for user in users:
        user_daily_charge = []
        print(user["activated_on"])
        if (user["activated_on"] < date_time_obj.date()):
            print("old user")
            for day in range(start_day_of_month.day, end_day_of_month.day + 1):
                daily_charge = active_subscription["monthly_price_in_dollars"] / (
                            (end_day_of_month.day - start_day_of_month.day) + 1)
                print(daily_charge)
                user_daily_charge.append(round(daily_charge, 2))
        else:
            print("new user")
            for day in range(user["activated_on"].day, end_day_of_month.day + 1):
                daily_charge = active_subscription["monthly_price_in_dollars"] / (
                            (user["activated_on"].day - start_day_of_month.day) + 1)
                print(daily_charge)
                user_daily_charge.append(round(daily_charge, 2))

    sum = 0
    for i in range(0, len(user_daily_charge)):
        print(user_daily_charge[i])
        sum = sum + user_daily_charge[i];

    return sum;


####################
# Helper functions #
####################

def first_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the first day of that month. For example:

    >>> first_day_of_month(datetime.date(2019, 2, 7))  # Feb 7
    datetime.date(2019, 2, 1)                          # Feb 1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date.replace(day=1)


def last_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the last day of that month. For example:

    >>> last_day_of_month(datetime.date(2019, 2, 7))  # Feb  7
    datetime.date(2019, 2, 28)                        # Feb 28

    Input type: datetime.date
    Output type: datetime.date
    """
    last_day = calendar.monthrange(date.year, date.month)[1]
    return datetime.date(date.year, date.month, last_day)


def next_day(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the next day. For example:

    >>> next_day(datetime.date(2019, 2, 7))   # Feb 7
    datetime.date(2019, 2, 8)                 # Feb 8

    >>> next_day(datetime.date(2019, 2, 28))  # Feb 28
    datetime.date(2019, 3, 1)                 # Mar  1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date + datetime.timedelta(days=1)


#---------------------------------------------------------------

import unittest

user_signed_up = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 3,
        'name': 'Employee #3',
        'activated_on': datetime.date(2019, 1, 10),
        'deactivated_on': None,
        'customer_id': 1,
    },
]

constant_users = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
]

new_plan = {
    'id': 1,
    'customer_id': 1,
    'monthly_price_in_dollars': 4
}

no_users = []


# Note: the class must be called Test
class Test(unittest.TestCase):
    # def test_works_when_the_customer_has_no_active_users_during_the_month(self):
    #  self.assertAlmostEqual(bill_for('2019-01', new_plan, no_users), 0.00, delta=0.01)

    #  def test_works_when_everything_stays_the_same_for_a_month(self):
    #   self.assertAlmostEqual(bill_for('2019-01', new_plan, constant_users), 8.00, delta=0.01)

    def test_works_when_a_user_is_activated_during_the_month(self):
        self.assertAlmostEqual(bill_for('2019-01', new_plan, user_signed_up), 10.84, delta=0.01)
