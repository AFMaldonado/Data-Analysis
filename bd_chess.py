import pandas as pd
from sqlalchemy import create_engine
import os

# Conexion a la base de datos

conn_string = '{}://{}:{}@{}/{}'.format(
os.environ["database_type"], os.environ["user"], os.environ["password"], os.environ["host"] , os.environ["database"])

sql_conn = create_engine(conn_string)

# Creacion base de datos Chess

query_sql = '''
CREATE SCHEMA `chess` ;
'''

sql_conn.execute(query_sql)

# Creacion de tabla de estadisticas

query_sql = '''
CREATE TABLE `chess`.`statistics` (
  `index` INT NOT NULL,
  `rank` INT NULL,
  `country` VARCHAR(500) NULL,
  `flag` VARCHAR(45) NULL,
  `num_players` INT NULL,
  `women` INT NULL,
  `percent_women` DECIMAL(4,2) NULL,
  `fide_average` INT NULL,
  `gms` INT NULL,
  `ims` INT NULL,
  `fms` INT NULL,
  `wgms` INT NULL,
  `wims` INT NULL,
  `wfms` INT NULL,
  `age_avg` INT NULL,
  PRIMARY KEY (`index`));
'''
sql_conn.execute(query_sql)

# Creacion de tabla jugadores

query_sql = '''
CREATE TABLE `chess`.`players` (
  `rank` INT NULL,
  `name` VARCHAR(500) NULL,
  `title` VARCHAR(200) NULL,
  `country` VARCHAR(200) NULL,
  `fide` VARCHAR(200) NULL,
  `age` INT NULL,
  `age_k_factor` INT NULL);
'''

sql_conn.execute(query_sql)

# Llenado tabla estadisticas

query_sql = '''
LOAD DATA
INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/International_Chess_Stats.csv"
INTO TABLE chess.statistics
FIELDS TERMINATED BY ","
OPTIONALLY ENCLOSED BY "'";
'''

sql_conn.execute(query_sql)

# Llenado tabla jugadores

query_sql = '''
LOAD DATA
INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Complete_Players_Database.csv"
INTO TABLE chess.players
FIELDS TERMINATED BY ","
OPTIONALLY ENCLOSED BY "'";
'''

sql_conn.execute(query_sql)

# Lectura de 5 primeros registros tabla players

query_sql = 'select * from players'
df = pd.read_sql(query_sql, sql_conn)

df.head(5)

# Lectura de 5 primeros registros tabla statistics

query_sql = 'select * from statistics'
df2 = pd.read_sql(query_sql, sql_conn)

df2.head(5)
