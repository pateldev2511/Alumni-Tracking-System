function initialize() {

	var mapOptions, map, marker, searchBox,searchBox2,
		infoWindow = '',
		addressEl = document.querySelector( '#map-search' ),addressEl2 = document.querySelector( '#map-search2' ),
		element = document.getElementById( 'map-canvas' );

	mapOptions = {
		// How far the maps zooms in.
		zoom: 8,
		// Current Lat and Long position of the pin/
		center: new google.maps.LatLng( 18.5204, 73.8567 ),
		// center : {
		// 	lat: -34.397,
		// 	lng: 150.644
		// },
		disableDefaultUI: false, // Disables the controls like zoom control on the map if set to true
		scrollWheel: true, // If set to false disables the scrolling on the map.
		draggable: true, // If set to false , you cannot move the map around.
		// mapTypeId: google.maps.MapTypeId.HYBRID, // If set to HYBRID its between sat and ROADMAP, Can be set to SATELLITE as well.
		// maxZoom: 11, // Wont allow you to zoom more than this
		// minZoom: 9  // Wont allow you to go more up.

	};

	/**
	 * Creates the map using google function google.maps.Map() by passing the id of canvas and
	 * mapOptions object that we just created above as its parameters.
	 *
	 */
	// Create an object map with the constructor function Map()
	map = new google.maps.Map( element, mapOptions ); // Till this like of code it loads up the map.

	/**
	 * Creates the marker on the map
	 *
	 */
	marker = new google.maps.Marker({
		position: mapOptions.center,
		map: map,
		// icon: 'http://pngimages.net/sites/default/files/google-maps-png-image-70164.png',
		draggable: true
	});

	/**
	 * Creates a search box
	 */
	searchBox = new google.maps.places.SearchBox( addressEl );
	searchBox2 = new google.maps.places.SearchBox( addressEl2 );
	/**
	 * When the place is changed on search box, it takes the marker to the searched location.
	 */
	google.maps.event.addListener( searchBox, 'places_changed', function () {
		var places = searchBox.getPlaces(),
			bounds = new google.maps.LatLngBounds(),
			i, place, lat, long, resultArray,
			addresss = places[0].formatted_address;

		for( i = 0; place = places[i]; i++ ) {
			bounds.extend( place.geometry.location );
			marker.setPosition( place.geometry.location );  // Set marker position new.
		}

		map.fitBounds( bounds );  // Fit to the bound
		map.setZoom( 15 ); // This function sets the zoom to 15, meaning zooms to level 15.
		// console.log( map.getZoom() );

		lat = marker.getPosition().lat();
		long = marker.getPosition().lng();

		resultArray =  places[0].address_components;

		// Get the city and set the city input value to the one selected
		for( var i = 0; i < resultArray.length; i++ ) {
			console.log(resultArray[ i ]);
			if ( resultArray[ i ].types[0] && "locality" === resultArray[ i ].types[0] ) {
				var city = resultArray[ i ].long_name;
				console.log("City : "+city);
			}
			if ( resultArray[ i ].types[0] && 'administrative_area_level_1' === resultArray[ i ].types[0] ) {
				var stat = resultArray[ i ].long_name;
				console.log("State : "+stat );
			}
			if ( resultArray[ i ].types[0] && 'country' === resultArray[ i ].types[0] ) {
				var countr = resultArray[ i ].long_name;
				console.log("Country : "+countr );
			}
		}

		var x_y = "";
				if(city.length != 0 )
				{
					x_y = x_y + city + ",";
				}
				if(stat.length != 0)
				{
					x_y = x_y + stat + ",";
				}
				if(countr.length != 0)
				{
					x_y = x_y + countr + ".";
				}
				addressEl.value = x_y;




		// Closes the previous info window if it already exists
		if ( infoWindow ) {
			infoWindow.close();
		}
		/**
		 * Creates the info Window at the top of the marker
		 */
		infoWindow = new google.maps.InfoWindow({
			content: addresss
		});

		infoWindow.open( map, marker );
	} );


	google.maps.event.addListener( searchBox2, 'places_changed', function () {
		var places = searchBox2.getPlaces(),
			bounds = new google.maps.LatLngBounds(),
			i, place, lat, long, resultArray,
			addresss = places[0].formatted_address;

		for( i = 0; place = places[i]; i++ ) {
			bounds.extend( place.geometry.location );
			marker.setPosition( place.geometry.location );  // Set marker position new.
		}

		map.fitBounds( bounds );  // Fit to the bound
		map.setZoom( 15 ); // This function sets the zoom to 15, meaning zooms to level 15.
		// console.log( map.getZoom() );

		lat = marker.getPosition().lat();
		long = marker.getPosition().lng();

		resultArray =  places[0].address_components;
		// console.log(resultArray);
		// Get the city and set the city input value to the one selected
		for( var i = 0; i < resultArray.length; i++ ) {
			console.log(resultArray[ i ]);

			if ( resultArray[ i ].types[0] && "locality" === resultArray[ i ].types[0] ) {
				var city = resultArray[ i ].long_name;
				console.log("City : "+city);
			}
			if ( resultArray[ i ].types[0] && 'administrative_area_level_1' === resultArray[ i ].types[0] ) {
				var stat = resultArray[ i ].long_name;
				console.log("State : "+stat );
			}
			if ( resultArray[ i ].types[0] && 'country' === resultArray[ i ].types[0] ) {
				var countr = resultArray[ i ].long_name;
				console.log("Country : "+countr );
			}
		}

		var x_y = "";
				if(city.length != 0 )
				{
					x_y = x_y + city + ",";
				}
				if(stat.length != 0)
				{
					x_y = x_y + stat + ",";
				}
				if(countr.length != 0)
				{
					x_y = x_y + countr + ".";
				}
				addressEl2.value = x_y;




		// Closes the previous info window if it already exists
		if ( infoWindow ) {
			infoWindow.close();
		}
		/**
		 * Creates the info Window at the top of the marker
		 */
		infoWindow = new google.maps.InfoWindow({
			content: addresss
		});

		infoWindow.open( map, marker );
	} );

	/**
	 * Finds the new position of the marker when the marker is dragged.
	 */
	google.maps.event.addListener( marker, "dragend", function ( event ) {
		var lat, long, address, resultArray, citi;

		console.log( 'i am dragged' );
		lat = marker.getPosition().lat();
		long = marker.getPosition().lng();

		var geocoder = new google.maps.Geocoder();
		geocoder.geocode( { latLng: marker.getPosition() }, function ( result, status ) {
			if ( 'OK' === status ) {  // This line can also be written like if ( status == google.maps.GeocoderStatus.OK ) {
				address = result[0].formatted_address;
				resultArray =  result[0].address_components;
				// Get the city and set the city input value to the one selected
				for( var i = 0; i < resultArray.length; i++ ) {
					if ( resultArray[ i ].types[0] && 'administrative_area_level_2' === resultArray[ i ].types[0] ) {
						var city = resultArray[ i ].long_name;
						console.log("City : "+city);
					}
					if ( resultArray[ i ].types[0] && 'administrative_area_level_1' === resultArray[ i ].types[0] ) {
						var stat = resultArray[ i ].long_name;
						console.log("State : "+stat );
					}
					if ( resultArray[ i ].types[0] && 'country' === resultArray[ i ].types[0] ) {
						var countr = resultArray[ i ].long_name;
						console.log("Country : "+countr );
					}

				}
				var x_y = "";
				if(city.length != 0 )
				{
					x_y = x_y + city + ",";
				}
				if(stat.length != 0)
				{
					x_y = x_y + stat + ",";
				}
				if(countr.length != 0)
				{
					x_y = x_y + countr + ".";
				}
				addressEl.value = x_y;


			

			} else {
				console.log( 'Geocode was not successful for the following reason: ' + status );
			}

			// Closes the previous info window if it already exists
			if ( infoWindow ) {
				infoWindow.close();
			}

			/**
			 * Creates the info Window at the top of the marker
			 */
			infoWindow = new google.maps.InfoWindow({
				content: address
			});

			infoWindow.open( map, marker );
		} );
	});


}