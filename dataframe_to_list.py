def dataframe_to_list(data):
    SECONDS_PER_DAY = 24*60*60
    dataframe = data.copy()
    #dataframe = dataframe
    min_date = dataframe['disp'].min().to_pydatetime()
    dataframe['disp'] = dataframe['disp'].apply(lambda x: (x.to_pydatetime()- min_date).total_seconds()/SECONDS_PER_DAY)
    dataframe['max'] = dataframe['max'].apply(lambda x: (x.to_pydatetime()-min_date).total_seconds()/SECONDS_PER_DAY)
    dataframe['durée'] = dataframe['durée']
    
    return(list(dataframe['disp']),list(dataframe['max']),list(dataframe['durée']))