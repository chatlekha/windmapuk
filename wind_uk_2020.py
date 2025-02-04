import folium
import pandas as pd
import branca

df = pd.read_excel('wind_energy_UK_2020.xlsx')
m = folium.Map(location=[55.835501, -3.411868], zoom_start=7)

def fancy_html(row):
    i = row
    
    Project = df.NAME[i]                            
    Size = df.PROJECT[i]                           
    Type = df.TYPE[i]
    Owner = df.Owner[i]                                           
    Developer = df.Developer[i]                               
    Year = df.YEAR[i]                             
    
    left_col_colour = "#48C9B0"
    right_col_colour = "#D1F2EB "
    
    html = """<!DOCTYPE html>
<html>

<head>
<h4 style="margin-bottom:0"; width="300px">{}</h4>""".format(Year) + """

</head>
    <table style="height: 126px; width: 300px;">
<tbody>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Project</span></td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(Project) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Size (MW)</td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(Size) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Type</td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(Type) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Owner</span></td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(Owner) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Developer</span></td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(Developer) + """
</tr>
<tr>
</tbody>
</table>
</html>
"""
    return html

row=0;
for row in range(0,len(df)):
    html = fancy_html(row)

    iframe = branca.element.IFrame(html=html, width=350,height=200)
    popup=folium.Popup(iframe, parse_html=True)
    #text=folium.Html(df.NAME[row]+' | '+ str(df.PROJECT[row])+' MW',script=True)
    
    folium.Marker([df.LAT[row],df.LONG[row]],
    popup=popup).add_to(m)
    m.save('chatlekha_map.html')
                  
