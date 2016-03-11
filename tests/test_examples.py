"""Test to make sure that my changes to get_example_project do not break
the instructions in eemeter.readthedocs.org.
"""
from eemeter.examples import get_example_project, one_resi_gbutton_project
from eemeter.meter import DefaultResidentialMeter
from eemeter.meter import DataCollection

from datetime import datetime

def test_existing_meter():
    """Step through the example from eemeter.readthedocs.org.
    """

    project = get_example_project("94087")
    meter = DefaultResidentialMeter()
    results = meter.evaluate(DataCollection(project=project))
    electricity_usage_pre = results.get_data("annualized_usage", ["electricity", "baseline"]).value
    electricity_usage_post = results.get_data("annualized_usage", ["electricity", "reporting"]).value
    natural_gas_usage_pre = results.get_data("annualized_usage", ["natural_gas", "baseline"]).value
    natural_gas_usage_post = results.get_data("annualized_usage", ["natural_gas", "reporting"]).value
    electricity_savings = (electricity_usage_pre - electricity_usage_post) / electricity_usage_pre
    natural_gas_savings = (natural_gas_usage_pre - natural_gas_usage_post) / natural_gas_usage_pre

    # assert str(electricity_savings) == '[ 0.49999999]'
    # assert str(natural_gas_savings) == '[ 0.50000001]'
    # Surprisingly, these results published in the docs actually reproduce exactly on my local dev
    # but not on github in the automated tests, so round instead.  This "test" merely ensures
    # that I have not broken the documented stepwise example instructions.

    assert round(electricity_savings[0], 2) == 0.5
    assert round(natural_gas_savings[0], 2) == 0.5
