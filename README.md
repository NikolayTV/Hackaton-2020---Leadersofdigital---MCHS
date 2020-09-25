# Hackaton-2020---Leadersofdigital---MCHS
https://docs.google.com/document/d/1q3gyag7DPvKUqWCpd92OYG5bnMN3bHoWEaFwB_54LYE/edit - Документ с сылками и тезисами

## Tools 


1. JS библиотека для графиков и карт - (https://www.react-simple-maps.io)



# Nikolay

## Tools
1. https://blog.jupyter.org/interactive-gis-in-jupyter-with-ipyleaflet-52f9657fa7a - ipywidgets + ipyleaflet. Maps in ipywidgets
http://gallery.pangeo.io/ - gallery of other Earth specific tools and data. 
2. https://github.com/wildfirepy/wildfirepy - some python project for using wild fire data with terrible documentation
3. http://www.wildfireincidents.com/current-wildfire-activity-map - wildFire Activity map
4. http://gallery.pangeo.io/ - gallery of other Earth specific tools and data


## Maps API
1. есть API по категориям земель опенсорсное Based on the European Space Agency
  Гитхаб с описанеим https://github.com/Envirometrix/LandGISmaps
  Пример самой карты https://openlandmap.org/#/?base=BingMaps%20(Aerial)&center=55.2589,82.4785&zoom=10&opacity=80&layer=lcv_land.cover_esacci.lc.l4_c&time=2015
2. Open Weather Api - https://openweathermap.org/api
3. https://fires.ru/help.html - коммерческое API по локализации пожаров в РФ, есть бесплатная версия.
4. http://kaskad.ukmmchs.ru/map/query?int&20200925&20200926.json - Выдача термоточек по API от каскада
  
## МЛ
1. https://github.com/GeneralLi95/deepglobe_land_cover_classification_with_deeplabv3plus - Классификация земли по спутниковому снимку. Где-то там есть уже готовый датасет
2. https://www.kaggle.com/data13/brazilian-wildfire-prediction/notebook - Можно сделать предсказание вероятности появления пожара в регионе по историческим данным
3. https://www.kaggle.com/edhirif/predict-the-causes-of-wildfires-using-python 
   https://www.kaggle.com/edhirif/predict-the-causes-of-wildfires-using-python - Предсказание причины пожара по GPS, дате, времени, погоде
4. https://www.kaggle.com/psvishnu/forestfire-impact-prediction-stats-and-ml - Предсказание площади территории пожара
5. Можно также предсказывать силу пожара по его координатам погоде и т.п. 

Вывод: 
Для построения моделей предсказания площади охвата пожара, его интенсивности, причины пожара по координатам нужно спарсить категорию земель, время + прогноз погоды.

Для предсказания вероятности появления пожаров и их интенсивности нужны исторические данных по пожарам + погода.

