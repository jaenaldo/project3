#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install geopy


# In[2]:


get_ipython().system(' pip install geopandas')


# In[3]:


pip install pandas


# In[4]:


from geopy.geocoders import ArcGIS
import numpy as np, geopandas as gpd, pandas as pd


# In[5]:


crime = pd.read_csv('C:/Users/jaena/OneDrive/Desktop/Personal Project/Crime Rate/crime_final.csv')


# In[6]:


crime["FULL_ADDRESS"]= crime["ADDRESS"].astype(str)+ "," + " " + "Phoenix" + "," +" " + "AZ"+","+" "+crime["ZIP"].astype(str)


# In[7]:


coordinate = crime["FULL_ADDRESS"].tolist()
print(coordinate)


# In[8]:


print(coordinate[3016])


# In[9]:


nom = ArcGIS()


# In[10]:


from geopandas.tools import geocode

coords = geocode(coordinate, provider ='bing', api_key ='AlS0uxqoiGLOyuLIgovCp_CLqIwEOyHkHxMNu46nCtGLD9m1wFq-oDp6SIlumfeJ')
    


# In[11]:


coords.head(n=3017)


# In[12]:


# changing index 3016 due to the geocoding issue

from shapely.wkt import loads
string = "POINT (-112.141408 33.549435)"
geom = loads(string) 
coords.loc[3016, 'geometry']= geom  


# In[13]:


string1 = "N 38th Dr & W Frier Dr, Phoenix, AZ 85051, United States"
coords.loc[3016, 'address'] =string1


# In[14]:


coords.head(n=3017)


# In[15]:


row = coords.iloc[3014]
print(row)


# In[16]:


police = pd.read_csv('C:/Users/jaena/OneDrive/Desktop/Personal Project/Crime Rate/Police_Stations.csv')


# In[17]:


police["FULL_ADDRESS"]= police["ADDRESS"].astype(str)+ "," + " " + "Phoenix" + "," +" " + "AZ"+","+" "+police["ZIPCODE"].astype(str)


# In[18]:


police["FULL_ADDRESS"]


# In[19]:


police_coordinate = police["FULL_ADDRESS"].tolist()


# In[20]:


from geopandas.tools import geocode

police_coords = geocode(police_coordinate, provider ='bing', api_key ='AlS0uxqoiGLOyuLIgovCp_CLqIwEOyHkHxMNu46nCtGLD9m1wFq-oDp6SIlumfeJ')


# In[21]:


police_coords.head(n=20)


# In[22]:


coords = coords.to_crs(4326)
police_coords = police_coords.to_crs(4326)


# In[23]:


phx_map = gpd.read_file('C:/Users/jaena/OneDrive/Desktop/Personal Project/Crime Rate/mygeodata/border_level8_polygon.shp')

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(20,20))
plt.title("2020 Phoenix, Arizona Crime Map - City Boundary", fontsize=20)
phx_map.plot(ax=ax, **{'edgecolor':'black', 'facecolor':'white'})
coords.plot(ax=ax, marker =".", markersize=25, color='red', alpha=0.25)
police_coords.plot(ax=ax, marker ="*", markersize=30, color='blue')
#plt.savefig('C:/Users/jaena/OneDrive/Desktop/Personal Project/Crime Rate/crime_map1.png', dpi=400, bbox_inches='tight')


# In[24]:


phx_map.head(n=500)


# In[25]:


zip_phx_map = gpd.read_file('C:/Users/jaena/OneDrive/Desktop/GIS322/data/data/AZ_zipcodes/AZ_zipcodes.shp')


# In[26]:


zip_phx_map
zip_phx_map.plot()


# In[40]:


zip_phx_map = zip_phx_map[(zip_phx_map['Zipcode'] ==85003) | (zip_phx_map['Zipcode'] ==85004)                 |(zip_phx_map['Zipcode'] == 85007) |(zip_phx_map['Zipcode'] == 85008)                 |(zip_phx_map['Zipcode'] == 85009)|(zip_phx_map['Zipcode'] == 85012)                 |(zip_phx_map['Zipcode'] == 85013)|(zip_phx_map['Zipcode'] == 85014)                 |(zip_phx_map['Zipcode'] == 85015)|(zip_phx_map['Zipcode'] == 85016)                 |(zip_phx_map['Zipcode'] == 85017)|(zip_phx_map['Zipcode'] == 85018)                 |(zip_phx_map['Zipcode'] == 85019)|(zip_phx_map['Zipcode'] == 85020)                 |(zip_phx_map['Zipcode'] == 85021)|(zip_phx_map['Zipcode'] == 85022)                 |(zip_phx_map['Zipcode'] == 85023)|(zip_phx_map['Zipcode'] == 85024)                 |(zip_phx_map['Zipcode'] == 85027)|(zip_phx_map['Zipcode'] == 85028)                 |(zip_phx_map['Zipcode'] == 85029)                 |(zip_phx_map['Zipcode'] == 85031)|(zip_phx_map['Zipcode'] == 85032)                 |(zip_phx_map['Zipcode'] == 85033)|(zip_phx_map['Zipcode'] == 85034)                 |(zip_phx_map['Zipcode'] == 85035)|(zip_phx_map['Zipcode'] == 85037)                 |(zip_phx_map['Zipcode'] == 85040)|(zip_phx_map['Zipcode'] == 85041)                 |(zip_phx_map['Zipcode'] == 85042)|(zip_phx_map['Zipcode'] == 85043)                 |(zip_phx_map['Zipcode'] == 85044)#|(zip_phx_map['Zipcode'] == 85045)\
                |(zip_phx_map['Zipcode'] == 85048)|(zip_phx_map['Zipcode'] == 85006)\
                 |(zip_phx_map['Zipcode'] == 85050)|(zip_phx_map['Zipcode'] == 85051)\
                 |(zip_phx_map['Zipcode'] == 85053)|(zip_phx_map['Zipcode'] == 85054)\
                 |(zip_phx_map['Zipcode'] == 85083)|(zip_phx_map['Zipcode'] == 85085)\
                 |(zip_phx_map['Zipcode'] == 85086)|(zip_phx_map['Zipcode'] == 85087)\
                |(zip_phx_map['Zipcode'] == 85331)\
                |(zip_phx_map['Zipcode'] == 85254)|(zip_phx_map['Zipcode'] == 85253)\
                         |(zip_phx_map['Zipcode'] == 85251)|(zip_phx_map['Zipcode'] == 85282)\
                         |(zip_phx_map['Zipcode'] == 85353)|(zip_phx_map['Zipcode'] == 85045)]
                 
zip_phx_map.plot()
#47, 49, 52, 56-59, 77, 81, 84, (86 is the end), (98, 97)


# In[41]:


zip_phx_map['coords'] = zip_phx_map['geometry'].apply(lambda x: x.representative_point().coords[:])
zip_phx_map['coords'] = [coords[0] for coords in zip_phx_map['coords']]


# In[29]:


zip_phx_map


# In[54]:


import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(20,30))   
plt.rcParams.update({'font.size': 10})
zip_phx_map.plot(ax=ax, **{'edgecolor':'black', 'facecolor':'white'})
police_coords.plot(ax=ax, marker='o', markersize=1000, color='blue')
texts =[ax.text(row.coords[0], row.coords[1], s=row['Zipcode'], horizontalalignment='center'       , bbox = {'facecolor': 'white', 'alpha':0.8, 'pad': 2, 'edgecolor':'none'})        for idx, row in zip_phx_map.iterrows()]
coords.plot(ax=ax, marker='.', markersize = 80, color ='red', alpha = .3)
ax.set_title('2020 Crime Map of Phoenix Zipcode Boundary with the location of Police Stations')
plt.savefig('C:/Users/jaena/OneDrive/Desktop/Personal Project/Crime Rate/crime_map_with_ps.png')


# In[31]:


zip_phx_map.crs


# In[32]:


coords["ZIPCODE"]=crime["ZIP"]

gdf = gpd.GeoDataFrame(coords, geometry ='geometry')

data_with_zip = gpd.sjoin(phx_map, coords, how='left', op='contains')

crime_per_zip = data_with_zip.groupby('ZIPCODE').size().reset_index(name ='Count Zip')

print(crime_per_zip.head(n=100))


# In[33]:


merged_crime_per_zip = pd.merge(zip_phx_map, crime_per_zip, left_on='Zipcode', right_on='ZIPCODE')


# In[34]:


merged_crime_per_zip.plot(column="Count Zip", cmap='OrRd', 
                          legend=True,
                          legend_kwds={"label": "Crime map of Phoenix, Arizona per Zipcode in 2020","orientation":"horizontal"},
                          figsize=(20,20))


# In[35]:


from mpl_toolkits.axes_grid1 import make_axes_locatable

fig, ax = plt.subplots(figsize=(20,20))



divider = make_axes_locatable(ax)
plt.title('2020 Pheonix, Arizona Crime Map- Zipcode Level', fontsize=20)


merged_crime_per_zip.plot(column ="Count Zip", cmap = "OrRd",ax=ax, **{'edgecolor':'black'},
                         legend=True);
fig = ax.figure
cb_ax = fig.axes[1]
cb_ax.tick_params(labelsize=10)

texts =[ax.text(row.coords[0], row.coords[1], s=row['Zipcode'], horizontalalignment='center'       , bbox = {'facecolor': 'white', 'alpha':0.8, 'pad': 2, 'edgecolor':'none'})        for idx, row in zip_phx_map.iterrows()]
#plt.savefig('C:/Users/jaena/OneDrive/Desktop/Personal Project/Crime Rate/crime_map_per_zip.jpg')


# In[36]:


conda install basemap


# In[37]:


conda install anaconda=custom basemap


# In[38]:


from mpl_toolkits.basemap import Basemap
fig =plt.figure(figsize=(8,6), edgecolor='w')
m = Basemap(projection='cyl', resolution=None,
           llcrnrlat=-90, urcrnrlat=90,
           llcrnrlon=-180, urcrnrlon=180,)
draw_map(m)

