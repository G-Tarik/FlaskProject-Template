$(window).ready(
  function() {	
	var socket = io.connect();
	socket.on( 'connect', function() {
		socket.emit( 'client_connected', {'data': 'New client on websocket.'} );
	});
	socket.on( 'UpdateData', refreshData.bind() );
  }
);

function refreshData( data ) {
	$.each( data, function( key, value ) {
		$('#ws_box').text( value+'%' );
	});
}

