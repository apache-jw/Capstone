# Capstone Electric Vehicle Analysis 

The adoption of electric vehicles (EVs) is rapidly increasing, presenting both opportunities and challenges for car companies. We collected structured data on existing EV charging station locations, usage patterns, and capacity from the Alternative Fuels Data Center (AFDC) made available by the National Renewable Energy Laboratory (NREL) API. To capture regional nuances in EV charging infrastructure deployment and usage patterns, we gathered data from state and local sources. The California Electric Vehicle Infrastructure Plan and the CalTrans Open Data Portal are examples of such sources that provide insights into state-level initiatives and granular charging station data. Furthermore, we source data from utility companies to obtain information on their EV charging programs, grid integration efforts, and relevant datasets that can enhance our understanding of the EV ecosystem.

- *EVSE.ipynb utilizes data from AFDC to create a simple Python Folium map with added shapefiles from Caltrans Open data.*
- *Sample API GET Calls to '[Openchargemap](https://openchargemap.org/site)','[CalTrans HWY Data](https://caltrans-gis.dot.ca.gov/arcgis/rest/services/CHhighway)', '[AFDC](https://developer.nrel.gov/)' are provided.*

- *Additional Layers using from '[CA Electric Vehicle Charging Station Permit Streamlining Map](https://business.ca.gov/industries/zero-emission-vehicles/plug-in-readiness/)'

- Future Implementation of CalTrans Performance Measurement System '[(PeMS)](https://pems.dot.ca.gov/)' would provide more robust display of bottlenecks versus overlaying static shapefiles

#### References: 
- '[Total Public and Share Private Chargers, *California Energy Commission*](https://tableau.cnra.ca.gov/t/CNRA_CEC_PUBLIC/views/DMVDataPortal/ZEVInfrastructure?:embed=y&:isGuestRedirectFromVizportal=y&:display_count=n&:showAppBanner=false&:origin=viz_share_link&:showVizHome=n)'
- '[Priority Populations, *California Climate Investments*](https://gis.carb.arb.ca.gov/portal/apps/experiencebuilder/experience/?id=6b4b15f8c6514733972cabdda3108348)
