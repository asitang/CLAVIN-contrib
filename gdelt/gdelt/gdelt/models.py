from django.db import models



class GDELT(models.Model):
    GLOBALEVENTID = models.BigIntegerField()
    SQLDATE = models.IntegerField(null=True)
    MonthYear = models.CharField(max_length=6)
    Year = models.CharField(max_length=4)
    FractionDate = models.DecimalField(max_digits=8, decimal_places=4,null=True) 
    Actor1Code = models.CharField(max_length=3)  
    Actor1Name = models.CharField(max_length=255)  
    Actor1CountryCode = models.CharField(max_length=3) 
    Actor1KnownGroupCode = models.CharField(max_length=3) 
    Actor1EthnicCode = models.CharField(max_length=3) 
    Actor1Religion1Code = models.CharField(max_length=3) 
    Actor1Religion2Code = models.CharField(max_length=3)  
    Actor1Type1Code = models.CharField(max_length=3)  
    Actor1Type2Code = models.CharField(max_length=3)  
    Actor1Type3Code = models.CharField(max_length=3) 
    Actor2Code = models.CharField(max_length=3) 
    Actor2Name = models.CharField(max_length=255)  
    Actor2CountryCode = models.CharField(max_length=3)  
    Actor2KnownGroupCode = models.CharField(max_length=3)  
    Actor2EthnicCode = models.CharField(max_length=3)  
    Actor2Religion1Code = models.CharField(max_length=3) 
    Actor2Religion2Code = models.CharField(max_length=3) 
    Actor2Type1Code = models.CharField(max_length=3)  
    Actor2Type2Code = models.CharField(max_length=3) 
    Actor2Type3Code = models.CharField(max_length=3)  
    IsRootEvent = models.CharField(max_length=11)  
    EventCode = models.CharField(max_length=4)  
    EventBaseCode = models.CharField(max_length=4) 
    EventRootCode = models.CharField(max_length=4)  
    QuadClass = models.IntegerField(null=True)  
    GoldsteinScale = models.FloatField(null=True) 
    NumMentions = models.IntegerField(null=True)  
    NumSources = models.IntegerField(null=True) 
    NumArticles = models.IntegerField(null=True) 
    AvgTone = models.FloatField(null=True) 
    Actor1Geo_Type = models.IntegerField(null=True) 
    Actor1Geo_FullName = models.CharField(max_length=255) 
    Actor1Geo_CountryCode = models.CharField(max_length=2) 
    Actor1Geo_ADM1Code = models.CharField(max_length=4)  
    Actor1Geo_Lat = models.FloatField(null=True) 
    Actor1Geo_Long = models.FloatField(null=True) 
    Actor1Geo_FeatureID = models.CharField(max_length=11) 
    Actor2Geo_Type = models.IntegerField(null=True) 
    Actor2Geo_FullName = models.CharField(max_length=255) 
    Actor2Geo_CountryCode = models.CharField(max_length=2)  
    Actor2Geo_ADM1Code = models.CharField(max_length=4) 
    Actor2Geo_Lat = models.FloatField(null=True) 
    Actor2Geo_Long = models.FloatField(null=True) 
    Actor2Geo_FeatureID = models.CharField(max_length=11)  
    ActionGeo_Type = models.IntegerField(null=True) 
    ActionGeo_FullName = models.CharField(max_length=255)  
    ActionGeo_CountryCode = models.CharField(max_length=2)  
    ActionGeo_ADM1Code = models.CharField(max_length=4) 
    ActionGeo_Lat = models.FloatField(null=True) 
    ActionGeo_Long = models.FloatField(null=True) 
    ActionGeo_FeatureID = models.CharField(max_length=11) 
    DATEADDED = models.IntegerField(null=True)
    SOURCEURL = models.CharField(max_length=255)

