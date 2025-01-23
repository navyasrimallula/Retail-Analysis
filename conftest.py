import pytest
from lib import Utils
@pytest.fixture
def spark():
    "creates spark session"
    spark_session = Utils.get_spark_session("LOCAL")
    yield spark_session
    spark_session.stop()

@pytest.fixture
def expectedResult(spark):
    "gets the expected result data"
    ex_schema = "state string, count int"
    return spark.read.csv("test_results/stateAggregate.csv", schema = ex_schema)