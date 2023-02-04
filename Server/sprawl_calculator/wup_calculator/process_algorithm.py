from urban_sprawl.raster_helper.raster_downloader import download_raster
from urban_sprawl.raster_helper.raster_operations import clip_raster_with_geojson
from urban_sprawl.dis.dis_calculator import DisCalculator

'''
The "processAlgorithm" method is a part of the QGIS Processing Framework 
and it is used to perform some action for processing a raster and a vector layer.
'''

def processAlgorithm(url, geojson):

	# 1.Get the downloaded file as input raster layer.
	raster_file = download_raster(url)

	# 2.Check and add the necessary fields to the vector layer, such as "Dis" and "settlement_area".


	dis_calculator = DisCalculator(result_matrix)
	dis_value = dis_calculator.calculate()
	if dis_value == -1:
		feedback.reportError("Unable to Properly calculate Si_Raster")
		return -1.0

	geojson_object['properties']['Dis'] = float(dis_value)

	# 3.Run clip_raster_with_geojson() for the downloded raster and the geojson feature.
	clipped_raster_file = clip_raster_with_geojson(raster_file, geojson)

	# 4.Calculate and save the DIS for each feature using the calculate_and_save_dis() method.
	# 5.Calculate and save the WDIC for each feature using the calculate_and_save_wdis() method.
	# 6.Use the calculate() method to calculate the build-up area and settlement area for each feature.
	# 7.Return the results as a JSON object.

	raise NotImplementedError
