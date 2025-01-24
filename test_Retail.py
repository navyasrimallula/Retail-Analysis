import pytest
from lib import configReader, dataReader, Utils, dataManipulation

@pytest.mark.skip()
def test_readCust(spark):
    cust = dataReader.read_customers(spark,"LOCAL")
    assert cust.count()==12434

@pytest.mark.skip()
def test_readOrders(spark):
    ord = dataReader.read_orders(spark,"LOCAL")
    assert ord.count()==68882

@pytest.mark.skip()
def test_filter(spark):
    ord = dataReader.read_orders(spark,"LOCAL")
    assert dataManipulation.filter_closed_orders(ord).count()==7555

#@pytest.mark.skip()
def test_readAppConfig():
    con = configReader.get_app_config("LOCAL")
    assert con['customers.file.path'] == 'data/customers.csv'

@pytest.mark.skip()
def test_count_orders_state(spark, expectedResult):
    cust = dataReader.read_customers(spark,"LOCAL")
    assert dataManipulation.count_orders_state(cust).collect() == expectedResult.collect()

@pytest.mark.skip("work in progress")
def test_groupBy(spark):
    ord = dataReader.read_orders(spark,"LOCAL")
    cust = dataReader.read_customers(spark,"LOCAL")
    joined_df = dataManipulation.join_orders_customers(ord, cust)
    assert dataManipulation.count_orders_state(joined_df).count() == 44

#@pytest.mark.parametrize(
#    "status, count",
#    [("CLOSED", 7555),
#     ("PENDING_PAYMENT", 15030),
#     ("COMPLETE", 22899)]
#)
@pytest.mark.skip()
def test_order_status(spark, status, count):
    ord = dataReader.read_orders(spark,"LOCAL")
    filtered_count = dataManipulation.check_order_status(ord, status).count()
    assert filtered_count == count