# **ANÁLISIS Y MODELO DE MACHINE LEARNING PARA DATOS METEOROLÓGICOS DE MONTERREY, NUEVO LEÓN, MÉXICO**

## 📌 Objetivo del Proyecto

El propósito de este proyecto fue obtener y analizar datos meteorológicos utilizando la **API de Open-Meteor**, aplicar un proceso ETL en **AWS** y desarrollar un modelo de aprendizaje automático en **Google Colab** para evaluar patrones climáticos. En este proyecto, utilicé herramientas de **AWS** y **Python** para procesar información climática y generar predicciones útiles.

---

### 1️⃣ Obtención de Datos

- Utilicé la API de Open-Meteor para extraer información meteorológica diaria. Los parámetros a solicitar fueron:
  - Temperatura máxima (`temperature_2m_max`)
  - Temperatura mínima (`temperature_2m_min`)
  - Temperatura media (`temperature_2m_mean`)
  - Precipitación total (`rain_sum`)
  - Horas de precipitación (`precipitation_hours`)
  - Velocidad máxima del viento a 10m (`wind_speed_10m_max`)
  - Radiación solar acumulada (`shortwave_radiation_sum`)

- **Rango de Fechas**: `01 de Enero de 2020 a 31 de diciembre de 2024`

- **Validación de Datos**:
  - Realicé una revision para detectar campos duplicados.
  - Verifiqué que no hubiera valores nulos.
---

### 2️⃣ Proceso ETL en AWS

Creé un flujo de datos en AWS para procesar y almacenar los datos. A continuación, describo los pasos que seguí:

- **Extracción de Datos con AWS Lambda**:
  - Utilicé **AWS Lambda** para conectarme a la API de Open-Meteor y extraer los datos meteorológicos diarios de las fechas establecidas y almacenar los datos crudos en un bucket de **Amazon S3**.

- **Almacenamiento de Datos en Amazon S3**:
  - Los datos originales obtenidos de la API se almacenaron en un bucket de **Amazon S3**. Este bucket sirvió como almacenamiento para los datos originales y los ya procesados.

Bucket en la region us-east-1:

![image](https://github.com/user-attachments/assets/87ff4ac5-1d3f-4346-bf4b-4531596ee9e3)

Datos originales:

![image](https://github.com/user-attachments/assets/095c2823-cc5d-4c1c-83e9-b86e3b8800df)

Datos procesados (Se renombraron al descargarse):

![image](https://github.com/user-attachments/assets/4013b13e-f415-495d-b44c-17d25361d632)


- **Catalogación de Datos con AWS Glue Crawler**:
  - Usé **AWS Glue Crawler** para escanear los datos originales almacenados en S3 y generar un esquema en **AWS Glue Data Catalog**. Esto permitió organizar los datos de manera que pudieran ser utilizados en el GLUE JOB.

![image](https://github.com/user-attachments/assets/59662723-52b0-49c8-ad7f-786256d0f787)


- **Transformación de Datos con AWS Glue Job**:
  - Implementé un **AWS Glue Job** para realizar las siguientes transformaciones en los datos:
    - Cambiar el tipo de dato de la columna de fecha a `DATE`.
    - Convertir las columnas numéricas (como temperatura, precipitación, etc.) a tipos de datos adecuados (`FLOAT`).
    - Agregar un campo `id` único para cada registro, facilitando la identificación.

Visual ETL Job:

![image](https://github.com/user-attachments/assets/8f92135f-94fb-4b4c-a353-70efb4d71d3f)

### 3️⃣ Análisis Exploratorio y Modelado en Google Colab

Una vez completado el proceso ETL en AWS, realicé el análisis exploratorio y el desarrollo de un modelo de Machine Learning para evaluar la relación entre las variables climáticas.

- **Descarga de Datos Transformados**:
  - Descargué los datos transformados desde el bucket de **Amazon S3** y los cargué en **Google Colab** para su análisis.

- **Generación de Gráficos**:
  - Utilicé **Matplotlib** y **Seaborn** para generar gráficos que ayudaran a comprender las relaciones entre las variables climáticas. Estos gráficos incluyen:
    - Distribución de temperaturas (baja, alta y moderada).
    - Relación entre la radiación solar y las temperaturas.
    - Cambio de la temperatura a través de los años.

- **Desarrollo del Modelo de Machine Learning**:
  - Creé un modelo para evaluar la relación entre la **temperatura promedio**, **temperatura mínima**, **temperatura máxima** y la **radiación solar**.
  - El modelo permitió identificar patrones y tendencias significativas entre estas variables, proporcionando resultados sobre cómo la radiación solar afecta las temperaturas.

- **Resultados y Visualizaciones**:
  - Todos los gráficos generados, así como los resultados del modelo de Machine Learning, están disponibles en el notebook en el repositorio.

## Resultados

Al realizar el análisis exploratorio en Google Colab , mediante gráficos y la matriz de correlación, pude observar que existe una relación positiva muy fuerte entre las temperaturas (mínima, máxima y promedio) y la radiación solar.
Para confirmar esta relación, desarrollé un modelo de Machine Learning, el cual confirmó que las variables de temperatura pueden utilizarse para predecir la radiación solar con una eficiencia del 84% , según las métricas calculadas. 

## 📝 Conclusión del proyecto

Este proyecto representó para mi una integración de todo lo aprendido a lo largo de la academia, permitiéndome aplicar conceptos y métodos que aprendí. A través del uso de la **API de Open-Meteor**, creé un flujo ETL en **AWS** para extraer, transformar y almacenar datos meteorológicos. Además, realicé en **Google Colab** un análisis exploratorio y desarrollé un modelo de Machine Learning para evaluar la relación entre variables de la temperatura y la radiación solar.

### Aprendizajes:
- Poner en practica lo aprendido en la academia sobre **AWS** para procesar datos.
- Mejoré mis habilidades en la limpieza, validación y transformación de datos.
- Creé un modelo predictivo para extraer valor de los datos.

En resumen, este proyecto no solo me permitió consolidar mis conocimientos adquiridos en la academia , sino también identificar áreas de crecimiento para futuros trabajos. Estoy satisfecho con los resultados obtenidos y emocionado por continuar explorando nuevas formas de aprovechar los datos.
