from django.db import models
import pandas as pd

df = pd.read_csv('test_csv.txt', sep = ';')


# 필터된 데이터 프레임 result
class basic(models.Model):
    recipe_code = models.IntegerField() # 레시피이름
    introduce = models.CharField() # 간략소개
    quantile = models.CharField(max_length = 4) # 분량
    level = models.CharField(max_length = 3) # 난이도
    classfication = models.CharField(max_length = 20) # 유형분류
    image = models.CharField()
    calorie = models.IntegerField()
    
class raw(models.Model):
    recipe_code = models.IntegerField()
    raw_name = models.CharField()
    raw_quantile = models.CharField()

class process(models.Model):
    recipe_code = models.IntegerField()
    recipe_process_Char = models.CharField()
    recipe_process_num = models.IntegerField()
    recipe_process_image = models.CharField()
    

    

