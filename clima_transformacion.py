import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import gs_uuid
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Datos originales
Datosoriginales_node1739152381961 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://xideral-jesus/historical_weather.csv"], "recurse": True}, transformation_ctx="Datosoriginales_node1739152381961")

# Script generated for node Change Schema
ChangeSchema_node1739152520933 = ApplyMapping.apply(frame=Datosoriginales_node1739152381961, mappings=[("date", "string", "date", "date"), ("temperature_2m_max", "string", "temperature_2m_max", "float"), ("temperature_2m_min", "string", "temperature_2m_min", "float"), ("temperature_2m_mean", "string", "temperature_2m_mean", "float"), ("rain_sum", "string", "rain_sum", "float"), ("precipitation_hours", "string", "precipitation_hours", "float"), ("wind_speed_10m_max", "string", "wind_speed_10m_max", "float"), ("shortwave_radiation_sum", "string", "shortwave_radiation_sum", "float")], transformation_ctx="ChangeSchema_node1739152520933")

# Script generated for node UUID
UUID_node1739152655972 = ChangeSchema_node1739152520933.gs_uuid(colName="id")

# Script generated for node Datos 
EvaluateDataQuality().process_rows(frame=UUID_node1739152655972, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1739152336643", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
Datos_node1739152590209 = glueContext.write_dynamic_frame.from_options(frame=UUID_node1739152655972, connection_type="s3", format="csv", connection_options={"path": "s3://xideral-jesus", "partitionKeys": []}, transformation_ctx="Datos_node1739152590209")

job.commit()