import openmeteo_requests
import pandas as pd
import boto3
import os

def lambda_handler(event, context):
    openmeteo = openmeteo_requests.Client()
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
	"latitude": 25.67507,
	"longitude": -100.31847,
	"start_date": "2020-01-01",
	"end_date": "2024-12-31",
	"daily": ["temperature_2m_max", "temperature_2m_min", "temperature_2m_mean", "rain_sum", "precipitation_hours", "wind_speed_10m_max", "shortwave_radiation_sum"],
	"timezone": "America/Chicago"
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]

    # Procesamos la respuesta de la API y extraemos cada variable para volverla un arreglo
    daily = response.Daily()
    daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
    daily_temperature_2m_mean = daily.Variables(2).ValuesAsNumpy()
    daily_rain_sum = daily.Variables(3).ValuesAsNumpy()
    daily_wind_speed_10m_max = daily.Variables(4).ValuesAsNumpy()
    daily_shortwave_radiation_sum = daily.Variables(5).ValuesAsNumpy()

    # Creamos un diccionario con los datos
    daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
    )}

    daily_data["temperature_2m_max"] = daily_temperature_2m_max
    daily_data["temperature_2m_min"] = daily_temperature_2m_min
    daily_data["temperature_2m_mean"] = daily_temperature_2m_mean
    daily_data["rain_sum"] = daily_rain_sum
    daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
    daily_data["shortwave_radiation_sum"] = daily_shortwave_radiation_sum

    daily_dataframe = pd.DataFrame(data = daily_data)

    # 📂 Guardar datos en un bucket de S3
    s3 = boto3.client("s3")
    bucket_name = os.environ["S3_BUCKET_NAME"]  # Nombre del bucket en S3
    file_name = "historical_weather.csv"
    
    # Convertimos el dataframe en un archivo csv, por defecto delimitado por ","
    csv_buffer = daily_dataframe.to_csv(index=False)
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer)

    return{
        "statusCode": 200,
        "body": json.dumps(f"Archivo {file_name} guardado en S3 correctamente.")
    }