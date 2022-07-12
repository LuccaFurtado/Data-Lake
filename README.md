# Data-Lake

Streaming de dados entre as camadas de um Data Lake no Databricks com deltalake.

Esquema do projeto:
<p align="center">
<img src="https://github.com/LuccaFurtado/images/blob/main/spark-streaming(2).png" width="900" height="500">
</p>

O resultado pode ser visto a seguir:

![alt text](https://github.com/LuccaFurtado/Data-Lake/blob/main/streaming-databricks.jpg)

Na imagem da esquerda podemos ver o streaming dos dados da camada Raw para a camada Bronze. Já na imagem da direita, o streaming dos dados entre a camada Bronze e a camada Silver pode ser visualizado.

Ao dar o zoom nas imagens, mais precisamente nos eixos dos gráficos, é possível ver o intervalo de tempo de cada operação e que há um fluxo de dados acontecendo entre as respectivas camadas.

O código para a realização do streaming e algumas observações podem ser vistas nos seguintes notebooks: [Streaming Raw/Bronze](https://github.com/LuccaFurtado/Data-Lake/blob/main/ingest_table_final_cleaned.ipynb) e [Streaming Bronze/Silver](https://github.com/LuccaFurtado/Data-Lake/blob/main/silver_ingest.ipynb)

Outros arquivos utilizados foram os seguintes scripts: [Script para gerar dados semi aleatórios incrementais](https://github.com/LuccaFurtado/Data-Lake/blob/main/generate_incremental.py) cuja utilidade era inserir dados para visualização da ingestão dos dados e das operações de Insert, Update e Delete no processo de streaming entre a camada Raw e Bronze, [Script para carregar os dados no S3](https://github.com/LuccaFurtado/Data-Lake/blob/main/load_incremental.py) e [Script 'utils' com as funções utilizadas no script anterior](https://github.com/LuccaFurtado/Data-Lake/blob/main/utils.incremental.py).
