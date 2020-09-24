from django.db import models
import pandas as pd
from adaptor.model import CsvModel



# 필터된 데이터 프레임 result
class basic(CsvModel):
    recipe_code = models.IntegerField() # 레시피이름
    introduce = models.CharField() # 간략소개
    quantile = models.CharField(max_length = 4) # 분량
    level = models.CharField(max_length = 3) # 난이도
    classfication = models.CharField(max_length = 20) # 유형분류
    image = models.CharField()
    calorie = models.IntegerField()
    
    class Meta:
         delimiter = ";"
    
class raw(CsvModel):
    recipe_code = models.IntegerField()
    raw_name = models.CharField()
    raw_quantile = models.CharField()
    
    class Meta:
         delimiter = ";"

class process(CsvModel):
    recipe_code = models.IntegerField()
    recipe_process_Char = models.CharField()
    recipe_process_num = models.IntegerField()
    recipe_process_image = models.CharField()
    
    class Meta:
        delimiter = ";"

df0 = basic.import_data(data = open("레시피_기본정보.csv"))
df1 = raw.import_data(data = open("레시피_재료정보.csv"))
df2 = process.import_data(data = open("레시피_과정정보.csv"))
    
first_line = df0[0]
first_line.recipe_code
    

