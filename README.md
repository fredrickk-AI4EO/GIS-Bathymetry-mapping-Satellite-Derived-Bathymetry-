# GIS-Bathymetry-mapping-Satellite-Derived-Bathymetry-
Data  source, sites, satellite imagery archives,  
Day one notes in the process of being recovered.
SDB_production : MBT Ratio
Random Forest SDB (Depth prediction)-(Calibration =70%, Validation = 30%) 

Satellite Derived Bathymetry Post_Processing: .
                    Reflectance threshold-(low/hih Threshold)
                    Masking
                    
                    DAY 3
Satellite Derived Bathymetry QA/QC (statistical tools(point data, raster data, output, check-point data positive down & raster positive down)
                                        Evaluating QA/QC outputs
                                        Sattelite Derived Bathymetry outlier mitigation and improving results: Tools for outlier itigation- ESRI's ArcGISpro pixel editor(2D top-down editing)
                                                                                                                      Pure File Magic(PFM)-(D point cloud)
                                                                                                                      Other Hydrographic software(Caris, Fledermaus, QRS)
                                        Glint correction- Individual band,: Task: Running QA/QC tools on the RF data, and the visualizations

    Develop plan for improving SDB
Considerations:(Image captured on Tecno cammon 17 phn, date:(20/11/25))



                    Day 4

Pre-processing(imagery selected, in-situ data selected, dividing data into calibration and validataion, applying SDB Algorithm)

SDB ingredients- Imagery and In-situ data
Environmnental factors_Negative(clouds, Specular reflection etc)
                        Positive(calm clear water, no river discharge)


SDB Algorithms_ Band ration method, Random Forest 
Outlier Mitigation(boats etc-taken out)
Improving Results:
                  Detracting factors: SDB model poor depth estimation, compared to in-situ or visual assesment 

  Actions: Re-process - Evaluate/ mitigate in-situ outliers 
                        Re-configure parameters; RF:adjust trees/tree depth
                                                  Ratioo; Change representation type or improve regression fit


SDB-Mombasa(Data is Available-Project was done and data is with Alwx)
Tcarta products{ Basemaps, Global Bathymetry, Object Detection SAR shoreline, SAR Oil detection Seafloor classificatin, Seafllor classification, Water quality monitoring, Satellite Reconnainssance charts


Blue carbon(sea grass, coral, algae, mangroves)
Task: Uploa Mozambique SDB geotiff from the link(provided)
SESNSOR FUSSION FOR SCALABLE BATHYMETRIC MAPPING(Abu Dhadi Emirate, Red Sea)

Space Based hydrospatial: Radiative transfer SDB (Check the IDA software for this purpose)
                        : Wave Kinematic Bathymetry 
                        : Synthetic Aperture Radar(SAR)
                        : Seafloor Classification
                        : Seagrass Density & Loss
                        : Intertidal Classification
                        : Water quality 
SDB Data Sources: Sentinel-2 Data
                : ICEat-2 ATL24 access
                : SkyFI
                : Maxar Connect

Remote Sensing journal Article: Random Forest Regression in Python(blog post)
Data Source: (https://nsidc.org/data/atl24/versions/1)-(https://nsidc.org/data/ATL24/versions/1)

          DAY 5
Applications of SDB in support of Hydrographic Survey
infill coastal gaps, risk reduction, Improve efficiency
Marine Remote Sensing(The Red Sea)

                        









