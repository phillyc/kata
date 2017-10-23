import csv
import unittest
from shutil import copyfile

print("_____ SLCSP Data Munge! _____")
'''
functional flow: 

load_slcsp_file opens a new working file and manages the other functions
get_rate_area returns a tuple of rate area for a given zipcode
lookup_silver_rate_planes returns all silver rate plans for the given rate area
calc_slcsp returns the SLCSP of a given list of rates
'''

def load_slcsp_file():
    '''
    Main event function. 
    Creates a new solution file and loads it with data.
    '''
    copyfile("slcsp.csv", "solution_slcsp.csv")
    prune_plans_file()

    with open("slcsp.csv", "rb") as source:
        reader = csv.reader(source)
        with open("solution_slcsp.csv", "wb") as solution:
            writer = csv.writer(solution, delimiter=',')
            writer.writerow(["zipcode","rate"])
            next(reader) # Skip the header
            for row in reader:
                # Get the rate area for the given zipcode
                rate_area = get_rate_area(row[0])
                if rate_area == None:
                    continue
                silver_plans = lookup_silver_rate_plans(rate_area)
                slcsp = calc_slcsp(silver_plans)
                # Write the slcsp solution
                writer.writerow([row[0],slcsp])


def get_rate_area(zipcode):
    '''
    Open the zips.csv file and search for the given zip.
    Only return one match, if there is only one rate area.
    If multiple rows are found, but the same rate area, give that rate area.

    Expects int representing a zipcode.

    Returns a Rate Area tuple, ex NY 1, IL 4
    '''
    rate_area = ()
    with open("zips.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if str(zipcode) in row[0]:
                match = row[1],row[4]
                # Have we already captured this match?
                if set(match).issubset(set(rate_area)):
                    next
                # Previous captured RA doesn't match current value?
                if len(rate_area) != 0 and rate_area != match:
                    return None
                else:
                    rate_area = row[1], row[4]
        if len(rate_area) == 0:
            return None
        else:
            return rate_area


def prune_plans_file():
    '''
    Prune the plans.csv of any non-silver plans.
    This should speed up the searching in other functions.
    I this could probably be done even faster with something like a set.
    '''
    with open("plans.csv", "rb") as source:
        with open("pruned_plans.csv", "wb") as destination:
            reader = csv.reader(source)
            writer = csv.writer(destination, delimiter=",")
            writer.writerow(["plan_id","state","metal_level","rate","rate_area"])
            next(reader) # Skip the header
            for row in reader:
                if row[2] == "Silver":
                    writer.writerow(row)
                else:
                    continue


def lookup_silver_rate_plans(rate_area):
    '''
    Takes a given rate area tuple and returns a list of silver rates.

    Return list of rates: ex ['411.77', '292.36'] or []
    '''
    with open("pruned_plans.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        rate_area = [rate_area[0], rate_area[1]]
        found_rates = []
        for row in reader:
            if row[1] == rate_area[0] and row[4] == rate_area[1] and row[2] == 'Silver':
                found_rates.append(row[3])
            else:
                next
        return found_rates


def calc_slcsp(rates_found):
    '''
    Takes a given list of rates and returns the second lowest unique.

    Return a float representing the second lowest unique in the list.
    Return None if ambiguous.
    '''
    if len(rates_found) < 3:
        return None
    else:
        return float(sorted(rates_found)[1])


class MyTest(unittest.TestCase):

    def test_get_rate_area_should_return_false(self):
        self.assertEqual(get_rate_area(54923), None)

    def test_get_rate_area_should_return_MO_3(self):
        expected_ra = ('MO', '3')
        self.assertEqual(get_rate_area(64148), expected_ra)

    def test_get_rate_area_should_return_TN_3(self):
        expected_ra = ('TN', '3')
        self.assertEqual(get_rate_area(37333), expected_ra)

    def test_get_rate_area_should_return_DC_1(self):
        expected_ra = ('DC', '1')
        self.assertEqual(get_rate_area(20047), expected_ra)

    def test_get_rate_area_should_return_one_ra_when_duplicates_exist(self):
        expected_ra = ('KS', '4')
        self.assertEqual(get_rate_area(67651), expected_ra)

    def test_lookup_silver_rate_plans_FL(self):
        rate_area = ('FL', '60')
        rates_found = len(lookup_silver_rate_plans(rate_area))
        self.assertEqual(rates_found, 18)

    def test_lookup_silver_rate_plans_GA(self):
        rate_area = ('GA', '13')
        rates_found = len(lookup_silver_rate_plans(rate_area))
        self.assertEqual(rates_found, 30)

    def test_lookup_silver_rate_plans_PR(self):
        rate_area = ('PR', '1')
        rates_found = len(lookup_silver_rate_plans(rate_area))
        self.assertEqual(rates_found, 0)

    def test_calc_slcsp_returns_none_when_given_none(self):
        rates = []
        self.assertEqual(calc_slcsp(rates), None)
   
    def test_calc_slcsp_returns_none_when_given_two(self):
        rates = ['421.43', '324.98']
        self.assertEqual(calc_slcsp(rates), None)

    def test_calc_slcsp_returns_one_when_given_three(self):
        rates = ['421.43', '324.98', '330.98']
        self.assertEqual(calc_slcsp(rates), 330.98)

    def test_calc_slcsp_returns_one_when_given_duplicates(self):
        rates = ['421.43', '324.98', '324.98']
        self.assertEqual(calc_slcsp(rates), 324.98)

    def test_calc_slcsp_returns_one_when_given_many(self):
        rates = ['421.43', '324.98', '330.98', '364.46', '346.37', '411.77', '292.53', '408.1', '301.29', '352.04', '319.53', '318.83', '367.78', '412.06', '280.02', '448.5', '254.16', '337.14']
        self.assertEqual(calc_slcsp(rates), 280.02)

    def test_end_to_end_61232_should_resolve(self):
        rate_area = get_rate_area(61232)
        if rate_area == False:
            slcsp = None
        else:
            silver_plans = lookup_silver_rate_plans(rate_area)
            slcsp = calc_slcsp(silver_plans)
        self.assertEqual(slcsp, 222.38)

    def test_end_to_end_86313_should_resolve(self):
        rate_area = get_rate_area(86313)
        if rate_area == False:
            slcsp = None
        else:
            silver_plans = lookup_silver_rate_plans(rate_area)
            slcsp = calc_slcsp(silver_plans)
        self.assertEqual(slcsp, 292.9)

    def test_end_to_end_20047_should_not_resolve(self):
        rate_area = get_rate_area(20047)
        if rate_area == None:
            slcsp = None
        else:
            silver_plans = lookup_silver_rate_plans(rate_area)
            slcsp = calc_slcsp(silver_plans)
        self.assertEqual(slcsp, None)

    def test_end_to_end_47452_should_not_resolve(self):
        rate_area = get_rate_area(47452)
        if rate_area == None:
            slcsp = None
        else:
            silver_plans = lookup_silver_rate_plans(rate_area)
            slcsp = calc_slcsp(silver_plans)
        self.assertEqual(slcsp, None)


if __name__ == '__main__':
    # Swap these functions to run tests or actual file building.
    # unittest.main()
    load_slcsp_file()

    